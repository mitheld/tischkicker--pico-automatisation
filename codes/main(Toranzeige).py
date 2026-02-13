# mitheld
# Copyright with mitheld
# Created by mitheld on 30 July, 2023
# Changes excluded 
# Version 1.0.5, from 17 February 2024


from picounicorn import PicoUnicorn
import utime
from font import *
#import machine
from machine import Pin,UART
#from machine import Pin

picounicorn = PicoUnicorn()

#uart0 = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1), bits=8, parity=None, stop=1)
#playerAPin_value = machine.ADC(28) # 
#playerBPin_value = machine.ADC(27) #
PlayerAin_value = Pin(0, Pin.IN, Pin.PULL_DOWN)
PlayerBin_value = Pin(1, Pin.IN, Pin.PULL_DOWN)

#Definition of the class for flashing
class structFlashInformation:
     def __init__(self):
        self.flash_time_in_ms=0
        self.flash_count=0
        
#Definition of the class for the colors, how they are specified 
class structColourInformation:
    def __init__(self):
        self.red=0
        self.green=0
        self.blue=0

class structPlayer:
    def __init__(self):
        self.colourInformation = structColourInformation()
        self.flashInformation = structFlashInformation()
        self.flashInformation.flash_time_in_ms=250
        self.flashInformation.flash_count=4
        self.colourInformation.green=255
        self.goal_count = 0
        self.player_id =0
        self.has_scored = False


display_width = picounicorn.get_width()
display_height = picounicorn.get_height()


#Definiton of the viewed numbers as Arrays, called as characters
characterGoals = {}
characterGoals[0] = zero
characterGoals[1] = one
characterGoals[2] = two
characterGoals[3] = three
characterGoals[4] = four
characterGoals[5] = five
characterGoals[6] = six
characterGoals[7] = seven
characterGoals[8] = eigth
characterGoals[9] = nine	#Nine is the highest number what can be showed, because of the need to show two numbers

#Definiton of the viewed characters as Arrays
characterWinner = {}
characterWinner['W'] = W
characterWinner['I'] = I
characterWinner['N'] = N
characterWinner['O'] = O
characterWinner['A'] = A	#For the respective player, designated as player A or B/goal A or B
characterWinner['B'] = B	#For the respective player, designated as player A or B/goal A or B

#Defintion of the background color of the LED-Matrix and the given of color for the Players
blackColourInformation = structColourInformation()
playerA = structPlayer()
playerA.player_id = 1	#Definition of the player_id in order to be able to retrieve it later on. Furthermore, the player who has just scored a goal serves as an indicator for the program. : Here, player_A gets the player_id 1
playerA.colourInformation.green = 255	#Assignment of the player's color
playerB = structPlayer()
playerB.player_id = 2	#Definition of the player_id in order to be able to retrieve it later on. Furthermore, the player who has just scored a goal serves as an indicator for the program. Here player_B gets the player_id 2
playerB.colourInformation.blue = 255	#Assignment of the player's color

class handleDisplay:
    def printPixel(x,y ,colourInformation):
        picounicorn.set_pixel(x,y,colourInformation.red,colourInformation.green,colourInformation.blue)

#Setting up the function when goal_A/player_A has scored a goal, what should happen next
def showPlayerAHasScored():
    playerA.goal_count +=1
    playerA.has_scored = True
    
#Setting up the function when goal_B/player_B has scored a goal, what should happen next
def showPlayerBHasScored():
    playerB.goal_count +=1
    playerB.has_scored = True

#Setting up the function that a specially created frame around the result should flash in the player color.
def flashReactangle(structFlashInformation, structColourInformation):
    timestamp =0
    while timestamp < structFlashInformation.flash_count:
        drawReactangle(structColourInformation)
        utime.sleep_ms(structFlashInformation.flash_time_in_ms)
        drawReactangle(blackColourInformation)
        utime.sleep_ms(structFlashInformation.flash_time_in_ms)
        timestamp +=1
        
#Set up the function to draw the rectangle around the result    
def drawReactangle(structColourInformation):
    drawYLines(structColourInformation)
    drawXLines(structColourInformation)

#Set up the function to draw the vertical lines of the rectangle
def drawYLines(structColourInformation):
    for y in range(display_height):
        picounicorn.set_pixel(0,y,structColourInformation.red,structColourInformation.green,structColourInformation.blue)
        picounicorn.set_pixel(display_width-1,y,structColourInformation.red,structColourInformation.green,structColourInformation.blue)

#Set up the function to draw the horizontal lines of the rectangle
def drawXLines(structColourInformation):
    for x in range(display_width):
        picounicorn.set_pixel(x,0,structColourInformation.red,structColourInformation.green,structColourInformation.blue)
        picounicorn.set_pixel(x,display_height-1,structColourInformation.red,structColourInformation.green,structColourInformation.blue)
       
def clearDisplay():
    for y in range(display_height):
         for x in range(display_width):
              picounicorn.set_pixel(x, y, 0, 0, 0)

#Statement of the function, to display the one number of the result
def displaySingleNumber(structPlayer, offset_second_number):
    for row in range(display_height-2):
        char_width = len(characterGoals[structPlayer.goal_count][0])
        for col in range (0,char_width):
                x = col + 2 + offset_second_number
                y = row+1
            
                # write pixel
                if x < display_width-2 and x > -1:
                    if characterGoals[structPlayer.goal_count][row][col] == '1':
                        picounicorn.set_pixel(x, y, structPlayer.colourInformation.red, structPlayer.colourInformation.green, structPlayer.colourInformation.blue)
                    else:
                        picounicorn.set_pixel(x, y, 0, 0, 0)


