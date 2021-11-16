#!/usr/bin/env python3
""" A module that contains a filter for ; delimited strings """


import logging
import re


def filter_datum(fields, redaction, message, separator) -> str:
    """ Filter Datum filters the string for given fields """
    msgs = message.split(separator)
    for field in fields:
        for i in range(len(msgs)):
            msgs[i] = re.sub(f'{field}=.*', f'{field}={redaction}', msgs[i])
    return separator.join(msgs)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Formats the record """
        record.msg = filter_datum(self.fields,
                                  self.REDACTION,
                                  record.msg,
                                  self.SEPARATOR)
        return super().format(record)
