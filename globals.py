import tkinter as tk
from tkinter import messagebox

file_path = None


#ERROR POPUP MSG
def show_popup_message(message):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showinfo("ERROR", message)