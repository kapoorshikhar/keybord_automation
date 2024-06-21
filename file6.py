import pyautogui
import time

def position():     
    time.sleep(4)
    print(pyautogui.position())

# while True:
#     for i in range(10):
#         ex1=position()
#         print(i)
# position()

def leet():
    pyautogui.hotkey("win","d")
    pyautogui.hotkey("alt","space")
    pyautogui.typewrite("Brave")
    pyautogui.press("enter")
    time.sleep(5)
    pyautogui.click(21,19)
    time.sleep(5)
    pyautogui.click(1098,137)
    time.sleep(5)
    pyautogui.click(259,13)
    time.sleep(5)
    pyautogui.click(256,184)
    
leet()