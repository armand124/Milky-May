import os
import pygame as picture
picture.init()
aux_screen = picture.display.set_mode((1920,1080))
#Loading all the assets
class GUI():
 backButtonPressed = picture.image.load(os.path.join("menu", "backPressed.png")).convert_alpha()
 backButtonUnpressed = picture.image.load(os.path.join("menu" , "backUnpressed.png")).convert_alpha()
 continueButtonLocked = picture.image.load(os.path.join("menu","continueButtonLocked.png")).convert_alpha()
 continueButtonUnpressed = picture.image.load(os.path.join("menu","continueButton.png")).convert_alpha()
 continueButtonPressed = picture.image.load(os.path.join("menu","continueButtonPressed.png")).convert_alpha()
 newgameButtonPressed = picture.image.load(os.path.join("menu", "newgamePressed.png")).convert_alpha()
 newgameButtonUnpressed = picture.image.load(os.path.join("menu" , "newgameUnpressed.png")).convert_alpha()
 settingsButtonPressed = picture.image.load(os.path.join("menu", "settingsPressed.png")).convert_alpha()
 settingsButtonUnpressed = picture.image.load(os.path.join("menu" , "settingsUnpressed.png")).convert_alpha()
 closeButtonPressed = picture.image.load(os.path.join("menu", "closePressed.png")).convert_alpha()
 closeButtonUnpressed = picture.image.load(os.path.join("menu" , "closeUnpressed.png")).convert_alpha()
 earthImage = picture.image.load(os.path.join("menu","earth.png")).convert_alpha()
 earthImagePressed = picture.image.load(os.path.join("menu","earthPressed.png")).convert_alpha()
 solar = picture.image.load(os.path.join("menu","solarSystem.png")).convert_alpha()
 solarPressed = picture.image.load(os.path.join("menu","solarSystemPressed.png")).convert_alpha()
 nebula = picture.image.load(os.path.join("menu" , "nebula.png")).convert_alpha()
 nebulaPressed = picture.image.load(os.path.join("menu","nebulaPressed.png")).convert_alpha()
 terraLogo = picture.image.load(os.path.join("menu","terraLogo.png")).convert_alpha()
 terraLogoPressed = picture.image.load(os.path.join("menu","terraLogoPressed.png")).convert_alpha()
 solar_1 = picture.image.load(os.path.join("menu","logoSistem1.png")).convert_alpha()
 solar_1pressed = picture.image.load(os.path.join("menu","logoSistem1Pressed.png")).convert_alpha()
 solar_2 = picture.image.load(os.path.join("menu","logoSistem2.png")).convert_alpha()
 solar_2pressed = picture.image.load(os.path.join("menu","logoSistem2Pressed.png")).convert_alpha()
 milk1__ = picture.image.load(os.path.join("menu","logoWay.png")).convert_alpha()
 milk2__ =picture.image.load(os.path.join("menu","logoWay2.png")).convert_alpha()
 milk1Pressed__ = picture.image.load(os.path.join("menu","logoWayPressed.png")).convert_alpha()
 milk2Pressed__ = picture.image.load(os.path.join("menu","logoWay2Pressed.png")).convert_alpha()
 backgroundGame = picture.image.load(os.path.join("menu",'backgroundSecond.png'))
 stars = picture.image.load(os.path.join("menu","stars.png")).convert_alpha()
 evaluareUnpressed = picture.image.load(os.path.join("assets",'evaluare.png')).convert_alpha()
 evaluarePressed = picture.image.load(os.path.join("assets",'evaluare_P.png')).convert_alpha()
 lectieUnpressed = picture.image.load(os.path.join("assets",'lectie.png')).convert_alpha()
 LectiePressed = picture.image.load(os.path.join("assets",'lectie_P.png')).convert_alpha()
 explicatieUnpressed = picture.image.load(os.path.join("assets",'explicatie.png')).convert_alpha()
 explicatiePressed = picture.image.load(os.path.join("assets",'explicatie_P.png')).convert_alpha()
 tablou = picture.image.load(os.path.join("assets",'tablout.png')).convert_alpha()
 background = picture.image.load(os.path.join("menu",'background.png'))
 gameTitle = picture.image.load(os.path.join("menu","logo.png")).convert_alpha()
 sS = picture.image.load(os.path.join("assets",'inapoi.png')).convert_alpha()
 sS_P = picture.image.load(os.path.join("assets",'inapoi_P.png')).convert_alpha()
 dS = picture.image.load(os.path.join("assets",'inainte.png')).convert_alpha()
 dS_P = picture.image.load(os.path.join("assets",'inainte_P.png')).convert_alpha()
 fn = picture.image.load(os.path.join("assets",'finish.png')).convert_alpha()
 fn_P = picture.image.load(os.path.join("assets",'finish_P.png')).convert_alpha()
 butonApasat = picture.image.load(os.path.join("assets",'true_p.png')).convert_alpha()
 buton = picture.image.load(os.path.join("assets",'true.png')).convert_alpha()
 adevarat_P = picture.image.load(os.path.join("assets","adevarat_P.png")).convert_alpha()
 adevarat = picture.image.load(os.path.join("assets","adevarat.png")).convert_alpha()
 fals_P = picture.image.load(os.path.join("assets","fals_p.png")).convert_alpha()
 fals = picture.image.load(os.path.join("assets","fals.png")).convert_alpha()
 mainFont = os.path.join("menu",'textFont.otf')
 sliderPressed = picture.image.load(os.path.join("menu", "volumeSlidePressed.png")).convert_alpha()
 sliderUnpressed = picture.image.load(os.path.join("menu" , "volumeSlide.png")).convert_alpha()
 font = picture.font.Font(mainFont, 50)
 soundLogo = picture.image.load(os.path.join("menu","logoSunet.png")).convert_alpha()  
