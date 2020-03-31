# import datetime
# import time

# datetime.timedelta()
# datetime.date()
# print(datetime.datetime.now())
# print(datetime.datetime.today())
# now_time = datetime.datetime.now()
# print(now_time.date())
# print(now_time.time())
# print(now_time.year)
# print(now_time.month)
# print(now_time.day)
# print(time.time())
# time.sleep(2)

from datetime import datetime, date, time, timedelta
d = datetime(2020, 10, 30, 14, 5)
print(d)
d2 = date(2019, 3, 23)
print(d2)
t = time(9, 0)
print(t)
# 日期、时间与字符串转换
ds = '2018/10/3T12:42:09'
ds_t = datetime.strptime(ds, '%Y/%m/%dT%H:%M:%S')
n = datetime.now()
n_str = n.strftime('%Y/%m/%dT%H:%M:%S')

n = datetime.now()
n_next = n + timedelta(days = 5, hours = 42)
print(n)
print(n_next)
d1 = datetime(2018, 10, 15)
d2 = datetime(2018, 11, 12)
rest = d2 -d1
print(rest.days)