import pyautogui
import time
import subprocess
import os
import sys
from datetime import datetime

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def find_zoom_path():
    possible_paths = [
        os.path.join(os.getenv('USERPROFILE'), "AppData\\Roaming\\Zoom\\bin\\Zoom.exe"),
        "C:\\Program Files (x86)\\Zoom\\bin\\Zoom.exe",
        "C:\\Program Files\\Zoom\\bin\\Zoom.exe"
    ]
    for path in possible_paths:
        if os.path.exists(path):
            print(f"Found Zoom executable at: {path}")
            return path
    raise FileNotFoundError("Zoom executable not found. Please install Zoom or specify the correct path.")

def launch_zoom():
    zoom_path = find_zoom_path()
    if zoom_path:
        try:
            subprocess.Popen([zoom_path])
            print("Zoom application launched.")
            time.sleep(15)  # Increased wait time for Zoom to fully open
        except Exception as e:
            print(f"Failed to launch Zoom: {e}")
    else:
        print("Zoom executable not found!")

def check_checkbox(image_name):
    checkbox = pyautogui.locateCenterOnScreen(image_name)
    if checkbox:
        pyautogui.click(checkbox)
        print(f"Checkbox {image_name} clicked.")
        time.sleep(1)
    else:
        print(f"Checkbox {image_name} not found!")

def join_meeting(meeting_id, username, password, camera_status, mic_status, screenshot_status, recording_status, pause_recording_status, stop_recording_status):
    launch_zoom()  # Ensure Zoom is launched before proceeding

    print("Attempting to find and click the join button...")
    join_button_path = resource_path('join_button.png')
    join_button = pyautogui.locateCenterOnScreen(join_button_path)
    if join_button:
        pyautogui.click(join_button)
        print("Join button clicked.")
    else:
        print("Join button not found! Make sure the image is correctly placed.")
        return

    time.sleep(2)
    pyautogui.write(meeting_id)
    print(f"Meeting ID '{meeting_id}' entered.")
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)

    # Clear existing username and enter the new username
    pyautogui.hotkey('ctrl', 'a')  # Select all text
    pyautogui.press('delete')  # Delete selected text
    pyautogui.write(username)  # Enter the new username
    print(f"Username '{username}' entered.")
    time.sleep(1)

    # Handle checkboxes
    if camera_status:
        check_checkbox(resource_path('checkbox1.png'))  # Assuming this is for turning on the camera
    if mic_status:
        check_checkbox(resource_path('checkbox2.png'))  # Assuming this is for muting the microphone

    join_meeting_button_path = resource_path('join_meeting_button.png')
    join_meeting_button = pyautogui.locateCenterOnScreen(join_meeting_button_path)
    if join_meeting_button:
        pyautogui.click(join_meeting_button)
        print("Join meeting button clicked.")
    else:
        print("Join meeting button not found!")
        return

    time.sleep(15)  # Wait for 15 seconds before entering the passcode

    pyautogui.write(password)
    print(f"Password entered.")
    time.sleep(1)

    # Additional actions based on user selections
    time.sleep(20)  # Wait for the meeting to start and for the password to be processed

    focus_zoom_window()
    if camera_status:
        turn_on_camera()
    if screenshot_status:
        take_screenshot()
    if recording_status:
        start_recording()
    if pause_recording_status:
        pause_recording()
    if stop_recording_status:
        stop_recording()

    time.sleep(10)  # Wait before attempting to leave the meeting
    leave()

def focus_zoom_window():
    screen_width, screen_height = pyautogui.size()
    pyautogui.click(screen_width // 2, screen_height // 2)
    time.sleep(1)

def turn_on_camera():
    pyautogui.hotkey('alt', 'v')
    print("Alt+V pressed to turn on the camera.")
    time.sleep(10)  # Additional delay after turning on the camera

def start_recording():
    pyautogui.hotkey('alt', 'r')
    print("Alt+R pressed to start recording.")
    time.sleep(5)  # Short delay to ensure the recording command is processed

    # Handle the send request button after Alt+R is pressed
    send_request_button_path = resource_path('send_request.png')
    send_request_button = pyautogui.locateCenterOnScreen(send_request_button_path)
    if send_request_button:
        pyautogui.click(send_request_button)
        print("Send request button clicked.")
        time.sleep(2)  # Short delay to ensure the button click is processed
    else:
        print("Send request button not found!")

    # Send Alt+R again to resume recording
    pyautogui.hotkey('alt', 'r')
    print("Alt+R pressed again to resume recording.")
    time.sleep(5)  # Short delay to ensure the recording command is processed

def pause_recording():
    pyautogui.hotkey('alt', 'p')
    print("Alt+P pressed to pause recording.")
    time.sleep(5)  # Wait for 5 seconds to ensure the pause command is processed

def stop_recording():
    pyautogui.hotkey('alt', 'r')
    print("Alt+R pressed to stop recording.")
    time.sleep(5)  # Short delay to ensure the stop command is processed

def take_screenshot():
    screenshot_filename = os.path.join(os.path.expanduser('~'), 'Desktop', f'zoom_meeting_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png')
    pyautogui.screenshot(screenshot_filename)
    print(f"Screenshot saved as {screenshot_filename}")

def leave():
    pyautogui.hotkey('alt', 'q')
    print("Alt+Q pressed to leave the meeting.")
    time.sleep(5)  # Wait for 5 seconds before pressing Enter
    pyautogui.press('enter')  # Press Enter to confirm
    print("Enter pressed to confirm leaving.")
    time.sleep(10)  # Wait for 10 seconds before the meeting is left
