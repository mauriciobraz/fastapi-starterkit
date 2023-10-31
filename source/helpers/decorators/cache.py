import time
import functools

from typing import Any, Callable
from collections import Counter, OrderedDict


def memoize(func: Callable) -> Callable:
    """
    Memoization decorator to cache function results.

    Args:
        func (Callable): The function to memoize.

    Returns:
        Callable: The memoized function.

    Usage:
        ```python
        @memoize
        def expensive_function(arg1, arg2):
            # ... expensive computation ...
            return result

        # The result is cached
        expensive_function(1, 2)
        ```
    """
    cache: dict = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in cache:
            return cache[key]

        result = func(*args, **kwargs)
        cache[key] = result

        return result

    return wrapper


def cache_ttl(ttl: int):
    """
    Decorator to cache a function's return value for a specified time.

    Args:
        ttl (int): Time-to-live in seconds for the cache.

    Usage:
        ```python
        @cache_ttl(10)
        def fetch_data():
            # ... fetch data from a remote source ...
            return data

        # Cached for 10 seconds
        fetch_data()
        ```
    """

    def decorator(func: Callable) -> Callable:
        cache: dict = {}
        timestamp: dict = {}

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items()))

            if key in cache and (time.time() - timestamp[key]) < ttl:
                return cache[key]

            result = func(*args, **kwargs)
            cache[key] = result
            timestamp[key] = time.time()

            return result

        return wrapper

    return decorator


def lru_cache(maxsize: int):
    """
    Least Recently Used (LRU) cache decorator.

    Args:
        maxsize (int): Maximum size of the cache.

    Usage:
        ```python
        @lru_cache(100)
        def expensive_function(arg1, arg2):
            # ... expensive computation ...
            return result

        # Cached with a max size of 100
        expensive_function(1, 2)
        ```
    """

    def decorator(func: Callable) -> Callable:
        cache: OrderedDict = OrderedDict()

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items()))

            if key in cache:
                cache.move_to_end(key)
                return cache[key]

            result = func(*args, **kwargs)
            cache[key] = result

            if len(cache) > maxsize:
                cache.popitem(last=False)

            return result

        return wrapper

    return decorator


def lfu_cache(maxsize: int):
    """
    Least Frequently Used (LFU) cache decorator.

    Args:
        maxsize (int): Maximum size of the cache.

    Usage:
        ```python
        @lfu_cache(100)
        def expensive_function(arg1, arg2):
            # ... expensive computation ...
            return result

        # Cached with a max size of 100
        expensive_function(1, 2)
        ```
    """
    cache: dict = {}
    freq_counter: Counter = Counter()

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items()))

            if key in cache:
                freq_counter[key] += 1
                return cache[key]

            result = func(*args, **kwargs)

            if len(cache) >= maxsize:
                least_common = freq_counter.most_common()[:-2:-1][0][0]
                del cache[least_common]
                del freq_counter[least_common]

            cache[key] = result
            freq_counter[key] = 1

            return result

        return wrapper

    return decorator
