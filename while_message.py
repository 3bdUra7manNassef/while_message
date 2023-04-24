#*modulse*#
import pyautogui as gui 
import time

#*chose massagse*#
while_to_print = input('enter a number to while print massaeg: ') #! input the user to while massag
massage = input('enter a massage: ') #! massage the uaer

#*sleep the computer*#
time.sleep(5)

#*while the massage*#

for i in range(int(while_to_print)): #! print a massage in for loop
    gui.typewrite(massage)
    gui.press('Enter')