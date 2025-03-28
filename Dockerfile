# Usar uma imagem oficial do Python
FROM python:3.10

# Definir diretório de trabalho no container
WORKDIR /app

# Copiar somente o requirements.txt primeiro para melhorar o cache durante a construção da imagem
COPY requirements.txt .

# Instalar as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código-fonte para o diretório de trabalho
COPY . .

# Definir o comando padrão para rodar a aplicação com o Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
