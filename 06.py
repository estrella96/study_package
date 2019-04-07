import calendar
# calendar:获取一年的日历字符串
# 参数：w=每个日期之间的间隔字符数 l=每周占用的行数 c=每个月之间的间隔字符数
cal=calendar.calendar(2019)
cal=calendar.calendar(2019,l=0,c=5)
# print(cal)
calendar.isleap(2000)
m=calendar.month(2019,4)
m=calendar.monthcalendar(2019,4)

# print(m)
# w,t=calendar.monthrange(2019,4)
# print(w)
# print(t)

#time
import time
# print(time.timezone)
# print(time.altzone)
# print(time.daylight)
# print(time.time())
# print(time.localtime())

#格式化
#2019年4月27日 18:00
t=time.localtime()
ft=time.strftime("%Y年%m月%d日 %H:%M",t)
# print(ft)

import datetime
dt=datetime.datetime(2018,3,26)
print(dt.today())
print(dt.now())
print(dt.fromtimestamp(time.time()))
t1=datetime.datetime.now()
print(t1.strftime("%Y-%m-%d %H:%M:%S"))
td=datetime.timedelta(hours=1)
print((t1+td).strftime("%Y-%m-%d %H:%M:%S"))

#timeit
import timeit
c='''
sum=[]
for i in range(1000):
    sum.append(i)
'''
t1=timeit.timeit(stmt="[i for i in range(1000)]",number=100000)
t2=timeit.timeit(stmt=c,number=100000)
print(t1)
print(t2)