from httpx import AsyncClient, ASGITransport
import pytest
from asgi_lifespan import LifespanManager
from app.main import app
from app.db.session import reset_db

@pytest.mark.asyncio
async def test_health():
    reset_db()
    async with LifespanManager(app):
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as ac:
            res = await ac.get("/health")
            assert res.status_code == 200
            assert res.json() == {"status": "ok"}
