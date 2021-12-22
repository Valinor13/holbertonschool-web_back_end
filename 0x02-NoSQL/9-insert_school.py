#!/usr/bin/env python3
""" This module is a sandbox for mongodb """

import pymongo


def insert_school(mongo_collection, **kwargs):
    """ insert new record into collection """
    new_doc = {}
    for k, v in kwargs.items():
        new_doc[k] = v
    return mongo_collection.insert_one(new_doc)
