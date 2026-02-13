# mitheld
# Copyright with mitheld
# Created by mitheld on 29. July 2023
# Changes excluded 
# Version 1.1.0, from 29 July, 2023

import machine
import utime
import _thread
from machine import Pin,UART

#uart1 = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9), bits=8, parity=None, stop=1)
#print('UART1:', uart1)
#print()

GoalA = machine.Pin(2, machine.Pin.OUT)
analog_value_goal_a = machine.ADC(28)

GoalB = machine.Pin(3, machine.Pin.OUT)
analog_value_goal_b = machine.ADC(27)


#Sets Output-Pins to low
GoalA.value(0)
GoalB.value(0)

#Sets GoalA-Pin and Balleingabe-Pin to high
def setGoalA():
    print("Tor A")
    utime.sleep_ms(1000)
    GoalA.low()
    utime.sleep_ms(1000)
    GoalA.high()
    utime.sleep_ms(1000)
    GoalA.low()
    #sendData= ["GoalA"]
    #uart1.write(sendData)
    #uart1.write("GoalA")

#Sets GoalB-Pin and Balleingabe-Pin to high
def setGoalB():
    print("Tor B")
    utime.sleep_ms(1000)
    GoalB.low()
    utime.sleep_ms(1000)
    GoalB.high()
    utime.sleep_ms(1000)
    GoalB.low()
    #sendData1= ["GoalB"]
    #uart1.write(sendData1)
    #uart1.write("GoalB")
    
    
    

#Checks is A has scored
def checkIfAHasScoredAGoal():
    global average_goal_a,reading_goal_a
    if(reading_goal_a < average_goal_a - 2000):
        utime.sleep_us(10)
        reading_goal_a = analog_value_goal_a.read_u16()
        if(reading_goal_a < average_goal_a -1000):
            return True
        
    return False

#Checks is B has scored
def checkIfBHasScoredAGoal():
    global average_goal_b,reading_goal_b
    if(reading_goal_b < average_goal_b - 2000):
        utime.sleep_us(10)
        reading_goal_b = analog_value_goal_b.read_u16()
        if(reading_goal_b < average_goal_b -1000):
            return True
    return False
  
#Caluclate the average brightness of GoalA
def caluclateAverageBrightnessForGoalA():
    global i_goal_a, average_goal_a, last100_measurments_goal_a,reading_goal_a
    reading_goal_a = analog_value_goal_a.read_u16()
    if(i_goal_a==100):
        i_goal_a=0
        last100_measurments_goal_a[i_goal_a] = reading_goal_a
    else:
        last100_measurments_goal_a.append(reading_goal_a)
    i_goal_a=i_goal_a+1
    average_goal_a = sum(last100_measurments_goal_a)/len(last100_measurments_goal_a)
    
#Caluclate the average brightness of GoalB
def caluclateAverageBrightnessForGoalB():
    global i_goal_b, average_goal_b, last100_measurments_goal_b,reading_goal_b
    reading_goal_b = analog_value_goal_b.read_u16()
    if(i_goal_b==100):
        i_goal_b=0
        last100_measurments_goal_b[i_goal_b] = reading_goal_b
    else:
        last100_measurments_goal_b.append(reading_goal_b)
    i_goal_b=i_goal_b+1
    average_goal_b = sum(last100_measurments_goal_b)/len(last100_measurments_goal_b)

#Sets varibale to zero
i_goal_a = 0
last100_measurments_goal_a = []
average_goal_a = 0
reading_goal_a=0

i_goal_b = 0
last100_measurments_goal_b = []
average_goal_b = 0
reading_goal_b=0




while(True):
    caluclateAverageBrightnessForGoalA()
    if(checkIfAHasScoredAGoal()):
            setGoalA()
            
    
    caluclateAverageBrightnessForGoalB()
    if(checkIfBHasScoredAGoal()):
            setGoalB()
            
    #print("ADC: " , reading_goal_a) #Debug
    print(average_goal_a) #Debug
    print(average_goal_b) #Debug
    #print(sendData)
    #print(sendData1)
    utime.sleep(0.02)

    