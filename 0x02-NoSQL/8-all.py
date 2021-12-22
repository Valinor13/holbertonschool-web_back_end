#!/usr/bin/env python3
""" This module is a sandbox for mongodb """

import pymongo


def list_all(mongo_collection):
    """ list all documents in collection """
    record_list = []
    for record in mongo_collection.find({}):
        record_list.append(record)
    return record_list
