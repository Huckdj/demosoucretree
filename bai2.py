import tkinter as tk
from tkinter import messagebox

def scan_now():
    messagebox.showinfo("Scan", "Scan Now clicked")

def quick_scan():
    status_label.config(text="Quick Scan")

def web_protection():
    status_label.config(text="Web Protection")

def quarantine():
    status_label.config(text="Quarantine")

def full_scan():
    status_label.config(text="Full Scan")

def simple_update():
    status_label.config(text="Simple Update")

root = tk.Tk()
root.title("AtarBals Modern Antivirus")
root.geometry("800x500")

sidebar = tk.Frame(root, bg='blue', width=200)
sidebar.pack(side=tk.LEFT, fill=tk.Y)

sections = ["Status", "Updates", "Settings", "Share Feedback", "Buy Premium", "Help"]
labels=tk.Label(sidebar, text="AtarBals AntiVirus", font=("Helvetica", 20), bg='blue', fg='white')
labels.pack(pady=10, padx=20, anchor='w')
for section in sections:
    section_label = tk.Label(sidebar, text=section, font=("Helvetica", 14), bg='blue', fg='white')
    section_label.pack(pady=10, padx=20, anchor='w')


scan_now_button = tk.Button(sidebar, text="Scan Now", font=("Helvetica", 14), bg='green', fg='white', command=scan_now)
scan_now_button.pack(pady=20, padx=20, anchor='w')

main_content = tk.Frame(root, bg='white')
main_content.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

title_label = tk.Label(main_content, text="Scan", font=("Helvetica", 24), bg='white')
title_label.pack(pady=20)

subtitle_label = tk.Label(main_content, text="Premium will be free forever. You just need to click button.", font=("Helvetica", 14), bg='white')
subtitle_label.pack(pady=10)

button_frame = tk.Frame(main_content, bg='white')
button_frame.pack(pady=20)

quick_scan_button = tk.Button(button_frame, text="Quick Scan", font=("Helvetica", 14), bg='magenta', command=quick_scan)
quick_scan_button.grid(row=0, column=0, padx=20, pady=10)

web_protection_button = tk.Button(button_frame, text="Web Protection", font=("Helvetica", 14), bg='magenta', command=web_protection)
web_protection_button.grid(row=0, column=1, padx=20, pady=10)

quarantine_button = tk.Button(button_frame, text="Quarantine", font=("Helvetica", 14), bg='magenta', command=quarantine)
quarantine_button.grid(row=1, column=0, padx=20, pady=10)

full_scan_button = tk.Button(button_frame, text="Full Scan", font=("Helvetica", 14), bg='magenta', command=full_scan)
full_scan_button.grid(row=1, column=1, padx=20, pady=10)

simple_update_button = tk.Button(button_frame, text="Simple Update", font=("Helvetica", 14), bg='magenta', command=simple_update)
simple_update_button.grid(row=2, column=0, columnspan=2, pady=10)

status_label = tk.Label(main_content, text="Get Premium to Enable: {Web Protection}, {Full Scan}, {Simple Update}", font=("Helvetica", 14), bg='white', fg='magenta')
status_label.pack(pady=20)

root.mainloop()
