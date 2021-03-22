import seed
from datetime import datetime, date

login_ts = seed.result

timestamps = [datetime.strptime(d, "%Y-%m-%d %H:%M:%S") for d in login_ts]
dates = list(set([datetime.date(d) for d in timestamps]))
dates.sort()

streak = []
count = 0
start, end = None, None

for i, d in enumerate(dates):
    if i == 0:
        streak.append(d)
        continue

    if (dates[i] - dates[i - 1]).days == 1:
        streak.append(d)
    else:
        if len(streak) > count:
            start = streak[0]
            end = streak[len(streak) - 1]
        count = max(len(streak), count) 
        streak = []
        streak.append(d)

print("START END LENGTH")
print("{} {} {}".format(start, end, count))
