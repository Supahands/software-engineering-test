import subprocess
from tabulate import tabulate
from datetime import datetime


def sortTimeStamps(timestampList):
    """Turn the timestamp list string into a sorted list."""
    # removes the non-date chars of the output string
    tsl = timestampList.replace("['", "")
    tsl = tsl.replace("']", "")
    tsl = tsl.strip()
    tsl = tsl.split("', '")
    dates = []
    # convert the seed output to datetime objects
    for date in tsl:
        dates.append(datetime.strptime(date, "%Y-%m-%d %H:%M:%S"))
    # sorts the dates in ascending order
    dates.sort()
    return dates


def getConsecDates(dates):
    """Find the consecutive dates and places them in a 2d list."""
    dateTable = []
    i = 0
    while i < len(dates):
        row = ["startDate", "endDate", "numDays"]
        date1 = dates[i]
        row[0] = date1.date()
        row[1] = date1.date()
        row[2] = 1
        n = 1   # num of days counter
        if i + 1 == len(dates):
            dateTable.append(row)
            break
        else:
            for d in dates[i+1:]:
                # print(i, 'end', len(dates))
                numDays = (d.date() - date1.date()).days

                # condition for when the consecutive chain stops
                if numDays > n:
                    dateTable.append(row)
                    i = i + 1
                    break
                # condition for if the next date is the same as the previous date
                elif numDays == 0:
                    row[1] = d.date()
                    row[2] = n + 1
                    i = i + 1
                # condition for if the next date is consecutive
                else:
                    row[1] = d.date()
                    row[2] = n + 1
                    i = i + 1
                    # ensures the day counter wont increment for the same day
                    if((d.date() - dates[i-1].date()).days > 0):
                        row[2] = n + 1
                        n = n + 1
                    else:
                        row[2] = n
    # sorts the dates by LENGTH
    return sorted(dateTable, key=lambda x: x[2], reverse=True)


# puts the date list in a table
def datesToTable(dates):
    """Turn a 2d list containing the consecutive dates into a table."""
    return tabulate(dates, headers=["START", "END", "LENGTH"])


def main():
    """Show the solution."""
    output = subprocess.run("py seed.py", capture_output=True, text=True).stdout
    dates = sortTimeStamps(output)
    toTable = getConsecDates(dates)
    print(datesToTable(toTable))

main()
