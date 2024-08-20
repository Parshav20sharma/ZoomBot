import os
import win32com.client

def create_shortcut():
    # Create a shortcut to the application
    shortcut_path = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Zoom Bot.lnk')
    target_path = os.path.join(os.getcwd(), 'dist', 'zoom_automation_ui.exe')
    wDir_path = os.getcwd()
    icon_path = os.path.join(os.getcwd(), 'icon.ico')

    shell = win32com.client.Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.Targetpath = target_path
    shortcut.WorkingDirectory = wDir_path
    shortcut.IconLocation = icon_path
    shortcut.Save()

if __name__ == '__main__':
    create_shortcut()