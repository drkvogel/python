#!/usr/bin/env python3

import asyncio

print("Hello, World!")

async def count():
  print("One")
  await asyncio.sleep(1)
  print("Two")

async def main():
  await asyncio.gather(count(), count(), count())

  # count() # RuntimeWarning: coroutine 'count' was never awaited

  # await count()
  # await count()
  # await count()
  # executes as if synchronous  

if __name__ == "__main__":
  import time
  s = time.perf_counter()
  asyncio.run(main())
  elapsed = time.perf_counter() - s
  print(f'{__file__} executed in {elapsed:0.2f} seconds')

"""
❯ ./count_async.py
Hello, World!
One
One
One
Two
Two
Two
./count_async.py executed in 1.00 seconds
"""
