import pyttsx3
import speech_recognition as sr
from googlesearch import search

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',180)

def Speak(Audio):
        print("   ")
        print(f": {Audio}")
        engine.say(Audio)
        print("    ")
        engine.runAndWait()


def Takecommand(): 
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            queryHindi = r.recognize_google(audio, language='hi')
            print(f"Your Command :  {queryHindi}\n")

        except:   
            return "None"
            
        return queryHindi.lower()

#query = Takecommand()
#print("query")

def TaskExe():
        while True:

                queryHindi= Takecommand()

                if 'हेलो' in queryHindi:
                        Speak("हेलो आप कैसे हैं?")
                elif 'आप कैसे हैं?' in queryHindi:
                        Speak("मैं ठीक हूँ मैम")

TaskExe()
#takecommand()  
#print(takecommand()) 
#Speak("नमस्ते")