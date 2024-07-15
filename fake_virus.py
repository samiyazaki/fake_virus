import tkinter as tk
from tkinter import messagebox
import time
import threading

def show_fake_virus():
    messages = [
        "Virus detected!",
        "Deleting all files...",
        "What? You don't have any files?",
        "Well, I'm deleting them anyway!",
        "Just kidding :)"
        "How about just the file with all your games?",
        "No, I'm just kidding again!",
        "I'm not doing anything.",
        "I'm just a harmless fake virus.",
        "But I'm a virus nonetheless!",
        "Why did you download me?",
    ]
    while True:
        time.sleep(5) #s Show message every 5 seconds
        message = messages[int(time.time()) % len(messages)]
        messagebox.showwarning("Virus Alert", message)

def start_fake_virus():
    threading.Thread(target=show_fake_virus, daemon=True).start()

def main():
    root = tk.Tk()
    root.title("Fake Virus")
    root.geometry("300x200")

    start_button = tk.Button(root, text="Start Fake Virus", command=start_fake_virus)
    start_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()