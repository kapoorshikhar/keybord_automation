import pyautogui
import time 

work =[]
def work_func():
    r = int(input("Enter the number of commands you want to enter: "))
    for n in range(r):
        i = input("Enter the command: {n}")
        work.append(i)
    print(work)
    for n in work:
        x=command(n)
def command(n):
    if n=="close":
        pyautogui.hotkey("alt","f4")
    if n == "position":
        time.sleep(4)
        print(pyautogui.position())
    if n == "al":
        pyautogui.hotkey("alt","space")
        pyautogui.typewrite("clock")
        pyautogui.press("enter")
        pyautogui.click(1333,322)
        pyautogui.click(1274,265)
    
        


pyautogui.FAILSAFE=False
ex =work_func()
