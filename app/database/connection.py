import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

def get_database_url() -> str:
    user = os.getenv("POSTGRES_USER", "postgres")
    password = os.getenv("POSTGRES_PASSWORD", "postgres")
    host = os.getenv("POSTGRES_HOST", "localhost")
    port = os.getenv("POSTGRES_PORT", "5433")
    db = os.getenv("POSTGRES_DB", "ai_news_aggregator")
    return f"postgresql://{user}:{password}@{host}:{port}/{db}"

engine = create_engine(get_database_url())
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session():
    return SessionLocal()


# import os
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base

# # Force port 5433 to securely bypass the local Windows Postgres service
# DATABASE_URL = os.getenv(
#     "DATABASE_URL", 
#     "postgresql://postgres:postgres@localhost:5433/ai_news_aggregator"
# )

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

# # ADDED FOR THE REPOSITORY: Context manager function for session retrieval
# def get_session():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # Keeping get_db just in case other files use it
# def get_db():
#     yield from get_session()