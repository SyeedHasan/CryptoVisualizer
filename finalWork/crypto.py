#Imported modules
import requests
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

#User modules
from dateModule import getTime

#Functions
def scrapeData(cryptoCurrency, currency):
    
    #Set the url
    url = 'https://min-api.cryptocompare.com/data/pricemulti'
    
    #Add parameters to it by making a dictionary
    payload = {'fsyms': cryptoCurrency , 'tsyms': currency}
    
    #Make a get request using requests.get
    re = requests.get(url, params=payload)
    
    #Convert bytes into JSON format
    content = re.json()
    
    #Separate crypto currencies and other currencies by splitting
    cryptos = cryptoCurrency.split(',')

    #Hardcoded for now.    
    btc = content[cryptos[0]][currency]    
    eth = content[cryptos[1]][currency]
    
    #Returns the complete date
    currentTime = getTime()
    
    #Write the data
    writeData(btc, eth, currentTime) 

def writeData(btcValue, ethValue, time):
    #Make a complete string separated by commas for ease
    data = str(btcValue) + "," + str(ethValue) + "," + str(time)
    
    #Open the file in append mode
    with open('cryptoValues.txt', 'a') as fileObject:
        fileObject.write(data + ' ' + '\n')        

def readData():
    btc, eth, time = [], [], []
    #Open the file and read data line by line.
    with open('cryptoValues.txt', 'r') as fileObject:
        for line in fileObject:
            data = line.split(',')
            btc.append(data[0])
            eth.append(data[1])
            time.append(data[2].strip())
            
    return btc,eth,time

    
def animate(i):
#    scrapeData('BTC,ETH', 'USD')
    allData = readData()
    btcY = allData[0]
    ethY = allData[1]
    timeX = allData[2]
    #Clear the axis before re-plotting
    ax1.clear()
    plt.title('Bitcoin Visualization ')
    plt.xlabel('Time in mili-seconds (ms)')
    plt.ylabel('USD Price')
    ax1.plot(btcY)

#Animation works as a global function only. Hence this is called
# as the default code
style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ani = animation.FuncAnimation(fig, animate, interval=3000)
plt.show()
    
#Run the main function by default
#if __name__ == "__main__":
#    main()
