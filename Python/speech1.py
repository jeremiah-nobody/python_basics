import pyttsx3
import speech_recognition as sr

en = pyttsx3.init()
en.say("What's Your name?")
en.runAndWait()

name = input("What's your name?")

en.say(f"Hello, {name}")

en.runAndWait()