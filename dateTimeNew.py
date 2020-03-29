import datetime
import time
# datetime.timedelta()
# datetime.date()
print(datetime.datetime.now())
print(datetime.datetime.today())
now_time = datetime.datetime.now()
print(now_time.date())
print(now_time.time())
print(now_time.year)
print(now_time.month)
print(now_time.day)
print(time.time())
time.sleep(2)