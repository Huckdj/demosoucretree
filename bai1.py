import tkinter as tk

def start_recording():
    status_label.config(text="Recording Started")

def pause_recording():
    status_label.config(text="Recording Paused")

def end_recording():
    status_label.config(text="Recording Ended")

# Create the main window
root = tk.Tk()
root.title("Frame Recorder")
root.geometry("600x300")
root.configure(bg='lightpink')

title_label = tk.Label(root, text="Frame Recorder", font=("Helvetica", 24), bg='pink')
title_label.pack(pady=20)

fps_frame = tk.Frame(root, bg='lightpink')
fps_frame.pack(pady=10)

fps_label = tk.Label(fps_frame, text="create an", font=("Helvetica", 14), bg='lightpink')
fps_label.pack(side=tk.LEFT)

fps_entry = tk.Entry(fps_frame, font=("Helvetica", 14), width=5)
fps_entry.pack(side=tk.LEFT, padx=5)

fps_label_end = tk.Label(fps_frame, text="fps video", font=("Helvetica", 14), bg='lightpink')
fps_label_end.pack(side=tk.LEFT)

button_frame = tk.Frame(root, bg='lightpink')
button_frame.pack(pady=10)

pause_button = tk.Button(button_frame, text="Pause", font=("Helvetica", 14), command=pause_recording)
pause_button.pack(side=tk.LEFT, padx=10)

start_button = tk.Button(button_frame, text="Start", font=("Helvetica", 14), command=start_recording)
start_button.pack(side=tk.LEFT, padx=10)

end_button = tk.Button(button_frame, text="End", font=("Helvetica", 14), command=end_recording)
end_button.pack(side=tk.LEFT, padx=10)

status_label = tk.Label(root, text="Recording Paused", font=("Helvetica", 14), bg='lightpink')
status_label.pack(pady=20)

root.mainloop()
