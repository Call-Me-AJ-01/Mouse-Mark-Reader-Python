from pyautogui import hotkey
from time import sleep
from pygame import mixer
import pyperclip
import reg_
import pyttsx3 as r
engine = r.init()
engine.setProperty("rate",140)
from gtts import gTTS
import os
import shutil
from googletrans import Translator
import warnings
warnings.filterwarnings('ignore')

dic={"tamil":"ta","hindi":"hi","japanese":"ja","french":"fr","english":"en"}
i=1

while True:
    try: 
        shutil.rmtree("E:/AJ_Mark_II/Mouse Mark Reader/Tmp")
        break
    except:
        pass

while True:
    try:
        os.mkdir("E:/AJ_Mark_II/Mouse Mark Reader/Tmp")
        break
    except:
        pass
    
def speak(n):
    engine.say(n)
    engine.runAndWait()
    
while True:
    text=str(reg_.reg())
    #print(text)
    if text!="False":
        if "read" in text.lower():
            if text.lower()=="read this":
                hotkey('ctrl','c')
                speak("copied")
                speech=gTTS(text=pyperclip.paste(), lang="en", slow=False) 
                speech.save("E:/AJ_Mark_II/Mouse Mark Reader/Tmp/"+str(i)+".mp3")
                mixer.init(25100)
                mixer.music.load("E:/AJ_Mark_II/Mouse Mark Reader/Tmp/"+str(i)+".mp3")
                i+=1
                mixer.music.play()
            else:
                hotkey('ctrl','c')
                speak("copied")
                w,lang=text.lower().rsplit(" ",1)
                t=Translator(service_urls=["translate.google.com"])
                translation=t.translate(pyperclip.paste(),dest=dic[lang.strip().lower()])
                #print(translation.text)
                speech=gTTS(text=translation.text,lang=dic[lang.strip().lower()])
                speech.save("E:/AJ_Mark_II/Mouse Mark Reader/Tmp/"+str(i)+".mp3")
                mixer.init(25100)
                mixer.music.load("E:/AJ_Mark_II/Mouse Mark Reader/Tmp/"+str(i)+".mp3")
                i+=1
                mixer.music.play()
        elif "stop" in text:
            mixer.music.stop()
