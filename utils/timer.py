from time import monotonic_ns
import logging

logger = logging.getLogger(__name__)


class Timer:
    def __init__(self, message=None, quiet=False):
        self.durations = {}
        self.message = [message]
        self.quiet = quiet
        self.start = []

    def __call__(self, message=None):
        self.message.append(message or f'running code #{len(self.durations)}')
        return self

    def __enter__(self):
        self.start.append(monotonic_ns())
        if not self.quiet:
            logger.info(f'Started {self.message[-1]}')

    def __exit__(self, exc_type, exc_val, exc_tb):
        start = self.start.pop()
        message = self.message.pop()
        end = monotonic_ns()
        duration = (end - start) / 1_000_000_000
        if(message not in self.durations):
            self.durations[message] = 0.0
        self.durations[message] += duration
        if not self.quiet:
            logger.info(f'Finished {message} in {duration:.3f}sec')

    def reset(self):
        self.durations = {}

    def get_time_by_key(self, message):
        try:
            return self.durations[message]
        except:
            return 0.0

    def __str__(self) -> str:
        return '\n'.join(f'{msg}\t{duration}' for msg, duration in self.durations.items())

    def __dict__(self) -> dict:
        return dict(self.durations)


timer = Timer(quiet=True)

if __name__ == '__main__':
    #logging.basicConfig(level=logging.INFO)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    import time
    # usage
    # with timer("name")
    # logger.info(timer.__dict__())
    timer.reset()
    with timer('some name'):
        time.sleep(0.5)
        logger.info("hello")
    logger.info(timer.__dict__())

