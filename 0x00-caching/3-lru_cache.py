#!/usr/bin/env python3
""" This module will contain the LRUCache (least recently used) class """


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ The LRUCache object overwrites items at the end of the chain """

    def __init__(self):
        super().__init__()
        self.counter = 0
        self.lru_cache_order = {}

    def put(self, key, item):
        """ Assigns key/value pair to cache_data """

        if key and item:
            self.cache_data[key] = item
            self.lru_cache_order[self.counter] = key
            self.counter += 1

        if len(self.lru_cache_order) > self.MAX_ITEMS:
            for k, v in self.lru_cache_order.items():
                if v == key and k != (self.counter - 1):
                    del self.lru_cache_order[k]
                    break

        if len(self.cache_data) > self.MAX_ITEMS:
            ckey_list = []
            for ckey in self.lru_cache_order.keys():
                ckey_list.append(ckey)
            ckey_list.sort()
            lru_key = self.lru_cache_order[ckey_list[0]]
            del self.lru_cache_order[ckey_list[0]]
            print(f"DISCARD: {lru_key}")
            del self.cache_data[lru_key]

    def get(self, key):
        """ Returns dictionary item based on key value """

        if key and key in self.cache_data.keys():
            self.lru_cache_order[self.counter] = key
            self.counter += 1
            for k, v in self.lru_cache_order.items():
                if v == key and k != (self.counter - 1):
                    del self.lru_cache_order[k]
                    break
            return self.cache_data[key]