#Processes
#Reading Volume from file : last save
volumeSession = open(os.path.join("menu","volume.txt"))
lastVolume = 10
for x in volumeSession.read():
    lastVolume = ord(x)


class utils():
 #Screen Size
 screen_width = 1920
 screen_height = 1080
 monitor_screen = picture.display.set_mode((1920,1080))


 #Transforming from char to string
 lastVolume = lastVolume-48

 #Constants for button and frames position

 #Menu Buttons
 Buttonscreen_width_menu = screen_width/2-115
 Buttonscreen_height_menu = screen_height/9 + 190

 #Volume Slider Button
 Volume_x = 1920/2 - 200
 Volume_y = 400
 sliderDistance = 40
 volumeButton = []
 #In game logic handlers
 enteredInSettings = False
 enteredInGame = False
 screenPhase = 1
 runningSes = True
 mouseDown = False
 score = 0
 enableWriting = False
 doneWriting = False
 user_txt = ''
 earth = False
 solar_system = False
 galaxy = False
 explanation = False
 enteredInGame = False
 evaluation = 1
 questions = 1
 q = False
 eval = False    
 #Checks if the game has a last save
 sessionInfo = open(os.path.join("menu","sessions.txt"),"r")
 sesInfo = sessionInfo.read()
 sessionInfo.close()

 #Function that prints string on screen with custom limits
 def blit_text(surface, text, pos, font, color=picture.Color('black')):
    words = [word.split(' ') for word in text.splitlines()] 
    space = font.size(' ')[0]  
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0] 
                y += word_height 
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  
        y += word_height 


#Classes for Button And Frames
#The init functions of the classes have 4 arguments , first the positions we want to place the objects and how the
#object will look after a certain action

class Frame():
    def __init__(self , x , y , imagePressed):
        self.imagePressed = imagePressed
        self.rect = self.imagePressed.get_rect()
        self.rect.topleft = (x,y)

    def frameOnCursor(self):
        if self.rect.collidepoint(picture.mouse.get_pos()):
                return True
    def showFrame(self):
        utils.monitor_screen.blit(self.imagePressed , (self.rect.x , self.rect.y))

#Class for SoundSlider
class SoundButton():
    def __init__(self , x , y , image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    def buttonPressed(self):
        if self.rect.collidepoint(picture.mouse.get_pos()):
            if picture.mouse.get_pressed()[0]==1:
                return True
    def showButton(self):
        utils.monitor_screen.blit(self.image , (self.rect.x , self.rect.y))


class Button():
    def __init__(self , x , y , imagePressed,imageUnpressed):
        self.imagePressed = imagePressed
        self.imageUnpressed = imageUnpressed
        self.rect = self.imageUnpressed.get_rect()
        self.rect.topleft = (x,y)
    def buttonPressed(self):
       if picture.mouse.get_pressed()[0] and utils.mouseDown is True:
        if self.rect.collidepoint(picture.mouse.get_pos()):
                clickSound = picture.mixer.Sound(os.path.join("sounds","clickSound.mp3"))
                clickSound.set_volume(float(lastVolume)/10)
                clickSound.play()
                utils.mouseDown = False
                return True
    def buttonOnCursor(self):
        if self.rect.collidepoint(picture.mouse.get_pos()):
                return True

    def showButton(self):
        if Button.buttonOnCursor(self):
         utils.monitor_screen.blit(self.imagePressed , (self.rect.x , self.rect.y))
        elif Button.buttonPressed(self):
         utils.monitor_screen.blit(self.imagePressed,(self.rect.x+5,self.rect.y-5))
        else:
         utils.monitor_screen.blit(self.imageUnpressed,(self.rect.x,self.rect.y))

class TruthButton():
    def __init__(self , x , y , imageUnpressed , imagePressed,true):
        self.imagePressed = imagePressed
        self.imageUnpressed = imageUnpressed
        self.rect = self.imageUnpressed.get_rect()
        self.rect.topleft = (x,y)
        self.adevar = true
    def buttonPressed(self):
       if picture.mouse.get_pressed()[0] and utils.mouseDown is True:
        if self.rect.collidepoint(picture.mouse.get_pos()):
                clickSound = picture.mixer.Sound(os.path.join("sounds","clickSound.mp3"))
                clickSound.set_volume(float(lastVolume)/10)
                clickSound.play()
                return True
    def buttonOnCursor(self):
        if self.rect.collidepoint(picture.mouse.get_pos()):
                return True

    def showButton(self):
        if Button.buttonOnCursor(self):
         utils.monitor_screen.blit(self.imagePressed , (self.rect.x , self.rect.y))
        elif Button.buttonPressed(self):
         utils.monitor_screen.blit(self.imagePressed,(self.rect.x+5,self.rect.y-5))
        elif self.adevar and utils.user_txt =='Adevarat_':
            utils.monitor_screen.blit(self.imagePressed , (self.rect.x , self.rect.y))
        elif self.adevar is False and utils.user_txt =='Fals_':
            utils.monitor_screen.blit(self.imagePressed , (self.rect.x , self.rect.y))
        else:
         utils.monitor_screen.blit(self.imageUnpressed,(self.rect.x,self.rect.y))