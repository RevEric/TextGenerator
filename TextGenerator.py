import random
import os
import sys
import time

running = 1
while(running == 1):
    #target = "Sample string."
    target = input("Enter string: ")
    print("")
    current = list()
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,? "

    clear = lambda: os.system('cls')
    clear()

    time.sleep(3)

    i = 0
    current.append("")
    while (i < len(target)):
        #first we have to make sure that the character is in our charset, and if it isn't, it gets added
        if target[i] not in charset:
            charset = charset + target[i]
        
        current[i] = random.choice(charset)
        print ("    ", ''.join(current), '',end='\r')
        time.sleep(.00001)
        if(current[i] == target[i]):
            i = i + 1
            current.append("")
    
    print("\n")
    answer = input("Enter Y to continue, anything else to quit: ")
    if(answer.lower() != "y"):
        running = 0
    else:
        print("")


