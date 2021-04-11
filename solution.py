from datetime import date, datetime, timedelta
import unittest
import sys


import seed


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

def consecCounter(date_list):
    result = [] # 2D list to store both end 

    start = date_list[0] # Start set to first date
    consec_day = 1
    for prev_end,curr_end in zip(date_list,date_list[1:]): # Uses zip to allow link to previous end
        new = [] #New list used to create 2D list (will be appended into list)
        if (curr_end - start).days == consec_day: #If there the next day is still consecutive
            if(curr_end == prev_end): # Incase of duplicate dates
                continue
            consec_day = consec_day + 1 # Add to consec days
           
        elif(curr_end-start).days == 0: # Condition for dates that have less than one consec day
            consec_day = 1 # To ensure that even though there are no consecutive days, it will always be counted as 1
            new.append(start.strftime('%Y-%m-%d'))  # Append to internal list while also formatting date
            new.append(start.strftime('%Y-%m-%d'))
            new.append(consec_day) 
            result.append(new) # Append internal list to main list
            start = curr_end # Set start to the next date pair

        else: # Next date no longer consecutive  
            new.append(start.strftime('%Y-%m-%d'))
            new.append(prev_end.strftime('%Y-%m-%d')) # Append previous end asto not append the next start aswell
            new.append(consec_day)
            result.append(new) 
            start = curr_end
            consec_day = 1

    result = sorted(result, key=lambda x: x[2], reverse=True) # Sorting according to the length
    return result

    

if __name__ == "__main__":
    
    # test_date_conversion()
    print("================================================================================================================================================")
    temp_list = seed.res # Retrieve array of dates from seed.py
    temp_list = sorted(temp_list) # Sort dates before conversion
    date_list = toDates(temp_list) # Convert all dates to datetime format
    result = consecCounter(date_list) # Count all consecutive days
    print(date_list)
    print(result)
    
    
    
    print("START\t\tEND\t\tLENGTH") # Printing table header
    print("--------------------------------------------")
    # Printing 2D array with two for loops
    for inner_list in result:
        for result in inner_list:
            print(result , end = "\t") # 4 line space between the dates and the length
        print("\n") # Break line for next result
    
    
    
    

