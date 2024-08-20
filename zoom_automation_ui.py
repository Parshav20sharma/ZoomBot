import tkinter as tk
import zoom_automation  # Make sure this imports correctly

def start_automation():
    meeting_id = meeting_id_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    camera_status = camera_var.get()
    mic_status = mic_var.get()
    screenshot_status = screenshot_var.get()
    recording_status = recording_var.get()
    pause_recording_status = pause_recording_var.get()
    stop_recording_status = stop_recording_var.get()

    zoom_automation.join_meeting(
        meeting_id=meeting_id,
        username=username,
        password=password,
        camera_status=camera_status,
        mic_status=mic_status,
        screenshot_status=screenshot_status,
        recording_status=recording_status,
        pause_recording_status=pause_recording_status,
        stop_recording_status=stop_recording_status
    )

root = tk.Tk()
root.title("Zoom Automation")

tk.Label(root, text="Meeting ID:").grid(row=0)
tk.Label(root, text="Username:").grid(row=1)
tk.Label(root, text="Password:").grid(row=2)

meeting_id_entry = tk.Entry(root)
username_entry = tk.Entry(root)
password_entry = tk.Entry(root)

meeting_id_entry.grid(row=0, column=1)
username_entry.grid(row=1, column=1)
password_entry.grid(row=2, column=1)

camera_var = tk.BooleanVar()
mic_var = tk.BooleanVar()
screenshot_var = tk.BooleanVar()
recording_var = tk.BooleanVar()
pause_recording_var = tk.BooleanVar()
stop_recording_var = tk.BooleanVar()

tk.Checkbutton(root, text="Turn On Camera", variable=camera_var).grid(row=3, columnspan=2)
tk.Checkbutton(root, text="Mute Microphone", variable=mic_var).grid(row=4, columnspan=2)
tk.Checkbutton(root, text="Take Screenshot", variable=screenshot_var).grid(row=5, columnspan=2)
tk.Checkbutton(root, text="Start Recording", variable=recording_var).grid(row=6, columnspan=2)
tk.Checkbutton(root, text="Pause Recording", variable=pause_recording_var).grid(row=7, columnspan=2)
tk.Checkbutton(root, text="Stop Recording", variable=stop_recording_var).grid(row=8, columnspan=2)

tk.Button(root, text="Start", command=start_automation).grid(row=9, columnspan=2)

root.mainloop()
