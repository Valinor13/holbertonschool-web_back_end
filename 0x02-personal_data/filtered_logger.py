#!/usr/bin/env python3
""" A module that contains a filter for ; delimited strings """


import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """ Filter Datum filters the string for given fields """
    messages = message.split(separator)
    for field in fields:
        for i in range(0, len(messages)):
            messages[i] = re.sub(field + '=[^ ]*' + '$',
                                 field + '=' + redaction,
                                 messages[i])
    return separator.join(messages)
