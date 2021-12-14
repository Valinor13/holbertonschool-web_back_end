#!/usr/bin/env python3
""" This is the redis python module """

import redis
import uuid
from typing import Union


class Cache:
    """ This class caches """

    def __init__(self):
        """ Cache constructor method, auto clears db instance """
        self._redis = redis.Redis()
        self._redis.flushdb(asynchronous=False)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ cache data with random key and return key """
        key_id = str(uuid.uuid4())
        self._redis.set(key_id, data)
        return key_id
