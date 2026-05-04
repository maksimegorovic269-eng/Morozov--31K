import asyncio
async def worker(name, q):
    while True:
        task = await q.get()
        print(f"{name} выполняет {task}")
        await asyncio.sleep(1)
        q.task_done()

async def main():
    q = asyncio.Queue()

    for i in range(5):
        await q.put(f"Task-{i}")

    workers = [asyncio.create_task(worker(f"W{i}", q)) for i in range(3)]

    await q.join()

    for w in workers:
        w.cancel()

asyncio.run(main())