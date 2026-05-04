import asyncio

async def producer(q):
    for i in range(5):
        await q.put(i)
        print(f"Произведено {i}")

async def consumer(q):
    while True:
        item = await q.get()
        print(f"Потреблено {item}")
        q.task_done()

async def main():
    q = asyncio.Queue()

    prod = asyncio.create_task(producer(q))
    cons = asyncio.create_task(consumer(q))

    await prod
    await q.join()
    cons.cancel()

asyncio.run(main())