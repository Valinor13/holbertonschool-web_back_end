#!/usr/bin/env python3
""" This module will contain the FIFOCache (first in first out) class """


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ The FIFOCache object overwrites items in sequence of arrival """

    def __init__(self):
        super().__init__()
        self.fifo_cache_order = []

    def put(self, key, item):
        """ Assigns key/value pair to cache_data """

        if key and item:
            self.cache_data[key] = item
            self.fifo_cache_order.append(key)

        if len(self.cache_data) > self.MAX_ITEMS:
            fifo_key = self.fifo_cache_order.pop(0)
            print(f"DISCARD: {fifo_key}")
            del self.cache_data[fifo_key]

    def get(self, key):
        """ Returns dictionary item based on key value """

        if key and key in self.cache_data.keys():
            return self.cache_data[key]
