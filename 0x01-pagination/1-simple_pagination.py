#!/usr/bin/env python3
""" This module will contain the Pagination program """


import csv
import math
from typing import List


def index_range(page, page_size):
    """ Index Range: Returns a tuple with page results """

    return (((page - 1) * page_size), (page * page_size))


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Get Page: returns list of results based on the input page num """
        pagi_list = []
        assert (isinstance(page, int),
                isinstance(page_size, int),
                page, page_size) >= (True, True, 1, 1)
        pagi = index_range(page, page_size)
        ds = self.dataset()
        if pagi[0] > len(ds) / page_size:
            return []
        for x in range(pagi[0], pagi[1]):
            pagi_list.append(ds[x])
        return pagi_list
