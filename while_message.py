#*modules*#
import pyautogui as gui 
import time

#*chose messages*#
while_to_print = input('enter a number to while print messaeg: ') #! input the user to while message
massage = input('enter a massage: ') #! massage the user

#*sleep the computer*#
time.sleep(5)

#*while the message*#

for i in range(int(while_to_print)): #! print a massage in for loop
    gui.typewrite(massage)
    gui.press('Enter')