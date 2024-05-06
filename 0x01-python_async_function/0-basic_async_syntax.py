#!/usr/bin/env python3

'''Task 0's module.
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Waits for a random number
    '''
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time

async def main():
    random_delay = await wait_random()
    print(f"Random delay: {random_delay:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())

