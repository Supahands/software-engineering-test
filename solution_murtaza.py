from seed import res
from datetime import datetime


def length_of_series(x):
    return x[2]


def derive_streaks(datelist):

    # result will be a list of tuples: (start, end, length)
    result_list = []

    # Initializing variables
    start, end, counter = datelist[0], datelist[0], 0

    for ind, date in enumerate(datelist):
        if ind == 0:
            continue

        # if two days are consecutive, increment counter and update end date of the series
        if (date - datelist[ind - 1]).days == 1:
            counter += 1
            end = datelist[ind]
        # Add the start date, end date and length of the series in the result list and result counters
        else:
            result_list.append((start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d'), counter))
            start = date
            end = date
            counter = 0

    return result_list


def format_and_display_output(result):
    print('|  START   |    END   | LENGTH |')
    print('|----------|----------|--------|')

    for record in result:
        print("|{}|{}|   {}    |".format(record[0], record[1], record[2]))


def main(date_str):
    # Converting list of string dates to datetime objects
    # Using set to get unique values
    date_list = list(set([datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S').date() for date_str in res]))

    # Sorting in ascending order
    date_list.sort()

    result = derive_streaks(date_list)

    # Sorting result in descending order
    result = sorted(result, key=length_of_series, reverse=True)

    # Displaying output
    format_and_display_output(result)
