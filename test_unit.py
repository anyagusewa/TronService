import pytest
from unittest.mock import MagicMock
from sqlalchemy.ext.asyncio import AsyncSession
from main import get_wallet_data
from schemas import TronRequestCreate

@pytest.mark.asyncio
async def test_db_insertion():
    mock_db = MagicMock(AsyncSession)

    test_data = TronRequestCreate(address="TEvpZmxvtd6gDcCnq4qSjsnYvq2bsHQSZr")

    mock_tron = MagicMock()
    mock_tron.get_account.return_value = {
        "balance": 1000,
        "bandwidth": 10,
        "energy": 5
    }

    response = await get_wallet_data(test_data, mock_db)

    mock_db.add.assert_called_once_with(response)
    mock_db.commit.assert_called_once()
