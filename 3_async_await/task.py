import asyncio, time

async def delay(delay_time):
    print(f"{time.ctime()}: started sleeping for {delay_time} seconds")
    await asyncio.sleep(delay_time)
    print(f"{time.ctime()}: Finished sleeping for {delay_time} seconds")

async def main():
    #non-blocking
    delay_7 = asyncio.create_task(delay(7))
    delay_2 = asyncio.create_task(delay(2))
    delay_3 = asyncio.create_task(delay(3))

    print(type(delay_2))
    #blocking
    # await asyncio.sleep(10)
    await delay_7
    await delay_2
    await delay_3

asyncio.run(main())
