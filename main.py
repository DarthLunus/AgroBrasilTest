from fastapi import FastAPI
from api.routes import router
from core.database import Base, engine
import logging

# Configuração básica de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Incluir as rotas
app.include_router(router)

# Criar todas as tabelas do banco de dados (desenvolvimento)
def create_tables():
    try:
        Base.metadata.create_all(bind=engine)
        logger.info("Tabelas do banco de dados criadas com sucesso.")
    except Exception as e:
        logger.error(f"Erro ao criar as tabelas: {e}")
        raise

# Chamada para criar as tabelas ao iniciar a aplicação
create_tables()

# Endpoint de verificação de saúde
@app.get("/")
def health_check():
    return {"status": "API is running"}
