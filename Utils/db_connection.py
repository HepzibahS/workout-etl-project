from sqlalchemy import create_engine

def get_engine():
    return create_engine("postgresql+psycopg2://postgres@localhost:5432/ETL_Project")
