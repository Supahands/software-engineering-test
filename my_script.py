from datetime import datetime

import seed

def get_key_length(obj):
    return obj.score

class DateScore:
    score = 0

    def __init__(self, score, startDate, endDate):
        self.score = score
        self.startDate = startDate
        self.endDate = endDate


result = []
seedDates = seed
dates = seedDates.res

dates.sort()



for i in range(len(dates)):
    dates[i] = datetime.strptime(dates[i], '%Y-%m-%d %H:%M:%S')

flag = 0
start = 0
end = 0

while flag != 1:

    if start <= len(dates):
        if end + 1 < len(dates):
            if dates[end + 1].day - dates[end].day <= 1:
                end += 1
            else:
                dateScore = DateScore
                dateScore.startDate = dates[start]
                dateScore.endDate = dates[end]
                if dateScore.startDate.month == dateScore.endDate.month:
                    dateScore.score = dates[end].day - dates[start].day + 1
                elif dateScore.startDate.month < dateScore.endDate.month:
                    dateScore.score = dates[end].day - dates[start].day + 1
                    if dateScore.endDate.month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
                        dateScore.score += 30
                    elif dateScore.endDate.month == 4 or 6 or 9 or 11:
                        dateScore.score += 31
                    elif dateScore.endDate.month == 2:
                        dateScore.score += 28
                start = end + 1
                end = start
                result.append(DateScore(dateScore.score, dateScore.startDate, dateScore.endDate))
        else:
            dateScore = DateScore
            dateScore.startDate = dates[start]
            dateScore.endDate = dates[end]
            if dateScore.startDate.month == dateScore.endDate.month:
                dateScore.score = dates[end].day - dates[start].day + 1
            elif dateScore.startDate.month < dateScore.endDate.month:
                dateScore.score = dates[end].day - dates[start].day + 1
                if dateScore.endDate.month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
                    dateScore.score += 30
                elif dateScore.endDate.month == 4 or 6 or 9 or 11:
                    dateScore.score += 31
                elif dateScore.endDate.month == 2:
                    dateScore.score += 28
                result.append(DateScore(dateScore.score, dateScore.startDate, dateScore.endDate))

            break
    else:
        flag = 1



result.sort(key=get_key_length, reverse=True)
print("| START | END | LENGTH ||------------|------------|--------|", end= "")
for obj in result:
    print("|", obj.startDate.date(), "|", obj.endDate.date(), "|", obj.score, "|", end="")
