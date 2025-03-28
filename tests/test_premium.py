from fastapi.testclient import TestClient
from main import app
from core.config import COVERAGE_PERCENTAGE

client = TestClient(app)

def test_calculate_premium():
    # Teste com valores válidos
    response = client.post("/calculate_premium", json={
        "make": "Toyota",
        "model": "Corolla",
        "year": 2015,
        "value": 20000,
        "deductible_percentage": 0.1,
        "broker_fee": 50.0
    })
    assert response.status_code == 200
    response_json = response.json()

    # Verificar se o prêmio calculado está presente
    assert "calculated_premium" in response_json

    # Calcular manualmente o prêmio esperado
    rate = (2025 - 2015) * 0.005 + (20000 // 10000) * 0.005  # Cálculo da taxa
    base_premium = 20000 * rate
    deductible_discount = base_premium * 0.1
    final_premium = base_premium - deductible_discount + 50.0

    # Verificar se o valor do prêmio calculado é semelhante ao esperado
    assert abs(response_json["calculated_premium"] - final_premium) < 0.01

    # Verificar a presença da chave 'policy_limit'
    assert "policy_limit" in response_json

def test_invalid_deductible_percentage():
    # Teste com franquia inválida (acima de 1.0)
    response = client.post("/calculate_premium", json={
        "make": "Toyota",
        "model": "Corolla",
        "year": 2015,
        "value": 20000,
        "deductible_percentage": 1.1,
        "broker_fee": 50.0
    })
    assert response.status_code == 422  # Espera erro de validação

def test_missing_broker_fee():
    # Teste com fee de corretor faltando
    response = client.post("/calculate_premium", json={
        "make": "Toyota",
        "model": "Corolla",
        "year": 2015,
        "value": 20000,
        "deductible_percentage": 0.1
    })
    assert response.status_code == 200
    response_json = response.json()

    # Verificar se o prêmio é calculado corretamente, considerando broker_fee como 0
    rate = (2025 - 2015) * 0.005 + (20000 // 10000) * 0.005
    base_premium = 20000 * rate
    deductible_discount = base_premium * 0.1
    final_premium = base_premium - deductible_discount

    assert abs(response_json["calculated_premium"] - final_premium) < 0.01

def test_invalid_value():
    # Teste com valor negativo do carro
    response = client.post("/calculate_premium", json={
        "make": "Toyota",
        "model": "Corolla",
        "year": 2015,
        "value": -20000,
        "deductible_percentage": 0.1,
        "broker_fee": 50.0
    })
    assert response.status_code == 422  # Espera erro de validação
