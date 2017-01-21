import datetime 
str = '18/01/2017'
x= datetime.datetime.strptime(str,'%d/%m/%Y')
print  datetime.datetime.combine(x, datetime.time(0, 0))
