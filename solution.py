import subprocess
from datetime import datetime, timedelta
from tabulate import tabulate


# Get list of date objects from cleaned inputs
def getDatefromCleanedInputs(dateTimeList):
    dateList = []
    for dateTimeObj in dateTimeList:
        dateList.append(datetime.strptime(
            dateTimeObj, '%Y-%m-%d %H:%M:%S').date())
    # sort and remove duplicates
    dateList = sorted(set(dateList))
    return dateList

# Calculates date range and corresponding login counts
def calculateLoginSummary(dateList):
    curDate = dateList[0]
    loginObj = Login(curDate, curDate, 1)
    consecutiveDayCountList = []

    for dateObj in dateList[1:dateList.__len__()]:
        if dateObj == loginObj.endDate + timedelta(1):
            loginObj.loginCount += 1
            loginObj.endDate = dateObj
        else:
            consecutiveDayCountList.append(loginObj)
            loginObj = Login(dateObj, dateObj, 1)
    consecutiveDayCountList.append(loginObj)
    return consecutiveDayCountList

# prints summary of date ranges and counts in decreasing order of counts
def printLoginSummaryAsTable(consecutiveDayCountList):
    # sort 'consecutiveDayCountList' in decreasing order of loginCount
    consecutiveDayCountList.sort(key=lambda x: x.loginCount, reverse=True)
    # print login activity in table format
    headers = ["START", "END", "LENGTH"]

    print(tabulate(consecutiveDayCountList, headers, tablefmt="github"))

# class to store login summary-start date, end date, login count
class Login:
    def __init__(self, startDate, endDate, loginCount):
        self.startDate = startDate
        self.endDate = endDate
        self.loginCount = loginCount

    def __iter__(self):
        for each in self.__dict__.values():
            yield each

    def __eq__(self, other):
        return (self.startDate == other.startDate and
                self.endDate == other.endDate and
                self.loginCount == other.loginCount)


# read date from seed.py to clean it
loginData = subprocess.run(
    ['python', "seed.py"], capture_output=True, text=True)
dateTimeList = loginData.stdout.replace("[", "").replace("]", "").strip().replace(
    "'", "").replace(", ", ",").split(",")


dateList = getDatefromCleanedInputs(dateTimeList)

consecutiveDayCountList = calculateLoginSummary(dateList)

printLoginSummaryAsTable(consecutiveDayCountList)
