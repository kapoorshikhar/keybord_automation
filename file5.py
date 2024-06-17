import pyautogui
import time 

def alarm():
    pyautogui.hotkey("win","d")
    pyautogui.hotkey("alt","space")
    pyautogui.typewrite("clock")
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.click(817,404)
    pyautogui.click(901,544)
    pyautogui.click(783,413)
    pyautogui.click(1021,505)
    pyautogui.click(894,559)
    pyautogui.click(1146,143)
    pyautogui.click(952,143)


def newalarm():
    pyautogui.hotkey("win","d")
    pyautogui.hotkey("alt","space")
    pyautogui.typewrite("clock")
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.click(778,411)
    pyautogui.click(1156,410)
    pyautogui.click(957,137)

def position():     
    time.sleep(4)
    print(pyautogui.position())

newalarm()
# while True:
#     for i in range(10):
#         ex1=position()
#         print(i)
# position()