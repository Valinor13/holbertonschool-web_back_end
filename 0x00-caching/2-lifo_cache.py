#!/usr/bin/env python3
""" This module will contain the LIFOCache (last in first out) class """


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ The LIFOCache object overwrites items at the end of the chain """

    def __init__(self):
        super().__init__()
        self.lifo_cache_order = []

    def put(self, key, item):
        """ Assigns key/value pair to cache_data """

        if key and item:
            self.cache_data[key] = item
            self.lifo_cache_order.append(key)

        if len(self.cache_data) > self.MAX_ITEMS:
            lifo_key = self.lifo_cache_order.pop(-2)
            print(f"DISCARD: {lifo_key}")
            del self.cache_data[lifo_key]

    def get(self, key):
        """ Returns dictionary item based on key value """

        if key and key in self.cache_data.keys():
            return self.cache_data[key]
