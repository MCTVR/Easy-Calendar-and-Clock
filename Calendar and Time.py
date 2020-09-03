#Import
import calendar
from datetime import datetime
from datetime import date

#Assign values
now = datetime.now()
d_now = date.today()
current_time = now.strftime("%H:%M")
today_date = d_now.strftime("%d/%b/%Y")
am_pm = now.strftime("%H")
dt = datetime.today()

#print a blank line
print(" ")

#print today's date
print("Today's date =", today_date)

#print Part of Day
if float(am_pm) < float(6):
    print("Part of Day = Early Morning")
if float(am_pm) < float(12) and float(am_pm) >= float(6):
    print("Part of Day = Morning")
if float(am_pm) >= float(18) and float(am_pm) < float(24):
    print("Part of Day = Night")
if float(am_pm) > float(12) and float(am_pm) < float(18):
    print("Part of Day = Afternoon")
if float(am_pm) == float(12):
    print("Part of Day = Noon")

#print Current Time
print("Current Time =", current_time)
print(" ")

#print Calendar
print(calendar.month(dt.year, dt.month))

#Made by Master Creeper