import os
from menu import *
from declarations import *
from questions import Fact as info
import pygame as picture
import sys
from game import Game

picture.init()
aux_screen = picture.display.set_mode((1920,1080))

#Initialize Background Music
music = picture.mixer.Sound(os.path.join("sounds","backgroundMusic.mp3"))
music.play(-1) #Loop
music.set_volume(float(utils.lastVolume)/10.0)

@staticmethod
def getVolumeSave():
 i = 0
 while i<=9:
    if utils.lastVolume>=i:
        utils.volumeButton.append(SoundButton(utils.Volume_x+(utils.sliderDistance*i),utils.Volume_y,GUI.sliderPressed))
    else:
        utils.volumeButton.append(SoundButton(utils.Volume_x+(utils.sliderDistance*i),utils.Volume_y,GUI.sliderUnpressed))
    i = i+1

getVolumeSave()

#Enables fullscreen
flags = picture.FULLSCREEN | picture.DOUBLEBUF
screen = picture.display.set_mode((1920,1080), flags, 16)

clock = picture.time.Clock()

@staticmethod
def main():
 while utils.runningSes:
    #Mouse and Keyboard events
    utils.mouseDown = False
    for event in picture.event.get():
        if event.type == picture.QUIT or utils.runningSes == False:
            sys.exit()
        if event.type == picture.MOUSEBUTTONDOWN:
            utils.mouseDown = True
        if utils.enableWriting:
            if event.type == picture.KEYDOWN:
              if event.key == picture.K_BACKSPACE:
                utils.user_txt = utils.user_txt[:-1]
              else:
               if len(utils.user_txt)<=10:
                utils.user_txt += event.unicode
              if event.key == picture.K_RETURN:
                  utils.doneWriting = True
    #Updating Screen
    music.set_volume(float(utils.lastVolume)/10.0)
    if utils.enteredInGame is False and utils.enteredInSettings is False:
        Menu.UpdateMenuScreen()
    if utils.enteredInGame is True:
        Game.runSpecificLevel()
    if utils.enteredInSettings is True :
        Setari.settingsMenu()
    picture.display.flip()
    clock.tick(60)

main()