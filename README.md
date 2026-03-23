🤖 JARVIS – Python Personal Assistant

JARVIS is a Voice Controlled Personal Assistant built using Python.
It can listen to voice commands, speak responses, open applications, search Wikipedia, play YouTube songs, type text, and control the system using voice.

This project also includes a simple Tkinter UI that shows the assistant status (Sleeping / Listening / Speaking / Awake).

🚀 Features
🎤 Voice Recognition using SpeechRecognition
🔊 Text to Speech using pyttsx3
🖥️ GUI using Tkinter
🌐 Wikipedia Search
🎵 Play YouTube Songs
💬 WhatsApp Web Open / Chat Open
⌨️ Voice Typing
😂 Tell Jokes
🕒 Tell Time
🌙 Sleep / Wake Mode
🪟 Window Control (Minimize / Maximize)
📧 Open Gmail
🌍 Open Firefox Browser
📁 Project Structure
PA_Project/
│
├── app.py      # Main assistant logic
|-- AI_engine.py     #Aiengine
├── ui.py       # UI window
|-- storaage.py   #cloudstorage
|-- voice.py   #voiceagent
├── README.md
⚙️ Requirements

Install Python packages before running.

pip install pyttsx3
pip install SpeechRecognition
pip install wikipedia
pip install pywhatkit
pip install pyautogui
pip install pyjokes
pip install pyaudio

If pyaudio fails:

pip install pipwin
pipwin install pyaudio
▶️ How to Run
python jarvis.py

Then say:

wake up
🎙️ Voice Commands
Command	Action
wake up	Activate assistant
sleep	Sleep mode
time	Tell time
open firefox	Open browser
wikipedia <topic>	Search Wikipedia
play <song>	Play song on YouTube
type	Voice typing
open whatsapp	Open WhatsApp Web
open chat with <name>	Open WhatsApp chat
open mail	Open Gmail
joke	Tell joke
minimize	Minimize window
maximize	Maximize window
exit	Close assistant
🖥️ UI Preview
Shows assistant status
Sleeping / Listening / Speaking / Awake

Built using Tkinter.

🧠 How it Works
Microphone listens for command
SpeechRecognition converts speech → text
Command processed
pyttsx3 speaks response
UI status updated
📌 Future Improvements
AI ChatGPT integration
Better UI dashboard
Face recognition
App launcher
System monitoring
Alarm / Reminder
Mobile control
👨‍💻 Author

Praveen S V
Python / AI / Personal Assistant Project
