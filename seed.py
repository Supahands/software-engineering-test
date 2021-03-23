from datetime import datetime
from datetime import timedelta
from random import randint
import pandas as pd
import numpy as np

# start = datetime.now()
# end = start + timedelta(days=60)

# for _ in range(10):
#  if _ % 2 == 0:
#   value = randint(1, 12)
#  else:
#   value = randint(24, 48)
#
# step = timedelta(hours=value)

result = ['2021-03-13 15:13:05', '2021-03-13 23:13:05', '2021-03-16 15:13:05', '2021-03-16 23:13:05', '2021-03-17 07:13:05', '2021-03-17 15:13:05', '2021-03-17 23:13:05', '2021-03-18 07:13:05', '2021-03-18 15:13:05']

# result = []

# while start < end:
#     result.append(start.strftime('%Y-%m-%d %H:%M:%S'))
#     high_rand = randint(24, 72)
#     low_rand = randint(5, 18)
#     value = randint(low_rand, high_rand)
#     step = timedelta(hours=value)
#     start += step


def consecutive_date_list(input_date_list):
    date_list = [datetime.strptime(d, "%Y-%m-%d %H:%M:%S") for d in input_date_list]
    date_list_1 = [datetime.strftime(d, "%Y-%m-%d") for d in date_list]
    ordinals = [datetime.strptime(d, "%Y-%m-%d").toordinal() for d in date_list_1]

    ans = 0
    count = 0


    arr = np.array(ordinals)

    v = []
    ans_arr = []

    for i in range(1, len(arr)):

        if (arr[i] != arr[i-1]):
            v.append(arr[i])


    ans_arr.append(v[0])
    count += 1

    for i in range (1,len(v)):

        if (i>0 and v[i] == v[i-1]+1):
            ans_arr.append(v[i])
            count += 1

        else:
            count = 1

        ans = max(ans, count)

    return ans, ans_arr

length, result_list=consecutive_date_list(result)



start_date = result_list[0]        # getting the starting date
start_date = datetime.fromordinal(start_date)

end_date = result_list[-1]        # getting the ending date
end_date = datetime.fromordinal(end_date)


data = {'Start': start_date, 'End': end_date, 'Length': length}
df = pd.DataFrame(data=data, index=[0])
print(df)


