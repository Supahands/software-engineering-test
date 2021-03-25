import seed
from datetime import datetime, date

result= [datetime.strptime(i, "%Y-%m-%d %H:%M:%S") for i in seed.result]
dates = list(set([datetime.date(i) for i in result]))
count = 0
start = None
end = None
for i, d in enumerate(dates):
 if i != 0:
    if (dates[i] - dates[i - 1]).days == 1:
        count += 1
        end = dates[i]
        if start == None:
         start = dates[i - 1]
    else:
        if count != 0:
            print("START END LENGTH")
            print("{} {} {}".format(start, end, count))
            count = 0
            start = None
            end = None
        

if count != 0:
    print("START END LENGTH")
    print("{} {} {}".format(start, end, count))

