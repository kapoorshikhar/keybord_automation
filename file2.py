import pyautogui
import time

time.sleep(5)
# print(pyautogui.position())

pyautogui.moveTo(213,17) 
pyautogui.click()
pyautogui.hotkey("ctrl","c")
pyautogui.moveTo(1252,179) 
pyautogui.click()
pyautogui.hotkey("ctrl","v")
pyautogui.press("enter")

print (" first part executed")

pyautogui.moveTo(299,16) 
pyautogui.click()
pyautogui.hotkey("ctrl","c")
pyautogui.moveTo(1252,179) 
pyautogui.click()
pyautogui.hotkey("ctrl","v")
pyautogui.press("enter")


print ("Second part executed")

pyautogui.moveTo(398,16) 
pyautogui.click()
pyautogui.hotkey("ctrl","c")
pyautogui.moveTo(1252,179) 
pyautogui.click()
pyautogui.hotkey("ctrl","v")
pyautogui.press("enter")

print ("Third part executed")

pyautogui.moveTo(453,16)
pyautogui.click()
pyautogui.hotkey("ctrl","c")
pyautogui.moveTo(1252,179) 
pyautogui.click()
pyautogui.hotkey("ctrl","v")
pyautogui.press("enter")

print ("Fourth part executed")

pyautogui.moveTo(512,16)
pyautogui.click()
pyautogui.hotkey("ctrl","c")
pyautogui.moveTo(1252,179) 
pyautogui.click()
pyautogui.hotkey("ctrl","v")
pyautogui.press("enter")

print ("Fifth part executed")