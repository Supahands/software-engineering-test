from datetime import datetime, timedelta
from itertools import groupby
from operator import itemgetter
from subprocess import Popen, PIPE

def process_output_date(output_date):
    output_date = output_date.strip().strip("[]'")
    return datetime.strptime(output_date, '%Y-%m-%d %H:%M:%S').date()

def get_consecutive_date_ranges(dates):
    dates = sorted(dates)

    # Convert the dates to unique set of difference in days to the min date
    min_date = dates[0]
    days_diff = set([(date - min_date).days for date in dates])

    # Referring https://stackoverflow.com/a/2154437 to get consecutive ranges from a list of numbers
    date_ranges = []
    for k, g in groupby(enumerate(days_diff), lambda x:x[0]-x[1]):
        group = map(itemgetter(1), g)
        group = list(map(int,group))
        date_ranges.append((min_date + timedelta(days=group[0]), min_date + timedelta(days=group[-1]), len(group)))

    date_ranges.sort(key=lambda tup: tup[2], reverse=True)
    return date_ranges

def print_result(date_ranges):
    print('|%-12s|%-12s|%12s|' % ("START", "END", "LENGTH"))
    print('-' * 40)
    for range in date_ranges:
        print('|%-12s|%-12s|%12i|' % (range[0].strftime("%Y-%m-%d"), range[1].strftime("%Y-%m-%d"), range[2]))

if __name__ == '__main__':
    # Referring https://stackoverflow.com/a/6086063 to read printed output from other script
    proc = Popen(["python", "seed.py"], stdout=PIPE)
    output = proc.communicate()[0].decode("utf-8")

    dates = [process_output_date(output_date) for output_date in output.split(',')]

    date_ranges = get_consecutive_date_ranges(dates)

    print_result(date_ranges)