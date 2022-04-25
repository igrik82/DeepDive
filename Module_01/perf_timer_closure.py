"""Decorator for testing speed execution"""
import time


def timed_it(quantity: int = 1) -> str:
    """Outer func for quantity tests"""

    def decorator(func: "function"):
        """Decorator"""

        def inner(*args, **kwargs):
            start = time.perf_counter()

            for _ in range(quantity):
                result = func(*args, **kwargs)

            elapsed = time.perf_counter() - start
            print(
                f"Function {func.__name__} executed in {elapsed:.6f}\
sec for {quantity} iterations."
            )

            return result

        return inner

    return decorator
