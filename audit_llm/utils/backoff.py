import time
from typing import Any, Callable, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def backoff(delay: int = 2, retries: int = 3) -> Callable[[F], F]:
    """
    Decorator to retry a function with exponential backoff.

    Parameters
    ----------
    delay : int, optional
        Initial delay in seconds before retrying (default is 2).
    retries : int, optional
        Number of retry attempts (default is 3).

    Returns
    -------
    Callable
        Decorated function with backoff logic.
    """

    def decorator(func: F) -> F:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_retry = 0
            current_delay = delay
            while current_retry < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    current_retry += 1
                    if current_retry >= retries:
                        raise e
                    print(
                        f"Failed to execute function '{func.__name__}'."
                        f" Retrying in {current_delay} seconds..."
                    )
                    time.sleep(current_delay)
                    current_delay *= 2

        return wrapper  # type: ignore

    return decorator
