from datetime import datetime

date = datetime.now()

c = str(date.year) + "-" +  str(date.month) + "-" + str(date.day)

a = str(datetime.now().time())

b = a.split('.')

print(b)

d = datetime.strptime(b[0], "%H:%M:%S")
d = d.strftime("%I:%M %p ")
print(d)


