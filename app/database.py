from dotenv import load_dotenv

load_dotenv()  # Load all environment variables from the .env file

import os  # To get environment variables

from sqlmodel import Session, SQLModel, create_engine

DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_engine(DATABASE_URL)


async def init_db():
    SQLModel.metadata.create_all(engine)
