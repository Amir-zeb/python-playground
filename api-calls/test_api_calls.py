import httpx
import pytest
from api_calls import get_price_async,get_price_sync

def test_get_price_sync_extracts_correct_price(monkeypatch):
    fake_response_data = {"bitcoin": {"usd": 65000.0}}
    
    class FakeResponse:
        def json(self):
            return fake_response_data
    
    def fake_get(url):
        return FakeResponse()
    
    monkeypatch.setattr(httpx, "get", fake_get)
    
    result = get_price_sync("bitcoin")
    assert result == 65000.0
    
@pytest.mark.asyncio
async def test_get_price_async_extracts_correct_price(monkeypatch):
    fake_response_data = {"ethereum": {"usd": 3200.0}}
    
    class FakeResponse:
        def json(self):
            return fake_response_data
    
    class FakeAsyncClient:
        async def get(self, url):
            return FakeResponse()
    
    result = await get_price_async(FakeAsyncClient(), "ethereum")
    assert result == 3200.0

@pytest.mark.asyncio
async def test_get_price_async_crashes(monkeypatch):
    fake_response_data = {"ethereum": {"usd": 3200.0}}
    
    class FakeResponse:
        def json(self):
            return fake_response_data
    
    class FakeAsyncClient:
        async def get(self, url):
            return FakeResponse()
    
    with pytest.raises(KeyError):
            await get_price_async(FakeAsyncClient(), "bitcoin")