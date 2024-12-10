import os
from dotenv import load_dotenv

# Define o diretório raiz do projeto (BASE_DIR)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))

# Carrega as variáveis do arquivo .env
load_dotenv()

# Acessando as variáveis de banco de dados
DATABASE_URL_MYSQL = os.getenv("DATABASE_URL_MYSQL")
DATABASE_URL_MONGO = os.getenv("DATABASE_URL_MONGO")

# Acessando outras variáveis
SECRET_KEY = os.getenv("SECRET_KEY")
TEMP_DIR = os.getenv("TEMP_DIR")

# Aqui você pode armazenar as variáveis em um dicionário ou diretamente nas variáveis do seu código
config = {
    "DATABASE_URL_MYSQL": DATABASE_URL_MYSQL,
    "DATABASE_URL_MONGO": DATABASE_URL_MONGO,
    "SECRET_KEY": SECRET_KEY,
    "TEMP_DIR": TEMP_DIR
}

# Exemplo de como acessar uma variável
# print(config["DATABASE_URL_MYSQL"])  # Descomente se quiser exibir algo específico
