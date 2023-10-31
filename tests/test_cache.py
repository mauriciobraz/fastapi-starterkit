import time
from functools import lru_cache

from source.helpers.decorators.cache import cache_ttl, lfu_cache, memoize


def expensive_computation(a, b):
    if a == 0:
        return b

    return expensive_computation(a - 1, b + 1)


def fetch_data():
    return 42


def test_memoize():
    memoized_function = memoize(expensive_computation)

    assert memoized_function(1, 2) == 3

    assert memoized_function(1, 2) == 3


def test_cache_ttl():
    ttl_cached_function = cache_ttl(2)(fetch_data)

    assert ttl_cached_function() == 42

    assert ttl_cached_function() == 42

    time.sleep(1)
    assert ttl_cached_function() == 42


def test_lru_cache():
    lru_cached_function = lru_cache(2)(expensive_computation)

    assert lru_cached_function(1, 2) == 3
    assert lru_cached_function(3, 4) == 7

    assert lru_cached_function(5, 6) == 11
    assert lru_cached_function(1, 2) == 3


def test_lfu_cache():
    lfu_cached_function = lfu_cache(2)(expensive_computation)

    assert lfu_cached_function(1, 2) == 3
    assert lfu_cached_function(3, 4) == 7

    assert lfu_cached_function(1, 2) == 3

    assert lfu_cached_function(5, 6) == 11
    assert lfu_cached_function(3, 4) == 7
