#!/usr/bin/env python3
""" This module will contain the BasicCache class """


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ The BasicCache object stores and returns a basic dictionary object """

    def put(self, key, item):
        """ Assigns key/value pair to cache_data """

        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Returns dictionary item based on key value """

        if key and key in self.cache_data.keys():
            return self.cache_data[key]
