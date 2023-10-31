from threading import Lock
from typing import Any, Callable


def singleton(cls: Callable) -> Callable:
    """Automatically create a singleton instance of a class.

    Args:
        cls (Callable): The class to create a singleton instance of.

    Returns:
        Callable: A wrapped version of the original class with a singleton instance.

    Usage:
        ```python
        from helpers.decorators.singleton import singleton

        @singleton
        class MyClass:
            pass
        ```
    """
    instances: dict[Callable, Any] = {}

    def wrapper(*args: Any, **kwargs: dict[str, Any]) -> Any:
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)

        return instances[cls]

    return wrapper


def thread_safe_singleton(cls: Callable) -> Callable:
    """Automatically create a thread-safe singleton instance of a class.

    Args:
        cls (Callable): The class to create a thread-safe singleton instance of.

    Returns:
        Callable: A wrapped version of the original class with a thread-safe singleton instance.

    Usage:
        ```python
        from helpers.decorators.singleton import thread_safe_singleton

        @thread_safe_singleton
        class MyClass:
            pass
        ```
    """
    lock: Lock = Lock()
    instances: dict[Callable, Any] = {}

    def wrapper(*args: Any, **kwargs: dict[str, Any]) -> Any:
        with lock:
            if cls not in instances:
                instances[cls] = cls(*args, **kwargs)

        return instances[cls]

    return wrapper
