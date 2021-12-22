#!/usr/bin/env python3
""" This module is a sandbox for mongodb """

import pymongo


def insert_school(mongo_collection, **kwargs):
    """ insert new record into collection """
    return mongo_collection.insert_one(kwargs).inserted_id
