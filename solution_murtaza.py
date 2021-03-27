from seed import res
from datetime import datetime

# Converting list of string dates to datetime objects
date_list = [datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S') for date_str in res]

# Sorting the list in ascending order
date_list.sort()

# result will be a list of tuples: (start, end, length)
result = []
f = []

# Initializing variables
start = date_list[0]
persistent_iterator = 0
counter = 0
end = date_list[0]

for date in date_list[1:]:
    # if two days are consecutive, increment counter and update end date of the series
    if (date - date_list[persistent_iterator]).days == 1:
        persistent_iterator += 1
        counter += 1
        end = date_list[persistent_iterator]
    # Add the start date, end date and length of the series in the result list and result counters
    else:
        result.append((start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d'), counter))
        start = date
        end = date
        persistent_iterator += 1
        counter = 0

for ind, date in enumerate(date_list):
    if ind == 0:
        continue

    # if two days are consecutive, increment counter and update end date of the series
    if (date - date_list[ind - 1]).days == 1:
        counter += 1
        end = date_list[ind - 1]
    # Add the start date, end date and length of the series in the result list and result counters
    else:
        result.append((start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d'), counter))
        start = date
        end = date
        counter = 0


def length_of_series(x):
    return x[2]


# Sorting result in descending order
result = sorted(result, key=length_of_series, reverse=True)

print('|  START   |    END   | LENGTH |')
print('|----------|----------|--------|')

for record in result:
    print("|{}|{}|   {}    |".format(record[0], record[1], record[2]))

