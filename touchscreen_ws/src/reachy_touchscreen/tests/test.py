from sys import getcheckinterval
from pynput.keyboard import Key, Listener

text = input("Press ENTER to calibrate point : ")
coord = 0
while True :
        if text == "":
            print("you pressed enter")
            coord = 3
            break
        else :
            text = input("Pres only ENTER to calibrate the point : ") 



