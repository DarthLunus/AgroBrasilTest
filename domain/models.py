from pydantic import BaseModel, Field
from typing import Optional
from sqlalchemy import Column, Integer, String, Float
from core.database import Base

class CarDetails(BaseModel):
    make: str
    model: str
    year: int
    value: float
    deductible_percentage: float = Field(..., ge=0, le=1, description="Deductible percentage, between 0 and 1")
    broker_fee: float = Field(..., gt=0, description="Broker fee should be a positive value")
    registration_location: Optional[str] = None

    class Config:
        orm_mode = True  # Permite que o Pydantic modele os dados SQLAlchemy diretamente.

class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    make = Column(String, index=True)
    model = Column(String, index=True)
    year = Column(Integer)
    value = Column(Float)
    deductible_percentage = Column(Float)
    broker_fee = Column(Float)
    registration_location = Column(String, nullable=True)

    def __repr__(self):
        return f"<Vehicle(id={self.id}, make={self.make}, model={self.model}, year={self.year}, value={self.value}, deductible_percentage={self.deductible_percentage}, broker_fee={self.broker_fee}, registration_location={self.registration_location})>"
