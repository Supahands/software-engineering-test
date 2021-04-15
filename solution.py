import subprocess
import datetime


def process(l):
    """
    Aggregate dates by consecutive logins.

    >>> l = ['2021-03-13 15:13:05', '2021-03-13 23:13:05', '2021-03-16 15:13:05',
    ...      '2021-03-16 23:13:05', '2021-03-17 07:13:05', '2021-03-17 15:13:05',
    ...      '2021-03-17 23:13:05', '2021-03-18 07:13:05', '2021-03-18 15:13:05']
    >>> process(l)
    [(datetime.date(2021, 3, 13), datetime.date(2021, 3, 13)), (datetime.date(2021, 3, 16), datetime.date(2021, 3, 18))]
    """
    d = datetime.timedelta(days=1)
    # convert input string into sorted dates without duplicates
    l = sorted({datetime.datetime.fromisoformat(i).date() for i in l})

    # move each parts into each group of (start, end) if adjacent day
    i = l.pop(0)
    acc = [(i, i)]
    for i in l:
        if acc[-1][1] + d == i:  # if subsequent day
            acc[-1] = (acc[-1][0], i)  # change end day
        else:
            acc.append((i, i))
    return acc


if __name__ == '__main__':
    # run this part when file is invoked directly
    p = subprocess.run(["python", "seed.py"], capture_output=True)
    acc = process(eval(p.stdout))

    # print the table
    print("| START      | END        | LENGTH |")
    print("|------------|------------|--------|")
    for x, y in reversed(acc):
        days = (y - x).days + 1
        print(f"| {x.isoformat():>8} | {y.isoformat():>8} | {days:>6} |")
