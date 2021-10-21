import sys,time,os



def typewriter(message): #fonction name
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        
        if char != "\n":
            time.sleep(0.05) #spacing between each letter
        else:
            time.sleep(0.5) #spacing between each paragraph



os.system("cls")




