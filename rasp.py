from datetime import datetime
from timelessons import*
import time

k = 0
now  = datetime.now()

H = 0
M = 0

a = str(now)
a = a.split(' ')
a = a[1]
a2 = int(a[0:2]) + 5
a1 = int(a[3:5])

if a2 == 8:
        H = h1
        M = m1
        k = 1
if a2 == 9:
        if a1 < 10:
            H = h1
            M = m1
            k = 1
        if a1 > 10:
            H = h2
            M = m2
            k = 2
if a2 == 10:
        if a1 > 55:
            H = h4
            M = m4
            k = 4
        else:
            H = h3
            M = m3
            k = 3
if a2 == 11:
        if a1 < 35:
            H = h4
            M = m4
            k = 4
        else:
            H = h5
            M = m5
            k = 5
if a2 == 12:
        if a1 < 20:
            H = h5
            M = m5
            k = 5
        else:
            H = h6
            M = m6
            k = 6
if a2 == 13:
        if a1 < 5:
            H = h6
            M = m6
            k = 6
        else:
            H = h7
            M = m7
            k = 7
if a2 == 14:
        H = h8
        M = m8


then = datetime(1, 1, 1, H, M, 0)
duration = then - now
duration = str(duration)
x = duration.split(',')
x1 = x[1].split(':')
x = int(x1[1])
dku_0 = ('До конца', k, 'урока осталось', x, 'минут')
dku_0 = str(dku_0)
dku = ''
for i in dku_0:
    if i != '(' and i != "'" and i != ',' and i != ')':
        dku += i


