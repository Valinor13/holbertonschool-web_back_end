#!/usr/bin/env python3
""" This module will contain the index_range helper function """


def index_range(page, page_size):
    """ Index Range: Returns a tuple with page results """

    return (((page - 1) * page_size), (page * page_size))
