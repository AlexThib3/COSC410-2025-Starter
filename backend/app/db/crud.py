from sqlalchemy.orm import Session
from app.db import models, schemas

def get_user_by_email(db: Session, email: str) -> models.User | None:
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    obj = models.User(email=user.email, full_name=user.full_name)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def list_users(db: Session) -> list[models.User]:
    return db.query(models.User).all()
