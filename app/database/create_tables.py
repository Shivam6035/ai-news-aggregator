# import sys
# from pathlib import Path

# sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# from app.database.models import Base
# from app.database.connection import engine

# if __name__ == "__main__":
#     Base.metadata.create_all(engine)
#     print("Tables created successfully")

import sys
from pathlib import Path
from sqlalchemy import create_engine

# Keep your path fix so Python can find the 'app' module
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from app.database.models import Base

# STEP 2 FIX: Explicitly target Docker container on port 5433
DOCKER_DATABASE_URL = "postgresql://postgres:postgres@localhost:5433/ai_news_aggregator"
docker_engine = create_engine(DOCKER_DATABASE_URL)

if __name__ == "__main__":
    print("Connecting to Docker PostgreSQL on port 5433...")
    Base.metadata.create_all(docker_engine)
    print("Tables created successfully!")