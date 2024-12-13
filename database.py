from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Corrected PostgreSQL connection string
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost/students"

# Create the SQLAlchemy engine (no check_same_thread for PostgreSQL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for model classes
Base = declarative_base()