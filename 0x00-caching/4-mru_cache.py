#!/usr/bin/env python3
""" This module will contain the MRUCache (most recently used) class """


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ The MRUCache object overwrites items at the beginning of the chain """

    def __init__(self):
        super().__init__()
        self.counter = 0
        self.mru_cache_order = {}

    def put(self, key, item):
        """ Assigns key/value pair to cache_data """

        if key and item:
            self.cache_data[key] = item
            self.mru_cache_order[self.counter] = key
            self.counter += 1

        if len(self.mru_cache_order) > self.MAX_ITEMS:
            for k, v in self.mru_cache_order.items():
                if v == key and k != (self.counter - 1):
                    del self.mru_cache_order[k]
                    break

        if len(self.cache_data) > self.MAX_ITEMS:
            ckey_list = []
            for ckey in self.mru_cache_order.keys():
                ckey_list.append(ckey)
            ckey_list.sort(reverse=True)
            mru_key = self.mru_cache_order[ckey_list[1]]
            del self.mru_cache_order[ckey_list[1]]
            print(f"DISCARD: {mru_key}")
            del self.cache_data[mru_key]

    def get(self, key):
        """ Returns dictionary item based on key value """

        if key and key in self.cache_data.keys():
            self.mru_cache_order[self.counter] = key
            self.counter += 1
            for k, v in self.mru_cache_order.items():
                if v == key and k != (self.counter - 1):
                    del self.mru_cache_order[k]
                    break
            return self.cache_data[key]
