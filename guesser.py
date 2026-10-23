
#the main correlation i will be testing for is the numbers people choose based on the time of day, i could also swicth this for rather than number
#make it something like happiness scale rating, although this data is ordinal
import scipy
import matplotlib.pyplot as plt
import csv
from datetime import time
import datetime
import numpy as np
import pandas as pd
arr = []
day = []
def timefetch():
    current = datetime.datetime.now()

    poopy = current.strftime("%H:%M")
    return poopy #i need to send this into db to be analuysed or just as arrays ig
#this data also needs to be turned into a form which computers can undrstand, such as minutes from midnight
def hourtomin(time2):
    formula1 = str(time2)
    formula2 = formula1[0] + formula1[1]
    hrinmin = int(formula2) * 60
    mininmin = formula1[3]+formula1[4]
    
    frommid = int(hrinmin) + int (mininmin)
    print (frommid)
    return frommid

time1=[]
run= True
def guess():
    run= True
    
    user_input = int(input("enter a number between 1 and 100:"))

    while run == True:

        if user_input > 1 and user_input < 100:
                
            print ("success")
            choice = str(input("again?"))
            if choice=="y":
                arr.append(user_input)
                x = datetime.datetime.now()
                day1 = x.strftime("%A") 
                day.append(x.strftime("%A"))
                time2 = hourtomin(timefetch())
                time1.append(hourtomin(timefetch()))
                with open('data.csv', "a", newline='') as csvfile:
                    fieldnames = ["day", "time", "rating"]
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    stringtext = "{'day' : day1, 'time': time2, 'rating': user_input}"
                    
                    writer.writerow({
        "day": day1,
        "time": time2,
        "rating": user_input
    })
                print (time1)
                print (day)

                guess()
            else:
                run = False
                print ("end")
        else:
            print ("insert correct value")
            guess()

    return run



def interprete():
    #this is where im gonna use pandas to read the data and analyse it.
    data = pd.read_csv("data.csv", usecols=['time', 'rating'])

    print (data)
    corr_data = data.corr()
    print (corr_data)
    #clean_data = data.dropna()
    #clean_focus = clean_data['time':'rating']
    #print (clean_focus.to_string)
    return corr_data, data
interprete()

def graph():
    data = pd.read_csv("data.csv", usecols=['time', 'rating'])

    #displaying on graph
    plt.plot(data)
    plt.savefig("graph.png")
    plt.show()

graph()