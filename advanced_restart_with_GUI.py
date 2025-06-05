import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Progressbar
import os
import time
import threading

def countdown_and_restart(seconds):
    for i in range(seconds, 0, -1):
        countdown_label.config(text=f"Restarting in {i} seconds....")
        progress["value"]=((secnds - i + 1)/seconds) * 100
        window.update_idletasks()
        time.sleep(1)
    os.system("shutdown /r /t 1")
def confirm_restart():
    try:
        seconds = int(entry.get())
        if seconds <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive number.")
        return 
answer = messagebox.askyesno("Confirm REstart", f"Restart in {seconds} seconds?")
if answer:
    