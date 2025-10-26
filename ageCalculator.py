from datetime import date
from datetime import datetime
import calendar

def is_leap_year(year):
    # Leap year rules:
    # 1. Divisible by 4
    # 2. Not divisible by 100, unless also divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

today = date.today()

# Introduction
print("             WELCOME TO AGE CALCULATOR")
print("--------------------------------------------------")
input("             Enter any key to start...")
print("--------------------------------------------------")

# Variables for the input of the user
#Checks whether the user inputs valid variables

# Enter birthyear
year = int(input("Enter your Birth Year        : "))
if year < 0 or year > today.year: 
    print("Invalid year.")
    exit()

# Enter birthmonth
string_month = input(   "Enter your Birth Month       : ").strip().capitalize()
month = datetime.strptime(string_month, "%B").month
if month < 1 or month > 12 or (year == today.year and month > today.month):
    print("Invalid month.")
    exit()

# Checks the limited number of days in a month
days_in_month = calendar.monthrange(year, month)[1]

# Enter birthday
day = int(input(     "Enter the day you were born  : "))
if day < 1 or day > days_in_month:
    print("Invalid number of days.")
    exit()
print("--------------------------------------------------")
birthdate = date(year, month, day)

# Displays birthdate
print("               Your birthdate ")
print("--------------------------------------------------")
print(f"Year  : {birthdate.year} " \
f"    \nMonth : {birthdate.month} " \
f"    \nDay   : {birthdate.day}")
print("--------------------------------------------------")
# Variables for the result
yearResult = today.year - birthdate.year
monthResult = today.month - birthdate.month
dayResult = today.day - birthdate.day

# Print the current date
print("               Current Year")
print("--------------------------------------------------")
print(f"Year  : {birthdate.year} " \
f"    \nMonth : {birthdate.month} " \
f"    \nDay   : {birthdate.day}")
print("--------------------------------------------------")
# Validates day
if dayResult < 0:
    month -= 1
    prev_month_days = calendar.monthrange(today.year, today.month - 1 or 12)[1]
    dayResult += prev_month_days

# Validates month
if monthResult < 0:
    yearResult -= 1
    monthResult += 12

# Checks if there is negative ages
if yearResult <= 0 and monthResult <= 0 and dayResult <= 0:
    print("Invalid age result.") 
    exit()
else:
    # Prints the final output
    print("       You are currenly living with the age")
    print("--------------------------------------------------")
    print(f"Year(s)  : {yearResult} "
     f"\nMonth(s) : {monthResult} "
     f"\nDay(s)   : {dayResult}")
