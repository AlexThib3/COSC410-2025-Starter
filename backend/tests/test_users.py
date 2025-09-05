import pytest
from httpx import AsyncClient, ASGITransport
from asgi_lifespan import LifespanManager
from app.main import app
from app.db.session import reset_db

@pytest.mark.asyncio
async def test_create_and_list_users():
    reset_db()
    async with LifespanManager(app):
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as ac:
            resp = await ac.post("/api/v1/users/", json={"email": "a@example.com", "full_name": "A User"})
            assert resp.status_code == 201, resp.text
            resp = await ac.get("/api/v1/users/")
            assert resp.status_code == 200
            users = resp.json()
            assert any(u["email"] == "a@example.com" for u in users)
