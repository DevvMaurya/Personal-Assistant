import pyautogui
import time

def open_app(app_name):
    pyautogui.hotkey('win')
    time.sleep(0.5)
    pyautogui.typewrite(app_name)
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    if app_name == "camera":
        time.sleep(5)
        pyautogui.hotkey('enter')
    return "Opening " + app_name + "..."

def close_app():
    pyautogui.hotkey('alt', 'f4')
    return "Closing " + "App" + "..."

def write_text(text : str):
    time.sleep(5)
    pyautogui.typewrite(text+ ". ")
    return "Typing " + text + "..."

def app_size(size : str):
    # pyautogui.hotkey('alt', 'tab')
    # time.sleep(0.5)
    if "max" in size:
        pyautogui.hotkey('win', 'up')
        return "Maximizing the window..."
    elif "min" in size:
        pyautogui.hotkey('win', 'down')
        return "Minimizing the window..."


def press(key):

    match key:
        case "winG":
            pyautogui.hotkey('win', 'g')
            return "Pressing " + key
        case "winTab":
            pyautogui.hotkey('alt', 'tab')
            return "Pressing " + key
        case "winD":
            pyautogui.hotkey('win', 'd')
            return "Pressing " + key
        case "prtsc":
            pyautogui.hotkey('printscreen')
            return "Pressing " + key
        case "altf4":
            close_app()
            return "Pressing " + key
        
