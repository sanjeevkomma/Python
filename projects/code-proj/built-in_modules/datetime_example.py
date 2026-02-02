import datetime

today_datetime = datetime.datetime.today()
today_date = datetime.date.today()

print(today_datetime) # 2026-02-02 12:41:05.758163
print(today_datetime.date()) # 2026-02-02
print(today_datetime.time()) # 12:52:44.130338
print('===================')
print(today_date) # 2026-02-02
print(today_date.year) # 2026
print(today_date.month) # 2
print(today_date.day) # 2
print(today_date.weekday()) # 0
print('===================')
print(today_datetime.hour) # 12
print(today_datetime.minute) # 45
print(today_datetime.second) # 13
print('===================')
some_datetime = datetime.datetime(2019, 5, 27,9,5,25)
print(some_datetime) # 2019-05-27 09:05:25
modified_datetime = some_datetime + datetime.timedelta(days=90)
print(modified_datetime) # 2019-08-25 09:05:25
modified_datetime = modified_datetime + datetime.timedelta(weeks=4)
print(modified_datetime) # 2019-09-22 09:05:25
modified_datetime = modified_datetime + datetime.timedelta(hours=67)
print(modified_datetime) # 2019-09-25 04:05:25
