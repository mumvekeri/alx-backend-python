import asyncio
import random

async def wait_random(max_delay=10):
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def main():
    random_delay = await wait_random()
    print(f"Random delay: {random_delay:.2f} seconds")

asyncio.run(main())
