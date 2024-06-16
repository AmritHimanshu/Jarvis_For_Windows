import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0.9)

    try:
        print("Understanding.....")
        query = r.recognize_google(audio,language="en-in")
        print(f"You said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up lucifer" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep lucifer" in query:
                    speak("Ok sir, You can me call anytime")
                    break
                elif "hello" in query:
                    speak("Hello sir, how are you?")
                elif "i am fine" in query:
                    speak("That's great sir")
                elif "how r u" in query:
                    speak("Perfect sir")
                elif "thank" in query:
                    speak("You are welcome, sir")
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                elif "temperature" in query:
                    search = "temperature in bihar"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current {search} is {temp}")
                elif "weather" in query:
                    search = "weather in bihar"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    weather = data.find("div", class_ = "BNeawe").text
                    speak(f"current {search} is {weather}")
                
