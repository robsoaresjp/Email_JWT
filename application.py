from dotenv import load_dotenv
from flask import Flask
from models import initialize_database
from os import environ
from resources import initialize_resources
from schema.schema_file import Schema
from sqlalchemy import create_engine

# Iniciando o aplicativo Flask
application = Flask(__name__)

# Carregando variáveis de ambiente do arquivo .env apenas em desenvolvimento
if environ.get('EBS_ENVIRONMENT') in ['local', None]:
    load_dotenv('./environments/local.env')

# Carregando variáveis de ambiente no aplicativo Flask
for item in environ.items():
    application.config[item[0]] = item[1]

# Iniciando a configuração do banco de dados
initialize_database(application)

# Iniciando endpoints RESTfull
initialize_resources(application)

@application.before_first_request
def startup():
    print("Inicializando o bd de migração")

    Schema.migration()
    Schema.prepare_db()

# Executar aplicativo
if __name__ == '__main__':
    application.run(threaded=True)
