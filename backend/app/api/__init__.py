from fastapi import APIRouter
from .v1 import users

router = APIRouter()
router.include_router(users.router, prefix="/v1/users", tags=["users"])
