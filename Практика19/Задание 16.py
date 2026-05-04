import asyncio

async def task(name, delay):
    await asyncio.sleep(delay)
    print(f"Задача {name} завершена")

async def main():
    await asyncio.gather(
        task("A", 2),
        task("B", 1),
        task("C", 3)
    )

asyncio.run(main())