#!/usr/bin/env python

'''longest_streak.py

Command line usage:
Data from a file:
    python longest_streak.py [input filename]
Data from a pipe:
    python seed.py | python longest_streak.py -
'''

import sys
from collections import namedtuple
from datetime import datetime, timedelta
from typing import Iterable


DATEFORMAT = '%Y-%m-%d %H:%M:%S'
Streak = namedtuple('Streak', ['start', 'end', 'length'])


def longest_streak():
    '''Runs the command line interface for longest_streak.py'''
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit()
    elif sys.argv[1] == '-':
        text = sys.stdin.read()
    else:
        with open(sys.argv[1], 'r') as inputfile:
            text = inputfile.read()
    dates = convert_list(text)
    streak = find_streak(dates)
    print(format_streak(streak))


def convert_list(text: str) -> Iterable[datetime]:
    '''Converts the text output of seed.py into a list of date objects'''
    result = []
    text = text.strip('[]\n\t ')
    for date_str in text.split(','):
        date_str = date_str.strip('\'\" ')
        date = datetime.strptime(date_str, DATEFORMAT).date()
        if date not in result:
            result.append(date)
    return result


def find_streak(dates: Iterable[datetime]) -> Streak:
    '''
    Finds the longest daily streak

    Outputs as a named tuple in the format: (start, end, length)
    '''
    longest = None
    current = None
    for date in sorted(dates):
        if current is None or date - current.end > timedelta(days=1):
            current = Streak(date, date, 1)
            if longest is None:
                longest = current
            continue
        length = date - current.start
        current = Streak(current.start, date, length.days)
        if longest.length < current.length:
            longest = current
    return longest


def format_streak(value: Streak):
    '''
    Formats Streak named tuple as described in the README.md

    e.g.:
    | START      | END        | LENGTH |
    |------------|------------|--------|
    | 2021-03-16 | 2021-03-18 |      3 |
    '''
    columns = [
        ('START', value.start.strftime('%Y-%m-%d'), 'ljust'),
        ('END', value.end.strftime('%Y-%m-%d'), 'ljust'),
        ('LENGTH', str(value.length), 'rjust'),
    ]
    formatted_columns = []
    for header, text, func in columns:
        width = max(len(header), len(text))
        header = header.ljust(width).center(width + 2)
        sep = '-' * (width + 2)
        method = getattr(text, func)
        text = method(width).center(width + 2)
        formatted_columns.append((header, sep, text,))
    rows = []
    for i in range(3):
        items = [x[i] for x in formatted_columns]
        row = '|'.join(items)
        rows.append(''.join(['|', row, '|']))
    return '\n'.join(rows)


if __name__ == '__main__':
    longest_streak()
