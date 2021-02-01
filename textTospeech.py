# pip install pyttsx3
# pip install pywin32

import pyttsx3

txt = input("Text to Say :")
engine = pyttsx3.init()
engine.say(txt)
engine.runAndWait()
