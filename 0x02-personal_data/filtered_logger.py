#!/usr/bin/env python3
""" A module that contains a filter for ; delimited strings """


import logging
import re
from typing import List


PII_FIELDS = ('password', 'ip', 'ssn', 'phone', 'name')


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """ Filter Datum filters the string for given fields """
    msgs = message.split(separator)
    for field in fields:
        for i in range(len(msgs)):
            msgs[i] = re.sub(f'{field}=.*', f'{field}={redaction}', msgs[i])
    return separator.join(msgs)


def get_logger() -> logging.Logger:
    """ Gets a logRecord for class """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(RedactingFormatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Formats the record """
        record.msg = filter_datum(self.fields,
                                  self.REDACTION,
                                  record.msg,
                                  self.SEPARATOR)
        return super().format(record)
