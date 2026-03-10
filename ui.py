import tkinter as tk
from PIL import Image, ImageTk
import datetime
import os

# ================= ROOT WINDOW =================

root = tk.Tk()
root.title("NOVA AI SYSTEM")
root.geometry("1100x650")
root.configure(bg="black")
root.resizable(False, False)

# ================= CANVAS =================

canvas = tk.Canvas(root, width=1100, height=650, bg="black", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# ================= BACKGROUND =================

bg_image = None
image_path = "hud_background.jpg"

if os.path.exists(image_path):
    bg_raw = Image.open(image_path)
    bg_raw = bg_raw.resize((1100,650))
    bg_image = ImageTk.PhotoImage(bg_raw)
    canvas.create_image(0,0,image=bg_image,anchor="nw")

# ================= STATUS TEXT =================

status_text = tk.StringVar()
status_text.set("STATUS : IDLE")

status_label = tk.Label(
    root,
    textvariable=status_text,
    font=("Consolas",16),
    fg="cyan",
    bg="black"
)

canvas.create_window(550,30,window=status_label)

def update_status(text):
    status_text.set("STATUS : " + text)
    root.update_idletasks()

# ================= CLOCK =================

clock_text = tk.StringVar()

clock_label = tk.Label(
    root,
    textvariable=clock_text,
    font=("Consolas",14),
    fg="cyan",
    bg="black"
)

canvas.create_window(1000,30,window=clock_label)

def update_clock():
    now = datetime.datetime.now().strftime("%A  %H:%M:%S")
    clock_text.set(now)
    root.after(1000, update_clock)

update_clock()

# ================= CHAT HISTORY =================

chat_box = tk.Text(
    root,
    width=38,
    height=28,
    bg="black",
    fg="cyan",
    font=("Consolas",10),
    bd=0
)

canvas.create_window(170,350,window=chat_box)

def add_user_message(msg):
    chat_box.insert(tk.END,"\nYOU : "+msg+"\n")
    chat_box.see(tk.END)

def add_ai_message_typing(msg):
    chat_box.insert(tk.END,"NOVA : "+msg+"\n")
    chat_box.see(tk.END)

# ================= AI CORE ANIMATION =================

core_radius = 60
pulse = 0
pulse_dir = 1

def animate_core():

    global pulse, pulse_dir

    canvas.delete("core")

    r = core_radius + pulse

    canvas.create_oval(
        550-r,320-r,
        550+r,320+r,
        outline="cyan",
        width=3,
        tags="core"
    )

    pulse += pulse_dir

    if pulse > 12 or pulse < -3:
        pulse_dir *= -1

    root.after(40, animate_core)

animate_core()

# ================= VOICE WAVE ANIMATION =================

wave_height = 0
wave_dir = 1

def animate_wave():

    global wave_height, wave_dir

    canvas.delete("wave")

    for i in range(5):

        h = wave_height + (i*3)

        canvas.create_line(
            530+i*10,380,
            530+i*10,380-h,
            fill="cyan",
            width=3,
            tags="wave"
        )

    wave_height += wave_dir

    if wave_height > 25 or wave_height < 2:
        wave_dir *= -1

    root.after(60, animate_wave)

animate_wave()

# ================= SAVE CHAT =================

def save_chat(user, ai):
    pass

# ================= START UI =================

def start_ui():
    root.mainloop()