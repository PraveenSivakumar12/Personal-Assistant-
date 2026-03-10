import datetime
import threading
import webbrowser
import os
import pyautogui
from ui import root, update_status, add_user_message, add_ai_message_typing, save_chat, start_ui
from voice import speak, listen
from ai_engine import ask_ai
from storage import save_conversation

# ================= COMMAND PROCESSOR =================

def handle_command(query):

    # -------- TIME --------
    if "time" in query:
        return datetime.datetime.now().strftime("The time is %H:%M:%S")

    # ---------- WINDOW CONTROL ----------
    elif "maximize" in query:
        pyautogui.hotkey("win","up")
        return "Window maximized"

    elif "minimize" in query:
        pyautogui.hotkey("win","down")
        return "Window minimized"

    elif "close window" in query:
        pyautogui.hotkey("alt","f4")
        return "Closing window"

    # -------- GOOGLE --------
    elif "open google" in query:
        webbrowser.open("https://www.google.com")
        return "Opening Google"

    # -------- YOUTUBE --------
    elif "open youtube" in query:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube"

    # -------- WHATSAPP --------
    elif "open whatsapp" in query:
        webbrowser.open("https://web.whatsapp.com")
        return "Opening WhatsApp"

    # -------- GMAIL --------
    elif "open gmail" in query or "open mail" in query:
        webbrowser.open("https://mail.google.com")
        return "Opening Gmail"

    # -------- CHATGPT --------
    elif "open chatgpt" in query:
        webbrowser.open("https://chat.openai.com")
        return "Opening ChatGPT"

    # -------- PLAY SONG --------
    elif "play song" in query or "play music" in query:
        song = query.replace("play song", "").replace("play music", "")
        webbrowser.open(f"https://www.youtube.com/results?search_query={song}")
        return f"Playing {song}"

    # -------- OPEN EXCEL --------
    elif "open excel" in query:
        os.system("start excel")
        return "Opening Microsoft Excel"

    # -------- OPEN WORD --------
    elif "open word" in query:
        os.system("start winword")
        return "Opening Microsoft Word"

    # -------- OPEN POWERPOINT --------
    elif "open powerpoint" in query:
        os.system("start powerpnt")
        return "Opening PowerPoint"

    # -------- OPEN CHROME --------
    elif "open chrome" in query:
        os.system("start chrome")
        return "Opening Chrome"

    # -------- OPEN FILE EXPLORER --------
    elif "open files" in query or "open file explorer" in query:
        os.system("explorer")
        return "Opening File Explorer"

     # ---------- OPEN FILE BY NAME ----------
    elif "open file" in query:

        filename = query.replace("open file","").strip()

        result = find_file(filename)

        if result:
            return f"Opening {result}"

        return "File not found"

    #-------ScreenShot---------
    elif "screenshot" in command:
        img = pyautogui.screenshot()
        img.save("screenshot.png")
        return "Screenshot taken"

    # -------- SHUTDOWN --------
    elif "shutdown computer" in query:
        os.system("shutdown /s /t 5")
        return "Shutting down computer"

    # -------- RESTART --------
    elif "restart computer" in query:
        os.system("shutdown /r /t 5")
        return "Restarting computer"

    #-------- Lock computer -----
    elif "lock computer" in query:
        os.system("rundll32.exe user32.dll,LockWorkStation")
        return "Locking computer"

    # ---------- SYSTEM MONITOR ----------
    elif "cpu usage" in query:

        cpu = psutil.cpu_percent(interval=1)

        return f"CPU usage is {cpu} percent"


    elif "battery status" in query:

        battery = psutil.sensors_battery()

        percent = battery.percent

        if battery.power_plugged:
            return f"Battery is {percent} percent and charging"

        else:
            return f"Battery is {percent} percent"


    # ---------- EMAIL ----------
    elif "send email" in query:

        sender = "yourgmail@gmail.com"
        password = "your_app_password"
        receiver = "receiver@gmail.com"

        msg = MIMEText("Hello from Jarvis")
        msg["Subject"] = "Message from Jarvis"
        msg["From"] = sender
        msg["To"] = receiver

        try:

            server = smtplib.SMTP("smtp.gmail.com",587)

            server.starttls()

            server.login(sender,password)

            server.sendmail(sender,receiver,msg.as_string())

            server.quit()

            return "Email sent successfully"

        except:
            return "Unable to send email"


    # -------- AI QUESTIONS --------
    else:
        return ask_ai(query)


# ================= VOICE PROCESS =================

def process_voice():

    update_status("Listening...")

    query = listen()

    if query == "none":
        update_status("Didn't understand")
        return

    add_user_message(query)

    reply = handle_command(query)

    add_ai_message_typing(reply)

    speak(reply)

    save_chat(query, reply)

    save_conversation(query, reply)


# ================= LOOP =================

def run_loop():

    threading.Thread(target=process_voice, daemon=True).start()

    root.after(3000, run_loop)


# ================= STARTUP GREETING =================

def startup():

    hour = datetime.datetime.now().hour

    if hour < 12:
        greeting = "Good Morning Boss"
    elif hour < 17:
        greeting = "Good Afternoon Boss"
    else:
        greeting = "Good Evening Boss"

    add_ai_message_typing(greeting)

    speak(greeting)




# ================= MAIN =================

if __name__ == "__main__":

    root.after(1000, startup)

    root.after(2000, run_loop)

    start_ui()