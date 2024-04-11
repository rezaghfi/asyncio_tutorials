import asyncio
import functools
import os
import signal


def handle_exit_signal(signal_name, event_loop):
    print(f"Received signal {signal_name}: exiting")
    event_loop.stop()

async def run_event_loop():
    event_loop = asyncio.get_running_loop()

    for  signal_name in ('SIGINT', 'SIGTERM'):
        event_loop.add_signal_handler(getattr(signal, signal_name), functools.partial(handle_exit_signal, signal_name, event_loop))
    await asyncio.sleep(3600)

print("Event loop running for 1 hour, press ctrl+c to interrupt.")
print(f"pid {os.getpid()}: send SIGINT or SIGTERM to exit.")

asyncio.run(run_event_loop())