import asyncio, time


async def main():
    print(f"{time.ctime()}: Coroutine started")
    # after await have 1.coroutine 2.task 3.future
    await asyncio.sleep(1)
    print(f"{time.ctime()}: Coroutine completed")

asyncio.run(main())