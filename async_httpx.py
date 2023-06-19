import asyncio
import httpx
from time import perf_counter

async def async_version():
    urls = [f"http://localhost:8000/items/{item_id}" for item_id in range(1, 11)]

    async with httpx.AsyncClient() as client:
        for url in urls:
            response = await client.get(url)
            print(response.json())

def main():
    start = perf_counter()
    asyncio.run(async_version())
    stop = perf_counter()
    print("Time taken: ", stop-start)
    # Time taken:  0.34013409999897704

if __name__ == "__main__":
    main()