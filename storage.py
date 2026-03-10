import datetime

CHAT_FILE = "chat_log.txt"


def save_conversation(user, ai):
    with open(CHAT_FILE, "a", encoding="utf-8") as f:
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{time}] USER: {user}\n")
        f.write(f"[{time}] JARVIS: {ai}\n\n")


def load_history():
    try:
        with open(CHAT_FILE, "r", encoding="utf-8") as f:
            return f.read()
    except:
        return "No history found."