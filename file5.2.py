import pyautogui
import time

def newalarm():
    pyautogui.hotkey("win","d")
    pyautogui.hotkey("alt","space")
    pyautogui.typewrite("clock")
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.click(778,411)
    pyautogui.click(1156,410)
    pyautogui.click(957,137)
