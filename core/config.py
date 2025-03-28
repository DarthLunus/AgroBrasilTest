import os
from dotenv import load_dotenv
from typing import Optional

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

def get_env_var(key: str, default: Optional[str] = None, var_type: type = str) -> Optional[str]:
    value = os.getenv(key, default)
    if value is None:
        raise ValueError(f"Missing environment variable: {key}")
    try:
        return var_type(value)
    except ValueError:
        raise ValueError(f"Invalid value for {key}. Expected type: {var_type.__name__}, got: {type(value).__name__}")

# Carregar e validar as configurações
COVERAGE_PERCENTAGE = get_env_var("COVERAGE_PERCENTAGE", "1.0", float)
