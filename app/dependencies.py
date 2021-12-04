from app.database import Session, engine


def get_session():
    with Session(engine) as session:
        yield session
