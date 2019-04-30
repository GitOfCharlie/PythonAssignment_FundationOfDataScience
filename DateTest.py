import math
from datetime import datetime, timedelta

# 1
# time = eval(input())
# date = datetime.fromtimestamp(time)
# print(date.strftime("%Y-%m-%d %H:%M"))

# 2
# time = input()
# new_date = datetime.strptime(time, '%Y-%m-%d')
# print(new_date.timetuple().tm_yday)

# 3
# new_date1 = datetime.strptime(input(), '%Y-%m-%d %H:%M')
# new_date2 = datetime.strptime(input(), '%Y-%m-%d %H:%M')
# if new_date1 > new_date2:
#     delta = new_date1 - new_date2
# else:
#     delta = new_date2 - new_date1
# days = delta.days
# seconds = delta.seconds
# hours = days*24 + int(seconds / 3600)
# print(days, hours)


# 4
# week_day_dict = {
#     0: 'Monday',l
#     1: 'Tuesday',
#     2: 'Wednesday',
#     3: 'Thursday',
#     4: 'Friday',
#     5: 'Saturday',
#     6: 'Sunday',
# }
# date = datetime.strptime(input(), "%Y-%m-%d")
# print(week_day_dict[date.weekday()])