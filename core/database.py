import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter a URL do banco de dados da variável de ambiente ou usar um valor padrão
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./car_insurance.db")

# Configuração do banco de dados
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in SQLALCHEMY_DATABASE_URL else {})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """
    Retorna uma sessão do banco de dados que pode ser usada para interagir com o banco.
    
    Esta função utiliza o gerenciador de contexto (yield) para garantir que a
    sessão seja fechada após o uso.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
