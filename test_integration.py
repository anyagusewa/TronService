import httpx
import pytest

pytest_plugins = ["pytest_asyncio"]


@pytest.mark.asyncio
async def test_get_wallet_data():
    address = "TVmQM7BP7GdMHKY9hUEBjttCTJSaDHN888"

    async with httpx.AsyncClient(base_url="http://localhost:8000") as client:
        response = await client.post("/wallet", json={"address": address})

    assert response.status_code == 200
    assert "address" in response.json()
    assert "balance" in response.json()
    assert "bandwidth" in response.json()
    assert "energy" in response.json()


@pytest.mark.asyncio
async def test_get_wallets():
    async with httpx.AsyncClient(base_url="http://localhost:8000") as client:
        response = await client.get("/wallets?limit=3&offset=0")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) <= 3
