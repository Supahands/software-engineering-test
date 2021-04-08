# from datetime import date, time,timedelta,datetime
# import datetime
from datetime import date, datetime, timedelta


from dateutil.relativedelta import relativedelta
from collections import Counter

import seed 

# Date in ISO 8601 format 
# E.g. YYYY-MM-DD HH:MM:SS
#steps to program
# 1. parse dates into datetime.date format
# 2. append each date to array
# 3. sort array 
# 4. Once sorted loop through and count consecutive days
# 5. Once a consecutive streak ends append it to new array
# 6. repeat step 4-6
# 7. Create tabular display for each new row in new array
# print(seed)




    



def toDates(temp_list):
    format_string = "%Y-%m-%d"
    date_list = []
    for i in range(len(temp_list)):
        replace = temp_list[i]
        replace = replace[:-9] #trimming string to get rid of time as it is not needed for output
        temp_list[i] = replace 

    for item in temp_list:
        
        current = datetime.strptime(item, format_string)

        date_list.append(current)

    return date_list


if __name__ == "__main__":
    print("================================================================================================================================================")
    temp_list = seed.res
    temp_list = sorted(temp_list)
    date_list = toDates(temp_list)
    
    
    
    result = [] # Dictionary to store results in 

    start = date_list[0]
    consec_day = 1
    temp_new = []
    for end in date_list[1:]:
        new = []
        if (end - start).days == consec_day: #If there the next day is still consecutive
            consec_day = consec_day + 1
        else: #Next date no longer consecutive
            new.append(start.strftime('%Y/%m/%d'))
            temp_end = end - timedelta(days=1)
            new.append(temp_end.strftime('%Y/%m/%d'))
            new.append(consec_day)
            result.append(new) 
            # result[start] = consec_day
            start = end
            consec_day = 1
    temp_new.append(start.strftime('%Y/%m/%d'))
    temp_new.append(consec_day)
    
    # result[start] = consec_day

    
    result = sorted(result, key=lambda x: x[2], reverse=True)
    # result = sorted(result)
    print("START\t\tEND\t\tLENGTH")
    print("--------------------------------------------")
    for inner_list in result:
        for result in inner_list:
            print(result , end = "\t")
        print("\n")
        
    # for i in sort_orders:
    #     print(i[0], i[1])


