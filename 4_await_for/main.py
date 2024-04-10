import asyncio, time

from asyncio import exceptions

async def delay(delay_time):
    print(f"{time.ctime()}: started sleeping for {delay_time} seconds")
    await asyncio.sleep(delay_time)
    print(f"{time.ctime()}: Finished sleeping for {delay_time} seconds")

async def main():
    delay_2 = asyncio.create_task(delay(2))
    delay_70 = asyncio.create_task(delay(70))
    try:
        await asyncio.wait_for(delay_2, timeout=3)
        await asyncio.wait_for(delay_70, timeout=2)
    except exceptions.TimeoutError:
        print("Is delay(2) canceled?", delay_2.cancelled())
        print("Is delay(70) canceled?", delay_70.cancelled())
asyncio.run(main())
