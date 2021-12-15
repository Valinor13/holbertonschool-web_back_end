#!/usr/bin/env python3
""" This is the redis python module """

import redis
import uuid
import functools
from typing import Union, Callable


def count_calls(method: Callable) -> Callable:
    """ counts the times Cache methods are called """
    key = method.__qualname__
    @functools.wraps(method)
    def count_wrapper(self, *args, **kwargs) -> int:
        """ the callable wrapper for count """
        self._redis.incr(key)
        return method
    return count_wrapper


class Cache:
    """ This class caches """

    def __init__(self):
        """ Cache constructor method, auto clears db instance """
        self._redis = redis.Redis()
        self._redis.flushdb(asynchronous=False)

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ cache data with random key and return key """
        key_id = str(uuid.uuid4())
        self._redis.set(key_id, data)
        return key_id

    def get(self, key: str, fn: Callable = None) -> Union[str, int]:
        """ retrieves data from cache based on key """
        try:
            data = self._redis.get(key)
            if data:
                if fn:
                    return fn(data)
                return data
        except KeyError:
            return '(nil)'


def get_str(key: str) -> str:
    """ converts data to str """
    return Cache.get(key, str)


def get_int(key: str) -> int:
    """ converts data to int """
    return Cache.get(key, int)
