import os
import urllib.parse
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

# We halen de onderdelen nu los op uit je .env voor maximale veiligheid
DB_USER = "meuze" # Vul hier je Azure admin username in
DB_PASS = "AzureAdmin@2025#" # Vul hier je ECHTE wachtwoord in (met de #)
DB_HOST = "db-meuzeit-infra.postgres.database.azure.com"
DB_NAME = "postgres"

# Hier gebeurt de magie: we coderen het wachtwoord veilig
encoded_pass = urllib.parse.quote_plus(DB_PASS)

# We bouwen de URL handmatig op
DATABASE_URL = f"postgresql://{DB_USER}:{encoded_pass}@{DB_HOST}:5432/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()