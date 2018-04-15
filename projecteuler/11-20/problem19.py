# https://projecteuler.net/problem=19
#
# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# 1900 Jan 1 = Monday (1)
# Sunday:0, Monday:1, Tuesday:2, Wednesday:3, Thursday:4, Friday:5, Saturday:6

dow = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}

def step_dow(m):
    if m in {4, 6, 9, 11}:
        return 30 % 7
    elif m == 2:
        if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
            return 29 % 7
        else:
            return 28 % 7
    else:
        return 31 % 7


first_day_of_week = 1
# calculate dow of 1900 Dec 1st
y = 1900
for m in range(1,12):
    step = step_dow(m)
    first_day_of_week = (first_day_of_week + step) % 7

# print("1900 Dec 1st = " + dow[first_day_of_week])


sunday_count = 0
for y in range(1901, 2001):
    for m in range(0, 12):
        step = step_dow(m)
        first_day_of_week = (first_day_of_week + step) % 7
        # print(str(y) + ", " + str(m) + " 1st = " + dow[first_day_of_week])
        if first_day_of_week == 0:
            sunday_count += 1

print(sunday_count)