import asyncio

async def eternity():
    # Sleep for one hour
    await asyncio.sleep(3)
    print('yay!')

async def main():
    # Wait for at most 1 second
    try:
        #loop = asyncio.get_event_loop()
        await asyncio.wait_for(eternity(), timeout=1.0)
    except asyncio.TimeoutError:
        print('timeout!')

asyncio.run(main())