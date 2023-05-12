import tkinter as tk
import subprocess

root = tk.Tk()
root.geometry("300x200")

live_feed_icon = tk.PhotoImage(file="live_feed_icon.png")
upload_video_icon = tk.PhotoImage(file="upload_video_icon.png")

def run_live_feed():
    subprocess.run(["python", "main.py", "--mode", "live_feed"])

def run_upload_video():
    subprocess.run(["python", "main.py", "--mode", "upload_video"])

live_feed_button = tk.Button(root, image=live_feed_icon, text="Live Feed", command=run_live_feed)
live_feed_button.pack(pady=10)

upload_video_button = tk.Button(root, image=upload_video_icon, text="Upload Video", command=run_upload_video)
upload_video_button.pack(pady=10)

save_video_var = tk.BooleanVar()
save_video_checkbutton = tk.Checkbutton(root, text="Save Video?", variable=save_video_var)
save_video_checkbutton.pack(pady=10)

root.mainloop()
