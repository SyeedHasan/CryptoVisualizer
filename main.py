import requests as r
import datetime
import re
import matplotlib.pyplot as plt

re = r.get('https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH&tsyms=USD,EUR,PKR')

content = re.json()

curr = 'USD'

btc = content['BTC'][curr]

wr = str(btc)


date = datetime.datetime.now()

values = []
time = []
n = 0

with open('a.txt', 'a') as fO:
#    fO.write(wr + ' ' + str(date) +  '\n')
    fO.write(wr + ' ' + '\n')

with open('a.txt', 'r') as fO:
    for line in fO:
#        print(line.strip())
        values.append(line.strip())
        n = n+1
        time.append(n)
        
        
print(values)
print(time)


plt.plot(time, values)
plt.title('CHART OF BTC')
plt.xlabel('time in milliseconds')
plt.ylabel('PRICE')
plt.show()
plt.savefig('sqPlot.png', bbox_inches='tight')



#?fsyms=BTC,ETH&tsyms=USD,EUR,PKR