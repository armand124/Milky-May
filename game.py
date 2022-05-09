from menu import *
from declarations import *
from questions import Fact as info

#Function that handles the Back Button in Root Level and In-Game : logic and UI
@staticmethod
def backButtonGame(case):
    button = Button(0,0,GUI.fn_P , GUI.fn_P)
    if case=="Game":
     button = Button(30,utils.Buttonscreen_height_menu+600,GUI.backButtonPressed,GUI.backButtonUnpressed)
     if button.buttonPressed():
          utils.enteredInGame = False
    if case=="Game_In":
         button = Button(30,30,GUI.backButtonPressed,GUI.backButtonUnpressed)
         if button.buttonPressed():
           utils.enteredInGame = True
           utils.screenPhase = 2
    button.showButton()

#Function that handles the Back Button in Lesson Level : logic and UI
@staticmethod
def backButtonForGame():
    button = Button(30,900,GUI.backButtonPressed,GUI.backButtonUnpressed)
    if button.buttonPressed():
        utils.evaluation = 1
        utils.eval = False
    button.showButton()

#Function that handles the Back Button in Quiz Level : logic and UI
@staticmethod
def backButtonForQuestions():
    button = Button(30,900,GUI.backButtonPressed,GUI.backButtonUnpressed)
    if button.buttonPressed():
        utils.questions = 1
        utils.score = 1
        utils.q = False
    button.showButton()

#Function that handles the Back Button in Explain Level : logic and UI
@staticmethod
def explainButtonBack():
    button = Button(30,900,GUI.backButtonPressed,GUI.backButtonUnpressed)
    if button.buttonPressed():
        utils.explanation = False
    button.showButton()

#Root Level -> shows the levels possible and handles GUI and logic
@staticmethod
def rootLevel():
    utils.monitor_screen.blit(GUI.backgroundGame,(0,0))
    interactiveEarth = Button(120 , 300 ,GUI.earthImagePressed, GUI.earthImage)
    interactiveSolar = Button(780 , 100,GUI.solarPressed, GUI.solar)
    interactiveNebula = Button(1440 , 390 ,GUI.nebulaPressed, GUI.nebula)
    terra = Frame(20,120,GUI.terraLogo)
    __solar1 = Frame(650 , 500 , GUI.solar_1)
    __solar2 = Frame(650,660,GUI.solar_2)
    milk1 = Frame(1320,50,GUI.milk1__)
    milk2 = Frame(1320 ,210,GUI.milk2__)
    if interactiveEarth.buttonOnCursor():
        terra = Frame(20,120,GUI.terraLogoPressed)
    if interactiveEarth.buttonPressed():
        terra = Frame(20,120,GUI.terraLogoPressed)
        utils.screenPhase = 3
    if interactiveSolar.buttonOnCursor():
        __solar1 = Frame(660 , 490 , GUI.solar_1pressed)
        __solar2 = Frame(660,650,GUI.solar_2pressed)
    if interactiveSolar.buttonPressed():
        __solar1 = Frame(660 , 490 , GUI.solar_1pressed)
        __solar2 = Frame(660,650,GUI.solar_2pressed)
        utils.screenPhase = 4
    if interactiveNebula.buttonOnCursor():
        milk1= Frame(1330,40,GUI.milk1Pressed__)
        milk2= Frame(1330,200,GUI.milk2Pressed__)
    if interactiveNebula.buttonPressed():
        milk1= Frame(1330,40,GUI.milk1Pressed__)
        milk2= Frame(1330,200,GUI.milk2Pressed__)
        utils.screenPhase = 5
    __solar1.showFrame()
    __solar2.showFrame()
    terra.showFrame()
    milk1.showFrame()
    milk2.showFrame()
    interactiveNebula.showButton()
    interactiveSolar.showButton()
    interactiveEarth.showButton()

#Idle Screen on Specific level : logic and UI
@staticmethod
def level():
     utils.monitor_screen.blit(GUI.backgroundGame,(0,0))
     lectie = Button(400 , 540 , GUI.LectiePressed,GUI.lectieUnpressed)
     evaluare = Button(1200 , 540 ,GUI.evaluarePressed,GUI.evaluareUnpressed)
     if lectie.buttonPressed():
         utils.eval = True
     if evaluare.buttonPressed():
         utils.q = True
     lectie.showButton()
     evaluare.showButton()
     backButtonGame("Game_In")


