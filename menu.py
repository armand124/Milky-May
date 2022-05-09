import os
from declarations import *
import pygame as picture
from concurrent.futures import ThreadPoolExecutor

#Function that handles the Continue Button in the Menu : logic and UI
@staticmethod
def contButton():
    if utils.sesInfo=="0":
        utils.monitor_screen.blit(GUI.continueButtonLocked,(utils.Buttonscreen_width_menu,utils.Buttonscreen_height_menu))
    else:
        continueButton = Button(utils.Buttonscreen_width_menu,utils.Buttonscreen_height_menu , GUI.continueButtonPressed,GUI.continueButtonUnpressed)
        if continueButton.buttonPressed():
            utils.screenPhase = 2
            utils.enteredInGame = True
        continueButton.showButton()

#Function that handles the (New Game) Button in the Menu : logic and UI
@staticmethod
def newGameButton():
    button = Button(utils.Buttonscreen_width_menu,utils.Buttonscreen_height_menu+150,GUI.newgameButtonPressed,GUI.newgameButtonUnpressed)
    if button.buttonPressed():
        #If NewGame is pressed rewrites the checkpoint and enables the continue button
        file = open(os.path.join("menu","sessions.txt"),"w")
        file.write("1")
        file.close()
        utils.screenPhase = 2
        utils.enteredInGame = True
    button.showButton()

#Function that handles the Settings Button in the Menu : logic and UI
@staticmethod
def settingsButton():
    button = Button(utils.Buttonscreen_width_menu,utils.Buttonscreen_height_menu+300,GUI.settingsButtonPressed,GUI.settingsButtonUnpressed)
    if button.buttonPressed():
        utils.enteredInSettings = True
    button.showButton()

#Function that handles the Exit Button in the Menu : logic and UI
@staticmethod
def closeButton():
    button = Button(utils.Buttonscreen_width_menu,utils.Buttonscreen_height_menu+450,GUI.closeButtonPressed,GUI.closeButtonUnpressed)
    if button.buttonPressed():
        utils.runningSes = False
    button.showButton()

@staticmethod
def backButtonForSettings():
    button = Button(30,30,GUI.backButtonPressed,GUI.backButtonUnpressed)
    if button.buttonPressed():
        utils.enteredInSettings = False
    button.showButton()


class Menu():
 #Menu Screen Update Function
 def UpdateMenuScreen():
     utils.monitor_screen.blit(GUI.background,(0,0))
     utils.monitor_screen.blit(GUI.gameTitle,GUI.gameTitle.get_rect(center=(utils.screen_width/2 - 30,utils.screen_height/9 + 30)))
     newGameButton()
     settingsButton()
     contButton()
     closeButton()
     picture.display.update()

@staticmethod
def assignSound(x,smaller):
     if smaller:
         utils.volumeButton[x] = SoundButton(utils.Volume_x+(utils.sliderDistance*x),utils.Volume_y,GUI.sliderPressed)
     else:
         utils.volumeButton[x] = SoundButton(utils.Volume_x+(utils.sliderDistance*x),utils.Volume_y,GUI.sliderUnpressed)

class Setari():
 
 @staticmethod
 def settingsMenu():
    utils.monitor_screen.blit(GUI.backgroundGame,(0,0))
    utils.monitor_screen.blit(GUI.soundLogo,(650,200))
    i = 0
    while i<=9:
        utils.volumeButton[i].showButton()
        i = i+1
    i = 0
    while i<=9:
        if utils.volumeButton[i].buttonPressed():
            utils.lastVolume = i
            file = open(os.path.join("menu","volume.txt"),"w")
            file.write(str(i))
            file.close
            j = 0
            if i==0:
                while j <=9:
                    utils.volumeButton[j] = SoundButton(utils.Volume_x+(utils.sliderDistance*j),utils.Volume_y,GUI.sliderUnpressed)
                    j=j+1
            else:
             while j <= 9:
                assignSound(j,j<=i)
                j=j+1
        i=i+1
    i = 0
    while i<=9:
        utils.volumeButton[i].showButton()
        i=i+1      
    backButtonForSettings() 