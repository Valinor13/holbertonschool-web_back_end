#!/usr/bin/env python3
""" This module is a sandbox for mongodb """

import pymongo


def schools_by_topic(mongo_collection, topic):
    """ list schools be topic """
    return mongo_collection.find({"topics": topic})
