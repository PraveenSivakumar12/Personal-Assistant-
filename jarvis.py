# ===================== IMPORTS =====================
from ui import root, update_status
import pyttsx3
import speech_recognition as sr
import datetime
import time
import os
import wikipedia
import pywhatkit
import pyautogui
import pyjokes

# ===================== GLOBAL FLAGS =====================

awake = False

# ===================== TEXT TO SPEECH =====================
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    update_status("Speaking...")
    engine.say(audio)
    engine.runAndWait()


# ===================== VOICE COMMAND FUNCTION =====================
def commands():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        update_status("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio = r.listen(source, timeout=6, phrase_time_limit=6)
        except:
            return "none"

    try:
        update_status("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        return query.lower()

    except:
        update_status("Didn't understand")
        return "none"


# ===================== WISHING FUNCTION =====================
def wishes():
    hour = int(datetime.datetime.now().hour)

    if hour < 12:
        speak("Good Morning Boss")
    elif hour < 17:
        speak("Good Afternoon Boss")
    elif hour < 21:
        speak("Good Evening Boss")
    else:
        speak("Good Night Boss")


# ===================== MAIN PROGRAM =====================
if __name__ == "__main__":

    root.after(100, lambda: None)
    wishes()

    while True:
        query = commands()

        if query == "none":
            continue

        # ---- WAKE MODE ----
        if not awake:
            update_status("Sleeping... Say 'Wake up'")
            if 'wake up' in query:
                awake = True
                speak("I am awake Boss")
                update_status("Awake... Waiting for command")
            continue


        #------- NOT AWAKE -----
        if not awake:
            update_status("Sleeping... Say 'Wake up'")
            if 'wake up' in query:
                awake = True
                speak("I am awake Boss")
                update_status("Awake... Waiting for command")
                time.sleep(0.5)   # 🔥 IMPORTANT
            continue


        # ---- SLEEP ----
        if 'sleep' in query:
            speak("Going to sleep Boss")
            awake = False
            update_status("Sleeping... Say 'Wake up'")
            continue

        # ---- TIME ----
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(strTime)

        # ---- OPEN FIREFOX ----
        elif 'open firefox' in query:
            speak("Opening Firefox sir")
            os.startfile(r"C:\Program Files\Mozilla Firefox\firefox.exe")

        # ---- WIKIPEDIA SEARCH ----
        elif 'wikipedia' in query:
            speak("Searching in Wikipedia")
            try:
                search = query.replace("wikipedia", "")
                results = wikipedia.summary(search, sentences=1)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except:
                speak("No results found")

        # ---- PLAY SONG ----
        elif 'play' in query:
            playQuery = query.replace('play', '')
            speak("Playing " + playQuery)
            pywhatkit.playonyt(playQuery)

        # ---- VOICE TYPING ----
        elif 'type' in query:
            speak("Please tell me what should I write")
            while True:
                typeQuery = commands()
                if typeQuery == "exit typing":
                    speak("Done Sir")
                    break
                else:
                    pyautogui.write(typeQuery + " ")

        # ---- OPEN WHATSAPP ----
        elif 'open whatsapp' in query:
            speak("Opening WhatsApp")
            os.startfile("https://web.whatsapp.com")

        # ---- OPEN WHATSAPP CHAT ----
        elif 'open chat with' in query:
            name = query.replace('open chat with', '').strip()
            speak(f"Opening chat with {name}")
            try:
                pywhatkit.sendwhatmsg_instantly(
                    phone_no=None,
                    message="",
                    wait_time=10,
                    tab_close=False,
                    close_time=3,
                    contact=name
                )
            except:
                speak("Contact not found or WhatsApp not ready")

        # ---- MINIMIZE WINDOW ----
        elif 'minimize' in query or 'minimise' in query:
            pyautogui.moveTo(1232, 15)
            pyautogui.leftClick()

        # ---- MAXIMIZE WINDOW ----
        elif 'maximize' in query or 'maximise' in query:
            pyautogui.hotkey('win', 'up')
            speak("Window maximized")

        # ---- OPEN MAIL ----
        elif 'open mail' in query or 'open gmail' in query:
            speak("Opening mail")
            os.startfile("https://mail.google.com")

        # ---- JOKE ----
        elif 'joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        # ---- EXIT ----
        elif 'exit' in query or 'quit' in query:
            speak("Goodbye Boss")
            break

