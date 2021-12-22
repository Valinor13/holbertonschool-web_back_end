#!/usr/bin/env python3
""" This module is a sandbox for mongodb """

import pymongo


def update_topics(mongo_collection, name, topics):
    """ update all records that match """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