#Lesson on specific level , shows the information and (if needed) explanation button that redirects to explanation realm
@staticmethod
def lesson(explanationCase,facts):
    utils.monitor_screen.blit(GUI.backgroundGame,(0,0))
    if utils.evaluation <= len(explanationCase):
      utils.monitor_screen.blit(GUI.tablou,(0,0))
      sageataDr = Button(1750,620,GUI.dS_P,GUI.dS)
      if sageataDr.buttonPressed():
        utils.evaluation = utils.evaluation + 1
      if utils.evaluation <= len(explanationCase):
       if explanationCase[utils.evaluation-1] is not "404":
        explicatie = Button(760+20,500,GUI.explicatiePressed,GUI.explicatieUnpressed)
        explicatie.showButton()
        if explicatie.buttonPressed():
         utils.explanation = True
       backButtonForGame()
       utils.blit_text(utils.monitor_screen,facts[utils.evaluation - 1],(20,20),GUI.font)    
       sageataDr.showButton() 
    if utils.evaluation == len(explanationCase) +1:
      finish = Button(780,500,GUI.fn_P,GUI.fn)
      if finish.buttonPressed():
          utils.eval = False
          utils.evaluation = 1
      finish.showButton()
    if utils.evaluation > 1:
      sageataSt = Button(30,620 , GUI.sS_P,GUI.sS)
      if sageataSt.buttonPressed():
        utils.evaluation = utils.evaluation - 1
      sageataSt.showButton()

#Explnation Realm shows information that is not considered clearly
@staticmethod
def explainRealm(x,explan):
    utils.monitor_screen.blit(GUI.backgroundGame,(0,0))
    utils.monitor_screen.blit(GUI.tablou,(0,0))
    utils.blit_text(utils.monitor_screen,explan[x],(20,20),GUI.font)
    explainButtonBack()


#Quiz Level
@staticmethod
def questioning(questionsCase , answearsMode,answears):
    utils.monitor_screen.blit(GUI.backgroundGame,(0,0))
    if utils.questions <= len(questionsCase):
      utils.monitor_screen.blit(GUI.tablou,(0,0))
      sageataDr = Button(1750,620,GUI.dS_P , GUI.dS)
      if sageataDr.buttonPressed():
         utils.doneWriting = False
         utils.user_txt = utils.user_txt[:-1]
         if utils.user_txt == answears[utils.questions-1]:
             utils.score = utils.score + 1
         utils.questions = utils.questions + 1
         utils.user_txt = ''
      if utils.questions != len(questionsCase) +1:
       backButtonForQuestions()
       sageataDr.showButton()
       printSolutions(utils.questions-1,answearsMode)
       utils.blit_text(utils.monitor_screen,questionsCase[utils.questions-1],(20,20),GUI.font)    
    if utils.questions == len(questionsCase) +1:
      final_score = GUI.font.render(str(utils.score),True , (255,255,255))
      utils.monitor_screen.blit(final_score,(810,340))
      finish = Button(780,500,GUI.fn_P,GUI.fn)
      if finish.buttonPressed():
          utils.user_txt = ''
          utils.score = 0
          utils.q = False
          utils.questions = 1
      finish.showButton()

#Function that handles the quiz system, verifies the possible cases of answearing and provides the interface and logic
@staticmethod          
def printSolutions(i , answearMode):
    if answearMode[i] == "Write":
        utils.enableWriting = True
        if utils.doneWriting:
            utils.enableWriting = False
        else:
         utils.monitor_screen.blit(GUI.buton,(800,540))
         writedText = GUI.font.render(utils.user_txt,True,(0,0,0))
         utils.monitor_screen.blit(writedText,(810,565))
    if answearMode[i] == "AF":
        truth = TruthButton(400,540,GUI.adevarat,GUI.adevarat_P,True)
        notTruth = TruthButton(1200,540,GUI.fals,GUI.fals_P,False)
        if truth.buttonPressed():
            utils.user_txt = 'Adevarat_'
        if notTruth.buttonPressed():
            utils.user_txt = 'Fals_'
        truth.showButton()
        notTruth.showButton()

class Game():
 #Main game function , handles the logic
 def runSpecificLevel():
    if utils.screenPhase == 2:
        rootLevel()
        backButtonGame("Game")       
    if utils.screenPhase >2 and utils.q is False and utils.eval is False:
        level()
    if utils.eval is True and utils.explanation is False:
      if utils.screenPhase == 3:
        lesson(info.explanationEarth,info.factsEarth)
      if utils.screenPhase == 4:
          lesson(info.explanationSolar , info.factsSolar)
      if utils.screenPhase == 5:
          lesson(info.explanationGalaxy,info.factsGalaxy)
    if utils.eval is True and utils.explanation is True:
       if utils.screenPhase == 3:
        explainRealm(utils.evaluation-1,info.explanationEarth)
       if utils.screenPhase == 4:
        explainRealm(utils.evaluation-1,info.explanationSolar)
       if utils.screenPhase == 5:
        explainRealm(utils.evaluation-1,info.explanationGalaxy)
    if utils.eval is False and utils.explanation is False and utils.q is True:
        if utils.screenPhase == 3:
            questioning(info.questionEarth,info.answearModeEarth,info.answearsEarth)
        if utils.screenPhase == 4:
            questioning(info.questionSolar,info.answearModeSolar,info.answearsSolar)
        if utils.screenPhase == 5:
            questioning(info.questionGalaxy,info.answearModeGalaxy,info.answearsGalaxy)
