import pytest
from testcontainers.postgres import PostgresContainer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.session import Base
from app.db import models, crud, schemas

pytestmark = pytest.mark.docker

def test_postgres_integration():
    with PostgresContainer("postgres:16") as pg:
        engine = create_engine(pg.get_connection_url(), future=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine, future=True)
        with Session() as db:
            user = crud.create_user(db, schemas.UserCreate(email="tc@example.com", full_name="TC"))
            assert user.id is not None
