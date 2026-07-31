import httpx
import asyncio
import time

COINS = ["bitcoin", "ethereum", "dogecoin", "solana", "cardano"]

def get_price_sync(coin: str) -> float:
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
    response = httpx.get(url)
    data = response.json()
    print(data)
    return data[coin]["usd"]

async def get_price_async(client: httpx.AsyncClient, coin: str) -> float:
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
    response = await client.get(url)
    data = response.json()
    return data[coin]["usd"]

async def main() -> None:
    start = time.perf_counter()
    for c in COINS:
        res = get_price_sync(c)
        print(res)
    elapsed = time.perf_counter() - start
    print(f"Sync took {elapsed:.2f}s") # took around 2s
    
    start = time.perf_counter()
    async with httpx.AsyncClient() as client:
        res=await asyncio.gather(*(get_price_async(client, c) for c in COINS))
        print("🚀 ~ main ~ res:", res)
    elapsed = time.perf_counter() - start
    print(f"Async took {elapsed:.2f}s") # took around 0.51s

if __name__ == "__main__":
    # main()
    asyncio.run(main())