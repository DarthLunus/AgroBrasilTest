from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import ValidationError
from domain.models import CarDetails, Vehicle
from domain.services import calculate_premium
from core.database import get_db
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/calculate_premium")
def get_premium(car: CarDetails, db: Session = Depends(get_db)):
    try:
        # Calculando o prêmio
        premium_data = calculate_premium(car)
        
        # Criando o veículo no banco de dados
        vehicle = Vehicle(**car.dict())
        db.add(vehicle)
        db.commit()
        db.refresh(vehicle)

        # Retornando o resultado
        return JSONResponse(content=premium_data, status_code=status.HTTP_200_OK)
    
    except ValidationError as ve:
        # Erro de validação dos dados de entrada
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(ve))
    except Exception as e:
        # Captura de outros erros e retorno com status 500
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
