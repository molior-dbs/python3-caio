import asyncio

from caio.linux_aio_asyncio import AsyncioContext
from benchmark_write_common import main


if __name__ == "__main__":
    asyncio.run(main(AsyncioContext))