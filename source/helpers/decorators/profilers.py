from time import time
from typing import Any, Callable, Dict

from loguru import logger
from psutil import Process, cpu_percent


def profile(func: Callable) -> Callable:
    """
    Profile a function by measuring execution time, memory usage, and CPU usage, then log the results.

    Args:
        func (Callable): The function to profile.

    Returns:
        Callable: A wrapped version of the original function with profiling.

    Usage:
        ```python
        from helpers.decorators.measures import profile

        @profile
        def my_function():
            pass
        ```
    """

    def wrapper(*args: Any, **kwargs: dict[str, Any]) -> Any:
        process = Process()

        start_time = time()
        start_cpu = cpu_percent()
        start_memory = process.memory_info().rss / (1024 * 1024)

        result = func(*args, **kwargs)

        end_time = time()
        end_cpu = cpu_percent()
        end_memory = process.memory_info().rss / (1024 * 1024)

        cpu_used = end_cpu - start_cpu
        exec_time = end_time - start_time
        mem_used = end_memory - start_memory

        fn_name = f"{func.__qualname__}/{len(args) + len(kwargs)}"

        logger.debug(
            f"{fn_name} took {exec_time:.6f} seconds to execute, used {mem_used:.2f} MB of memory, and consumed {cpu_used:.2f}% CPU."
        )

        return result

    return wrapper


# Specific Profilers


def memory_profiler(func: Callable) -> Callable:
    """
    Profiles the memory used by a function and logs it.

    Usage:
        ```python
        from helpers.decorators.measures import memory_profiler

        @memory_profiler
        def my_function():
            pass
        ```
    """

    def wrapper(*args: Any, **kwargs: Dict[str, Any]) -> Any:
        process = Process()

        start_memory = process.memory_info().rss
        result = func(*args, **kwargs)
        end_memory = process.memory_info().rss

        fn_name = f"{func.__qualname__}/{len(args) + len(kwargs)}"
        logger.debug(
            f"{fn_name} used {end_memory - start_memory} bytes of memory.",
        )

        return result

    return wrapper


def cpu_profiler(func: Callable) -> Callable:
    """
    Profiles the CPU usage of a function and logs it.

    Usage:
        ```python
        from helpers.decorators.measures import cpu_profiler

        @cpu_profiler
        def my_function():
            pass
        ```
    """

    def wrapper(*args: Any, **kwargs: Dict[str, Any]) -> Any:
        start_cpu = cpu_percent()
        result = func(*args, **kwargs)
        end_cpu = cpu_percent()

        fn_name = f"{func.__qualname__}/{len(args) + len(kwargs)}"
        logger.debug(
            f"{fn_name} used {end_cpu - start_cpu}% of CPU.",
        )

        return result

    return wrapper
