import serial
import time
#import emo
#from emo import z

ArduinoData = serial.Serial('com3', 9600,timeout=0)    
#ArduinoSerial = serial.Serial('com3',9600,timeout=0) #Create Serial port object called arduinoSerialData
time.sleep(2) #wait for 2 secounds for the communication to get established

#print (ArduinoData.readline()) #read the serial data and print it as line

import pickle
f=open('store.pckl','rb')
var = pickle.load(f)
f.close()
#print("var:",var)

#while (1): #Do this forever

if var == 0:#if the value is 1
   # print("abhi") #by printing this i'm checking whether it'satisfying the condition or not
    ArduinoData.write('0'.encode()) #send 0
    print ("Green LED turns ON")
    time.sleep(1)
    
elif var == 1: #if the value is 0
    ArduinoData.write('1'.encode()) #send 1
    print ("Red LED turns ON")
    time.sleep(1)

elif var == 2: #if the value is 0
    #print("abhi")
    ArduinoData.write('2'.encode()) #send 2
    print ("Blue LED turns ON")
    time.sleep(1)

elif (var == 3): #if the value is 0
    ArduinoData.write('3'.encode()) #send 3
    print ("LED turns ON")
    time.sleep(1)

elif (var == 4): #if the value is 0
    ArduinoData.write('4'.encode()) #send 3
    print ("LED turns ON")
    time.sleep(1)
