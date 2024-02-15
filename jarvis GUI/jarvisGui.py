from JARVISUI import Ui_JarvisUI
from PyQt5 import QtCore , QtWidgets , QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType   #for talking


import pyttsx3
import speech_recognition as sr
import webbrowser
from pywikihow import search_wikihow
from bs4 import BeautifulSoup
import pywhatkit
import wikipedia
from googletrans import Translator
import os
import pyautogui
import psutil
from tkinter import Label
from tkinter import Entry
from tkinter import Button
import requests
from tkinter import Tk
from gtts import gTTS
from tkinter import StringVar
import PyPDF2
from pytube import YouTube
import datetime
from playsound import playsound
import keyboard
import pyjokes
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',170)

def Speak(Audio):
        print("   ")
        print(f": {Audio}")
        engine.say(Audio)
        print("    ")
        engine.runAndWait()


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()


    def run(self):          #For calling ourself
        self.TaskExe()

    def takecommand(self): 
        r = sr.Recognizer()
        # with sr.Microphone() as source:
        #     print("          ")
        #     print("Listening...")
        #     r.pause_threshold = 1
        #     audio = r.listen(source)
        with sr.Microphone(device_index=1) as source:
            print("          ")
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source,timeout=5,phrase_time_limit=5)

        try:
            print("Recognizing...")    
            self.query = r.recognize_google(audio, language='en-in')
            print(f"Your Command :  {self.query}\n")

        except:   
            return "None"
            
        return self.query.lower()

    def TaskExe(self):
        Speak("Hello,I am Jimmy ")

        def Music():
            Speak("Which language do you want to listen?")
            languageName =self.takecommand()

            if 'hindi' in languageName:
                # os.startfile('E:\\Music\\Hindi')
                music_dir = 'D:\\Music\\Hindi'
                songs = os.listdir(music_dir)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))

                
            #     elif 'play music' in query:
            # music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            # songs = os.listdir(music_dir)
            # print(songs)    
            # os.startfile(os.path.join(music_dir, songs[0]))
            
            # elif 'play music' in query:
            # music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            # songs = os.listdir(music_dir)
            # print(songs)    
            # os.startfile(os.path.join(music_dir, songs[0]))

            elif 'marathi' in languageName:
                #os.startfile('E:\\Music\\Marathi')
                music_dir = 'D:\\Music\\Marathi'
                songs = os.listdir(music_dir)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))
            
            elif 'english' in languageName:
                #os.startfile('E:\\Music\\English')
                music_dir = 'D:\\Music\\English'
                songs = os.listdir(music_dir)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))

            # else:
            #     pywhatkit.playonyt(musicName)

            Speak("Your Song Has Been Started! , Enjoy Mam!")

        def OpenApps():
            Speak("Ok Mam , Wait A Second!")
            
            if 'code' in self.query:
                os.startfile("C:\\Users\\sj386\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")     #C:\Users\HP\AppData\Local\Programs\Microsoft VS Code\\code.exe
                #os.startfile("C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe")     #C:\Users\HP\AppData\Local\Programs\Microsoft VS Code\\code.exe

            # elif 'telegram' in self.query:
            #     os.startfile("E:\\Applications\\Telegram Desktop\\Telegram Desktop\\Telegram.exe")

            elif 'chrome' in self.query:
                os.startfile("C:\\Program Files\\Google\Chrome\\Application\\chrome.exe")
                # os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")   #C:\Program Files (x86)\Google\Chrome\Application
                
            
            # elif 'facebook' in self.query:
            #     webbrowser.open('https://www.facebook.com/')

            # elif 'instagram' in self.query:
            #     webbrowser.open('https://www.instagram.com/')

            elif 'maps' in self.query:
                webbrowser.open('https://www.google.com/maps/@28.7091225,77.2749958,15z')

            elif 'youtube' in self.query:
                webbrowser.open('https://www.youtube.com')

            Speak("Your Command Has Been Completed Mam!")

        def Temp():
            search = "temperature in Maharashtra"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temperature = data.find("div",class_ = "BNeawe").text
            Speak(f"The Temperature Outside Is {temperature} celcius")

            Speak("Do I Have To Tell You Another Place Temperature ?")
            next = self.takecommand()

            if 'yes' in next:
                Speak("Tell Me The Name Of tHE Place ")
                name = self.takecommand()
                search = f"temperature in {name}"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temperature = data.find("div",class_ = "BNeawe").text
                Speak(f"The Temperature in {name} is {temperature} celcius")

            else:
                Speak("no problem Mam")

        def Reader():
            Speak("Tell Me The Name Of The Book!")

            name = self.takecommand()

            if 'india' in name:

                os.startfile('E:\\Kaushik Shresth\\Books\\Social Science\\History\\ch 1.pdf')
                book = open('E:\\Kaushik Shresth\\Books\\Social Science\\History\\ch 1.pdf','rb')
                pdfreader = PyPDF2.PdfFileReader(book)
                pages = pdfreader.getNumPages()
                Speak(f"Number Of Pages In This Books Are {pages}")
                Speak("From Which Page I Have To Start Reading ?")
                numPage = int(input("Enter The Page Number :"))
                page = pdfreader.getPage(numPage)
                text = page.extractText()
                Speak("In Which Language , I Have To Read ?")
                lang = self.takecommand()

                if 'hindi' in lang:
                    transl = Translator()
                    textHin = transl.translate(text,'hi')
                    textm = textHin.text
                    speech = gTTS(text = textm )
                    try:
                        speech.save('book.mp3')
                        playsound('book.mp3')

                    except:
                        playsound('book.mp3')

                else:
                    Speak(text)

            elif 'europe' in name:
                os.startfile('E:\\Kaushik Shresth\\Books\\Social Science\\History\\ch 3.pdf')
                book = open('E:\\Kaushik Shresth\\Books\\Social Science\\History\\ch 3.pdf','rb')
                pdfreader = PyPDF2.PdfFileReader(book)
                pages = pdfreader.getNumPages()
                Speak(f"Number Of Pages In This Books Are {pages}")
                Speak("From Which Page I Have To Start Reading ?")
                numPage = int(input())
                page = pdfreader.getPage(numPage)
                text = page.extractText()
                Speak("In Which Language , I Have To Read ?")
                lang = self.takecommand()

                if 'hindi' in lang:
                    transl = Translator()
                    textHin = transl.translate(text,'hi')
                    textm = textHin.text
                    speech = gTTS(text = textm )
                    try:

                        speech.save('book.mp3')
                        playsound('book.mp3')

                    except:
                        playsound('book.mp3')

                else:
                    Speak(text)

        def CloseAPPS():
            Speak("Ok Mam , Wait A second!")

            if 'youtube' in self.query:
                os.system("TASKKILL /F /im Chrome.exe")

            elif 'chrome' in self.query:
                os.system("TASKKILL /f /im Chrome.exe")

            # elif 'telegram' in self.query:
            #     os.system("TASKKILL /F /im Telegram.exe")

            elif 'code' in self.query:
                os.system("TASKKILL /F /im code.exe")

            # elif 'instagram' in self.query:
            #     os.system("TASKKILL /F /im chrome.exe")
                
            Speak("Your Command Has Been Succesfully Completed!")

        def YoutubeAuto():
            Speak("Whats Your Command ?")
            comm = self.takecommand()

            if 'pause' in comm:
                keyboard.press('space bar')

            elif 'restart' in comm:
                keyboard.press('0')

            elif 'mute' in comm:
                keyboard.press('m')

            elif 'skip' in comm:
                keyboard.press('l')

            elif 'back' in comm:
                keyboard.press('j')

            elif 'full screen' in comm:
                keyboard.press('f')

            elif 'film mode' in comm:
                keyboard.press('t')

            Speak("Done Mam")

        def TakeHindi():
            command = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening......")
                command.pause_threshold = 1
                audio = command.listen(source)

                try:
                    print("Recognizing.....")
                    self.query = command.recognize_google(audio,language='hi')
                    print(f"You Said : {self.query}")

                except:
                    return "none"

                return self.query.lower()

        def Tran():
            Speak("Tell Me The Line!")
            line = TakeHindi()
            traslate = Translator()
            result = traslate.translate(line)
            Text = result.text
            Speak(Text)
            
        def ChromeAuto():
            Speak("Chrome Automation started!")

            command = self.takecommand()

            if 'close this tab' in command:
                keyboard.press_and_release('ctrl + w')

            elif 'open new tab' in command:
                keyboard.press_and_release('ctrl + t')

            elif 'open new window' in command:
                keyboard.press_and_release('ctrl + n')

            elif 'history' in command:
                keyboard.press_and_release('ctrl +h')

        def screenshot():
            Speak("Ok Boss , What Should I Name That File ?")
            path = self.takecommand()
            path1name = path + ".png"
            # path1 = "E:\\Kaushik Shresth\\Screenshots\\"+ path1name
            path1 = "C:\\Users\\HP\\Pictures\\Screenshots\\"+ path1name
            kk = pyautogui.screenshot()
            kk.save(path1)
            # os.startfile("E:\\Kaushik Shresth\\Screenshots")
            os.startfile("C:\\Users\\HP\\Pictures\\Screenshots")
            Speak("Here Is Your ScreenShot") 

        while True:

            self.query = self.takecommand()

            if 'hello' in self.query:
                Speak("Hello Mam , I Am Jimmy .")
                Speak("Your Personal AI Assistant!")
                Speak("How May I Help You?")

            elif 'how are you' in self.query:
                Speak("I Am Fine Mam!")
                Speak("Whats About YOU?")

            elif 'you need a break' in self.query:
                Speak("Ok Mam , You Can Call Me Anytime !")
                Speak("Just Say Wake Up Jimmy!")
                break

            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                Speak(f"Sir, the time is {strTime}")

            elif 'youtube search' in self.query:
                Speak("OK Mam , This Is What I found For Your Search!")
                self.query = self.query.replace("Jimmy","")
                self.query = self.query.replace("youtube search","")
                web = 'https://www.youtube.com/results?search_self.query=' + self.query
                webbrowser.open(web)
                Speak("Done Mam!")

            elif 'website' in self.query:
                Speak("Ok Mam , Launching.....")
                self.query = self.query.replace("Jimmy","")
                self.query = self.query.replace("website","")
                self.query = self.query.replace(" ","")
                web1 = self.query.replace("open","")
                web2 = 'https://www.' + web1 + '.com'
                webbrowser.open(web2)
                Speak("Launched!")

            elif 'launch' in self.query:
                Speak("Tell Me The Name Of The Website!")
                name = self.takecommand()
                web = 'https://www.' + name + '.com'
                webbrowser.open(web)
                Speak("Done Mam!")

            elif 'wikipedia' in self.query:
                Speak("Searching Wikipedia.....")
                self.query = self.query.replace("Jimmy","")
                self.query = self.query.replace("wikipedia","")
                wiki = wikipedia.summary(self.query,2)
                Speak(f"According To Wikipedia : {wiki}")

            elif 'screenshot' in self.query:
                screenshot()

            # elif 'open facebook' in self.query:
            #     OpenApps()

            # elif 'open instagram' in self.query:
            #     OpenApps()

            elif 'open maps' in self.query:
                OpenApps()

            elif 'open code' in self.query:
                OpenApps()

            elif 'open youtube' in self.query:
                OpenApps()
                
            elif 'open telegram' in self.query:
                OpenApps()

            elif 'open chrome' in self.query:
                OpenApps()

            elif 'close chrome' in self.query:
                CloseAPPS()

            elif 'music' in self.query:
                Music()

            # elif 'close telegram' in self.query:
            #     CloseAPPS()

            # elif 'close instagram' in self.query:
            #     CloseAPPS()

            # elif 'close facebook' in self.query:
            #     CloseAPPS()

            elif 'pause' in self.query:
                keyboard.press('space bar')

            elif 'restart' in self.query:
                keyboard.press('0')

            elif 'mute' in self.query:
                keyboard.press('m')

            elif 'skip' in self.query:
                keyboard.press('l')

            elif 'back' in self.query:
                keyboard.press('j')

            elif 'full screen' in self.query:
                keyboard.press('f')

            elif 'film mode' in self.query:
                keyboard.press('t')

            elif 'youtube tool' in self.query:
                YoutubeAuto()

            elif 'close the tab' in self.query:
                keyboard.press_and_release('ctrl + w')

            elif 'open new tab' in self.query:
                keyboard.press_and_release('ctrl + t')

            elif 'open new window' in self.query:
                keyboard.press_and_release('ctrl + n')

            elif 'history' in self.query:
                keyboard.press_and_release('ctrl +h')

            elif 'chrome automation' in self.query:
                ChromeAuto()

            elif 'joke' in self.query:
                get = pyjokes.get_joke()
                Speak(get)

            elif 'repeat my word' in self.query:
                Speak("Speak Mam!")
                jj = self.takecommand()
                Speak(f"You Said : {jj}")

            elif 'location' in self.query:
                Speak("Ok Mam , Wait A Second!")
                webbrowser.open('https://www.google.com/maps/@28.7091225,77.2749958,15z')

            elif 'alarm' in self.query:
                Speak("Enter The Time !")
                time = input(": Enter The Time :")

                while True:
                    Time_Ac = datetime.datetime.now()
                    now = Time_Ac.strftime("%H:%M:%S")

                    if now == time:
                        Speak("Time To Wake Up Mam!")
                        playsound('iron.mp3')
                        Speak("Alarm Closed!")

                    elif now>time:
                        break

            # elif 'video downloader' in self.query:
            #     root = Tk()
            #     root.geometry('500x300')
            #     root.resizable(0,0)
            #     root.title("Youtube Video Downloader")
            #     Speak("Enter Video Url Here !")
            #     Label(root,text = "Youtube Video Downloader",font = 'arial 15 bold').pack()
            #     link = StringVar()
            #     Label(root,text = "Paste Yt Video URL Here",font = 'arial 15 bold').place(x=160,y=60)
            #     Entry(root,width = 70,textvariable = link).place(x=32,y=90)

            #     def VideoDownloader():
            #         url = YouTube(str(link.get()))
            #         video = url.streams.first()
            #         video.download()
            #         Label(root,text = "Downloaded",font = 'arial 15').place(x= 180,y=210)

            #     Button(root,text = "Download",font = 'arial 15 bold',bg = 'pale violet red',padx = 2 , command = VideoDownloader).place(x=180,y=150)

            #     root.mainloop()
            #     Speak("Video Downloaded")
                
            elif 'translator' in self.query:
                Tran()
            
            elif 'remember that' in self.query:
                remeberMsg = self.query.replace("remember that","")
                remeberMsg = remeberMsg.replace("Jimmy","")
                Speak("You Tell Me To Remind You That :"+remeberMsg)
                remeber = open('data.txt','w')
                remeber.write(remeberMsg)
                remeber.close()

            elif 'what do you remember' in self.query:      #error
                remeber = open('data.txt','r')
                Speak("You Tell Me That" + remeber.read())

            elif 'google search' in self.query:
                import wikipedia as googleScrap
                self.query = self.query.replace("Jimmy","")
                self.query = self.query.replace("google search","")
                self.query = self.query.replace("google","")
                Speak("This Is What I Found On The Web!")
                pywhatkit.search(self.query)

                try:
                    result = googleScrap.summary(self.query,2)
                    Speak(result)

                except:
                    Speak("No Speakable Data Available!")

            elif 'how to' in self.query:
                Speak("Getting Data From The Internet !")
                op = self.query.replace("Jimmy","")
                max_result = 1
                how_to_func = search_wikihow(op,max_result)
                assert len(how_to_func) == 1
                how_to_func[0].print()
                Speak(how_to_func[0].summary)
                
            elif 'temperature' in self.query:
                Temp()

            elif 'read book' in self.query:
                Reader()
            elif 'take hindi' in self.query:
                TakeHindi()
            else:
                # Speak("I do not get you mam,Please speak again")
                print("tell me something")

