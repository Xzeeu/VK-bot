from datetime import datetime
from timelessons import*

'''if datetime.datetime.today().isoweekday() == 7:
    rasp = '1.Физика\n2.Физика\n3.Русский\n4.Математика\n5.Математика\n6.Английский\n7.Физкультура\n8.Физкультура'''

k = 0
then = datetime(1, 1, 1, 15, 45, 0)
now  = datetime.now()
duration = then - now
duration = str(duration)
x = duration.split(',')
x1 = x[1].split(':')
x = int(x1[1])
print(x)
