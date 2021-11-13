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
        csv_rows = []
        pagi_list = []
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert (page, page_size) > (0, 0)
        pagi = index_range(page, page_size)
        with open(self.DATA_FILE, 'r') as f:
            csvr = csv.reader(f)
            for row in csvr:
                csv_rows.append(row)
            if pagi[0] > len(csv_rows) / page_size:
                return []
            header = csv_rows.pop(0)
            for x in range(pagi[0], pagi[1]):
                pagi_list.append(csv_rows[x])
        return pagi_list