# TaskExe()

startFunctions = MainThread()

class Gui_Start(QMainWindow):


    def __init__(self):
        super().__init__()
        self.Jimmy_ui = Ui_JarvisUI()
        self.Jimmy_ui.setupUi(self)

        self.Jimmy_ui.pushButton.clicked.connect(self.startFunc)
        self.Jimmy_ui.pushButton_2.clicked.connect(self.close)

    def startFunc(self):

        self.Jimmy_ui.movies_2 = QtGui.QMovie("Iron_Template_1.gif")      
        self.Jimmy_ui.label_2.setMovie(self.Jimmy_ui.movies_2)      
        self.Jimmy_ui.movies_2.start()


        self.Jimmy_ui.movies_3 = QtGui.QMovie("__1.gif")      
        self.Jimmy_ui.label_3.setMovie(self.Jimmy_ui.movies_3)      
        self.Jimmy_ui.movies_3.start()


        self.Jimmy_ui.movies_4 = QtGui.QMovie("initial.gif")      
        self.Jimmy_ui.label_4.setMovie(self.Jimmy_ui.movies_4)      
        self.Jimmy_ui.movies_4.start()


        self.Jimmy_ui.movies_5 = QtGui.QMovie("Health_Template.gif")      
        self.Jimmy_ui.label_5.setMovie(self.Jimmy_ui.movies_5)      
        self.Jimmy_ui.movies_5.start()


        self.Jimmy_ui.movies_6 = QtGui.QMovie("B.G_Template_1.gif")      
        self.Jimmy_ui.label_6.setMovie(self.Jimmy_ui.movies_6)      
        self.Jimmy_ui.movies_6.start()

        startFunctions.start()


Gui_App = QApplication(sys.argv)
Gui_Jarvis = Gui_Start()
Gui_Jarvis.show()
exit(Gui_App.exec_())