#Statement of the function, to display the one number of the result
def displaySinglChar(char):
    for row in range(display_height-2):
        char_width = len(characterWinner[char][0])
        for col in range (0,char_width):
                x = col + 2 
                y = row+1
            
                # write pixel
                if x < display_width-2 and x > -1:
                    if characterWinner[char][row][col] == '1':
                        picounicorn.set_pixel(x, y, 255, 255, 255)
                    else:
                        picounicorn.set_pixel(x, y, 0, 0, 0)

#Setting up the function to display the dots between the numbers of the result. To show that the display is running, it flashes every second                       
def displayDots(structPlayer, offset):
    char_width = len(characterGoals[structPlayer.goal_count][0])
    x = char_width + 2 + offset 
    
    picounicorn.set_pixel(x, 2, 255, 255, 255)
    picounicorn.set_pixel(x, 4, 255, 255, 255)
    

#List of the function that combines the functions /displaySinglChar , /drawReactangle and /displayDots into one function. To simplify the use
def displayScore(structPlayerA, structPlayerB):
    clearDisplay()
    displaySingleNumber(structPlayerA,0)
    displayDots(playerA, 1)
    char_width = len(characterGoals[structPlayerA.goal_count][0])
    offset_player_b = char_width+3
    displaySingleNumber(structPlayerB,offset_player_b)
    if(playerA.has_scored):
        flashReactangle(playerA.flashInformation,playerA.colourInformation)
        playerA.has_scored = False
    elif (playerB.has_scored):
        flashReactangle(playerB.flashInformation,playerB.colourInformation)
        playerB.has_scored = False
    
#Setting up the function to display the winner       
def showWinner(structPlayer):
        flashReactangle(structPlayer.flashInformation,structPlayer.colourInformation)
        clearDisplay()
        if structPlayer.player_id == 1:
             displaySinglChar('A')
             utime.sleep_ms(500)
        else:
             displaySinglChar('B')
             utime.sleep_ms(500)
        displaySinglChar('W')
        utime.sleep_ms(500)
        clearDisplay()
        displaySinglChar('O')
        utime.sleep_ms(500)
        clearDisplay()
        displaySinglChar('N')
        
def CalculateAverageGoalA():                                                            
    global i_goal_a, average_goal_a, last100_measurments_goal_a, reading_goal_a
    reading_goal_a = playerAPin_value.read_u16()
    if(i_goal_a == 100):
        i_goal_a = 0
        last100_measurments_goal_a[i_goal_a]= reading_goal_a
    else:  
        last100_measurments_goal_a.append(reading_goal_a)
    i_goal_a = i_goal_a +1
    average_goal_a = sum(last100_measurments_goal_a)/len(last100_measurments_goal_a)



def checkIfGoalAHasScored():                                    
    global average_goal_a, reading_goal_a
    if (reading_goal_a > average_goal_a -10000):
        utime.sleep_us(10)
        reading_goal_a = playerAPin_value.read_u16()
        if(reading_goal_a > average_goal_a -5000):
            return True
    return False


def CalculateAverageGoalB():
    global i_goal_b, average_goal_b, last100_measurments_goal_b, reading_goal_b
    reading_goal_b = playerBPin_value.read_u16()
    if(i_goal_b == 100):
        i_goal_b = 0
        last100_measurments_goal_b[i_goal_b] = reading_goal_b
    else:
        last100_measurments_goal_b.append(reading_goal_b)
    i_goal_b = i_goal_b +1
    average_goal_b = sum(last100_measurments_goal_b)/len(last100_measurments_goal_b)



def checkIfGoalBHasScored():
    global average_goal_b, reading_goal_b
    if(reading_goal_b < average_goal_b -10000):
        utime.sleep_us(10)
        reading_goal_b = playerBPin_value.read_u16()
        if(reading_goal_b < average_goal_b -5000):
            return True
    return False




i_goal_a = 0
last100_measurments_goal_a = []
average_goal_a = 0
reading_goal_a = 0

i_goal_b = 0
last100_measurments_goal_b = []
average_goal_b = 0
reading_goal_b = 0



#Player A = GREEN (green=255) #Debug
#Player B = BLUE (blue=255) #Debug

#Always running process that both checks and outputs that a goal has been scored. The loop uses the functions and classes that have just been created.
while(True):
    displayScore(playerA, playerB) 
    print(PlayerAin_value.value()) #Debug
    print(PlayerAin_value.value()) #Debug
    #CalculateAverageGoalA()
    if PlayerAin_value.value()== True:
        if playerA.goal_count < 9:
            showPlayerAHasScored()
            print("GoalA")
        else:
            showWinner(playerA)
            playerA.goal_count = 0
            playerB.goal_count = 0
        
    #CalculateAverageGoalB
    if PlayerBin_value.value()== True:
        if playerB.goal_count < 9:	#If player_A is under 9 goals, the game continues, but if player_A or player_B is over 9 goals, the function /showWinner is executed with the respective winner.
            showPlayerBHasScored()
            print("GoalB")
        else:
            showWinner(playerB)
            playerB.goal_count = 0
            playerA.goal_count = 0
utime.sleep_ms(500)

