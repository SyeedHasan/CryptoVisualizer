
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
        print("Successfully written.")
        

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
    scrapeData('BTC,ETH', 'USD')
    allData = readData()
    btcY = allData[0]
    ethY = allData[1]
    timeX = allData[2]
    #Clear the axis before re-plotting
    ax1.clear()
    plt.title('Bitcoin Value wrt Time (1MS) ')
    plt.xlabel('1MS')
    plt.ylabel('USD Price')
    plt.legend(['Blue: Bitcoin, Red:Ethereum'], loc='upper left')
    
    ax1.plot(btcY)
    
    
def animateGraph(): #Possibly a new module
    style.use('fivethirtyeight')

    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()





style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
plt.title('CHART OF ')
plt.xlabel('time in milliseconds')
plt.ylabel('price in ')
plt.legend(['Blue: Bitcoin, Red:Ethereum'], loc='upper left')

ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()
    
#Run the main function by default
#if __name__ == "__main__":
#    main()