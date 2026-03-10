import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source, timeout=5, phrase_time_limit=5)

        query = r.recognize_google(audio, language='en-in').lower()
        print("You said:", query)
        return query

    except sr.WaitTimeoutError:
        return "none"
    except sr.UnknownValueError:
        return "none"
    except sr.RequestError:
        print("Internet error")
        return "none"