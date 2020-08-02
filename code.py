"""
Doc String:
Nox app player
1920*1080
far left side
wholescreen visible
touching bot - top
"""
import win32api, win32con
from PIL import ImageGrab
from PIL import Image
from PIL import ImageOps
import os
import time
from numpy import *

#      Globals
# ------------------
 
x_pad = 1
y_pad = 31

def screenGrab():
    box = (x_pad+1, y_pad+1, x_pad+564,y_pad+1009 )
    im = ImageGrab.grab()
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +'.png', 'PNG')
    return im

#defining controls
def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print ("LClicked!")
    
def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))

#getting cords
def get_cords():
    (x,y) = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print (x,y)


#locations for clicks
class Locate:
    #key areas
    ClickArea = (282,448)
    SuperC = (462,74)
    
    #Figs
    FigScreen = (154,913)
    FirstUp = (474,700)
    SecondUp = (466,797)

    #Miku
    MikuScreen = (45,909)
    MikuUp = (477,700)

    #Abilities
    Shout = (170,970)
    Splash = (250,970)
    FullV = (340,970)
    Ensemble = (424,970)
    Sonic = (505,970)

    #Reset Upgrades
    ExpansionTab = (424,911)
    NewExpansion = (410,674)
    ReStage = (420,814)

#Defining Actions
def Clicks():
    mousePos(Locate.ClickArea)
    time.sleep(.04)
    leftClick()

def FigUp():
    mousePos(Locate.FigScreen)
    time.sleep(.1)
    
    leftClick()
    time.sleep(.1)
    
    screenGrab()
    s = screenGrab()
    time.sleep(.1)
    
    if s.getpixel(Locate.FirstUp) == (174, 17, 66):
        print ('Fig Up!')
        mousePos(Locate.FirstUp)
        time.sleep(.1)
        leftClick()
        time.sleep(.1)
    elif s.getpixel(Locate.SecondUp) == (174, 17, 66):
        print ('2nd Fig Up!')
        mousePos(Locate.SecondUp)
        time.sleep(.1)
        leftClick()
        time.sleep(.1)
    elif s.getpixel(Locate.SecondUp) == (196, 31, 121):
        print ('2nd Fig Up!')
        mousePos(Locate.SecondUp)
        time.sleep(.1)
        leftClick()
        time.sleep(.1)
    else:
        print('Fig Ups not Availible')

def MikuUp():
    mousePos(Locate.MikuScreen)
    time.sleep(.1)
    
    leftClick()
    time.sleep(.4)
    
    screenGrab()
    s = screenGrab()
    time.sleep(.2)
    
    if s.getpixel(Locate.MikuUp) == (196, 31, 121): #198,29,130
        print ('Miku Up!')
        mousePos(Locate.MikuUp)
        time.sleep(.1)
        leftClick()
        time.sleep(.1)
    else:
        print('Miku Up not Availible')

def Abilities():
    screenGrab()
    time.sleep(.1)
    s = screenGrab()
    if s.getpixel(Locate.Shout) == (254, 187, 0):
        print ('Shouting!')
        mousePos(Locate.Shout)
        time.sleep(.1)
        leftClick()
        time.sleep(2.1)
    if s.getpixel(Locate.Splash) == (254, 187, 0):
        print ('Splashing!')
        mousePos(Locate.Shout)
        time.sleep(.1)
        leftClick()
        time.sleep(2.1)
    if s.getpixel(Locate.FullV) == (254, 187, 0):
        print ('Turning it to 11!')
        mousePos(Locate.FullV)
        time.sleep(.1)
        leftClick()
        time.sleep(2.1)
    if s.getpixel(Locate.Ensemble) == (254, 187, 0):
        print ('Together!')
        mousePos(Locate.FullV)
        time.sleep(.1)
        leftClick()
        time.sleep(2.1)
    if s.getpixel(Locate.Sonic) == (254, 187, 0):
        print ('SAAAANIC BOOOOOOM!')
        mousePos(Locate.FullV)
        time.sleep(.1)
        leftClick()
        time.sleep(2.1)
        
def SuperC():
    screenGrab()
    time.sleep(.1)
    s = screenGrab()
    if s.getpixel(Locate.SuperC) != (197, 197, 188):
        print('Continuing Super Concert')
        mousePos(Locate.SuperC)
        time.sleep(0.1)
        leftClick()
        time.sleep(2.1)
    else:
        print('things are normal')


def main():
    screenGrab()
    while True:
        time.sleep(.2)
        Abilities()
        time.sleep(.2)
        MikuUp()
        time.sleep(.2)
        FigUp()
        SuperC()
        for i in range(750):
            Clicks()
 
if __name__ == '__main__':
    main()
