import asyncio

#coroutine
async def main():
    print("hello this is an event in event_loop")

#create event loop with run api
asyncio.run(main())