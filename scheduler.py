import asyncio, logging
from typing import Callable, List

log = logging.getLogger(__name__)

class JobScheduler:
    def __init__(self):
        self.jobs: List[tuple[int, Callable]] = []

    def add_job(self, coro: Callable, interval: int):
        """Register async function to run every <interval> seconds."""
        self.jobs.append((interval, coro))

    async def _wrap(self, coro, delay):
        while True:
            try:
                await coro()
            except Exception as e:
                log.error("Job %s failed: %s", coro.__name__, e, exc_info=True)
            await asyncio.sleep(delay)

    async def run_forever(self):
        await asyncio.gather(
            *[self._wrap(coro, delay) for delay, coro in self.jobs]
        )
