import time
import functools
import random


def retry(
    *,
    retries: int = 3,
    base_delay: float = 1.0,
    max_delay: float = 8.0,
    jitter: float = 0.2,
    allowed_exceptions: tuple[type[Exception], ...] = (Exception,),
):
    """
    Exponential backoff retry decorator.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0

            while True:
                try:
                    return func(*args, **kwargs)

                except allowed_exceptions as e:
                    attempt += 1
                    if attempt > retries:
                        raise

                    delay = min(
                        max_delay,
                        base_delay * (2 ** (attempt - 1))
                    )
                    delay += random.uniform(0, jitter)

                    print(
                        f"⚠️ Retry {attempt}/{retries} "
                        f"after {delay:.2f}s due to: {e}"
                    )
                    time.sleep(delay)

        return wrapper
    return decorator
