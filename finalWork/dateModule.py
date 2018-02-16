#Imported modules
from datetime import datetime

#Returns the current time
def getTime():
    
    date = datetime.now()
    
    #Alternate dhoondh
    currentDate = str(date.year) + "-" +  str(date.month) + "-" + str(date.day)
    
    time = str(datetime.now().time())
    
    #Take the hours, minutes and seconds only. NO MS.
    HMS = time.split('.')
        
    #Convert into 12-hour format. 
    currentTime = datetime.strptime(HMS[0], "%H:%M:%S")
    currentTime = currentTime.strftime("%I:%M %p ")
    
    #Make a string and return this.
    completeDate = str(currentDate) + " " +  str(currentTime)

    return completeDate


getTime()
