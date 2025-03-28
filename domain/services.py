import os
from datetime import datetime
from domain.models import CarDetails
from core.config import COVERAGE_PERCENTAGE  # Importando do arquivo de configuração

def calculate_rate(car: CarDetails, current_year: int = None, base_value: int = 10000) -> float:
    """
    Calcula a taxa de seguro com base na idade e valor do carro.
    :param car: Detalhes do carro.
    :param current_year: O ano atual, para calcular a idade do carro. Se não fornecido, usa o ano atual.
    :param base_value: Base de valor para o cálculo de valor rate. Padrão é 10.000.
    :return: A taxa calculada.
    """
    if current_year is None:
        current_year = datetime.now().year

    age_rate = (current_year - car.year) * 0.005
    value_rate = (car.value // base_value) * 0.005
    return age_rate + value_rate

def calculate_premium(car: CarDetails) -> dict:
    """
    Calcula o prêmio final de seguro com base nos detalhes do carro.
    :param car: Detalhes do carro.
    :return: Dicionário com os detalhes do prêmio calculado.
    """
    rate = calculate_rate(car)
    base_premium = car.value * rate
    deductible_discount = base_premium * car.deductible_percentage
    final_premium = base_premium - deductible_discount + car.broker_fee
    policy_limit = car.value * COVERAGE_PERCENTAGE
    deductible_value = policy_limit * car.deductible_percentage
    final_policy_limit = policy_limit - deductible_value
    
    return {
        "car_details": car.dict(),
        "applied_rate": rate,
        "policy_limit": final_policy_limit,
        "calculated_premium": final_premium,
        "deductible_value": deductible_value,
    }
