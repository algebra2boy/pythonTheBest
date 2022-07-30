import datetime


now = datetime.datetime.now()
print(now)  # 2022-07-30 17:38:09.965585

today_day = now.day
today_year = now.year
print(today_year)   # 2022
print(today_day)     # 30
print(now.weekday())    # return 5 cuz today's a Saturday. (0 is monday)