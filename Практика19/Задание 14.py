import asyncio

async def hello():
    await asyncio.sleep(1)
    print("Привет")

asyncio.run(hello())