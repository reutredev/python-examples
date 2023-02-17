import time
import asyncio
import httpx

async def fetch():
    urls = ["https://books.toscrape.com/catalogue/page-1.html",
            "https://books.toscrape.com/catalogue/page-2.html",
            "https://books.toscrape.com/catalogue/page-3.html",
            "https://books.toscrape.com/catalogue/page-4.html"]

    async with httpx.AsyncClient() as client:
        reqs = [client.get(url) for url in urls]
        results = await asyncio.gather(*reqs)
    print(results)

start = time.perf_counter()
asyncio.run(fetch())
end = time.perf_counter()
print(end-start)


