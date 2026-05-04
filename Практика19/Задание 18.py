import asyncio
async def read_file(name):
    await asyncio.sleep(1)
    print(f"{name} прочитан")

async def main():
    await asyncio.gather(
        read_file("file1"),
        read_file("file2")
    )

asyncio.run(main())