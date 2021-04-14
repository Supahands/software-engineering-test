from seed import res
from datetime import datetime


def length_of_series(x):
    return x[2]


def convert_string_to_date_lst(lst):
    # Using set to get unique values
    date_list = list(set([datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S').date() for date_str in lst]))

    # Sorting in ascending order
    date_list.sort()

    return date_list


def derive_streaks(datelist):

    if len(datelist) == 0:
        return []

    # result will be a list of tuples: (start, end, length)
    result_list = []

    # Initializing variables
    start, end, counter = datelist[0], datelist[0], 1

    for ind, date in enumerate(datelist):
        if ind != 0:
            # if two days are consecutive, increment counter and update end date of the series
            if (date - datelist[ind - 1]).days == 1:
                counter += 1
                end = datelist[ind]
            # Add the start date, end date and length of the series in the result list and result counters
            else:
                result_list.append((start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d'), counter))
                start = date
                end = date
                counter = 1
    result_list.append((start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d'), counter))

    return result_list


def format_and_display_output(result):
    print('|  START   |    END   | LENGTH |')
    print('|----------|----------|--------|')

    for record in result:
        print("|{}|{}|   {}    |".format(record[0], record[1], record[2]))


def main(date_str):

    if len(date_str) == 0:
        print("The given list of dates is empty")

    else:
        # Converting list of string dates to datetime objects
        date_list = convert_string_to_date_lst(date_str)

        result = derive_streaks(date_list)

        # Sorting result in descending order
        result = sorted(result, key=length_of_series, reverse=True)

        # Displaying output
        format_and_display_output(result)


main(res)
