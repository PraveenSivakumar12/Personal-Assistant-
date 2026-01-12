import tkinter as tk

root = tk.Tk()
root.title("JARVIS - Personal Assistant")
root.geometry("400x200")
root.resizable(False, False)

status_text = tk.StringVar()
status_text.set("Sleeping... Say 'Wake up'")

label = tk.Label(
    root,
    textvariable=status_text,
    font=("Arial", 14),
    fg="green"
)
label.pack(pady=70)

def update_status(text):
    status_text.set(text)
    root.update_idletasks()
    root.update()

