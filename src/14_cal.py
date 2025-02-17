"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime


txt_cal = calendar.TextCalendar()
today = datetime.today()


def print_cal(month=today.month, year=today.year):
    print(txt_cal.formatmonth(int(year), int(month)))


if(len(sys.argv) > 3):
    print("Usage: cal.py <month> <year>")
    sys.exit(1)
elif(len(sys.argv) == 3):
    print_cal(sys.argv[1], sys.argv[2])
elif(len(sys.argv) == 2):
    print_cal(sys.argv[1])
else:
    print_cal()
