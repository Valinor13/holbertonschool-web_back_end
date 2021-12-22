#!/usr/bin/env python3
""" This module is a sandbox for mongodb """

import pymongo


def schools_by_topic(mongo_collection, topic):
    """ list schools be topic """
    school_list = []
    for record in mongo_collection.find():
        if topic in record.get(topics):
            school_list.append(record.get(name))
    return school_list
