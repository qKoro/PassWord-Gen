import sys,time,os,random,fonction,string
from pystyle import *
listbye = ["""  ___                                           _      _            
 | _ )_  _ ___     ______ ___   _  _ ___ _  _  | |__ _| |_ ___ _ _  
 | _ \ || / -_)_  (_-< -_) -_) | || / _ \ || | | / _` |  _/ -_) '_| 
 |___/\_, \___( ) /__|___\___|  \_, \___/\_,_| |_\__,_|\__\___|_|(_)
      |__/    |/                |__/                                \n\n\nPRESS ENTER""", """   ___              _ _               ___   _                    _                                                     _        
  / __|___  ___  __| | |__ _  _ ___  |_ _| | |_  ___ _ __  ___  | |_ ___   ______ ___   _  _ ___ _  _   __ _ __ _ __ _(_)_ _    
 | (_ / _ \/ _ \/ _` | '_ \ || / -_)  | |  | ' \/ _ \ '_ \/ -_) |  _/ _ \ (_-< -_) -_) | || / _ \ || | / _` / _` / _` | | ' \ _ 
  \___\___/\___/\__,_|_.__/\_, \___| |___| |_||_\___/ .__/\___|  \__\___/ /__|___\___|  \_, \___/\_,_| \__,_\__, \__,_|_|_||_(_)
                           |__/                     |_|                                 |__/                |___/               \n\n\nPRESS ENTER""", """   ___              _      _             _                                            _             _     _                                
  / __|___  ___  __| |  __| |__ _ _  _  | |_ ___   _  _ ___ _  _   __ ___ _ __  ___  | |__  __ _ __| |__ | |_ ___   ______ ___   _  _ ___  
 | (_ / _ \/ _ \/ _` | / _` / _` | || | |  _/ _ \ | || / _ \ || | / _/ _ \ '  \/ -_) | '_ \/ _` / _| / / |  _/ _ \ (_-< -_) -_) | || (_-<_ 
  \___\___/\___/\__,_| \__,_\__,_|\_, |  \__\___/  \_, \___/\_,_| \__\___/_|_|_\___| |_.__/\__,_\__|_\_\  \__\___/ /__|___\___|  \_,_/__(_)
                                  |__/             |__/                                                                                    \n\n\nPRESS ENTER"""]

def Generate_Msg():
    RanMsg = random.randint(0, 2)
    if RanMsg == 0:
        fonction.typewriter(listbye[0])
    elif RanMsg == 1:
        fonction.typewriter(listbye[1])
    else:
        fonction.typewriter(listbye[2])
    time.sleep(1.5)
def Generate_Msg_RGB():
    RanmsgRGB = random.randint(0,2)
    if RanmsgRGB == 0:
        Anime.Fade(Center.Center(listbye[0]), Colors.white_to_red, Colorate.Horizontal, enter=True)
    elif RanmsgRGB == 1:
        Anime.Fade(Center.Center(listbye[1]), Colors.blue_to_green, Colorate.Horizontal, enter=True)
    else:
        Anime.Fade(Center.Center(listbye[2]), Colors.blue_to_red, Colorate.Horizontal, enter=True)

def Generate_Password(num):
    password = ''

    for n in range(num):
        x = random.randint(0, 94)
        password += string.printable[x]
    return Colorate.Horizontal(Colors.red_to_yellow, password)
banner1 ="""                                                                                
                                                                                
                                   ///////////                                  
                              /////////////////////                             
                          .///////////////////////////,                         
                        %/////////%           //////////                        
                       ////////*                 ////////(                      
                      ///////(                     ////////                     
                     ////////                       ///////#                    
                     ////////                       ///////*                    
                     ////////                       ///////(                    
                     ////////                       ///////(                    
                     ////////                       ///////(                    
                     ////////                       ///////(                    
               (/////////////////////////////////////////////////%              
             ///////////////////////////////////////////////////////            
            //////////////////////////////////&//////////////////////           
           ./////////////////////////////////@@@@@@@@////////////////           
           .////////////////////////////////@@@@@@@@/////////////////           
           .///////////////////////////////@@@@@@@@//////////////////           
           .//////////////////////////////@@@@@@@@///////////////////           
           ./////////////////////////////@@@@@@@@////////////////////           
           .//////////////////@@@@@/////@@@@@@@@/////////////////////           
           .////////////////#@@@@@@@@@&@@@@@@@@//////////////////////           
           ./////////////////#@@@@@@@@@@@@@@@@///////////////////////           
           ./////////////////////@@@@@@@@@@@@////////////////////////           
           ./////////////////////////@@@@@@&/////////////////////////           
            ////////////////////////////&@%//////////////////////////           
            *///////////////////////////////////////////////////////            
              (///////////////////////////////////////////////////(             
                  ///////////////////////////////////////////(/                 
                                                                                """
Title = """ ██▓███   ▄▄▄        ██████   ██████  █     █░ ▒█████   ██▀███  ▓█████▄         ▄████ ▓█████  ███▄    █ 
▓██░  ██▒▒████▄    ▒██    ▒ ▒██    ▒ ▓█░ █ ░█░▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌       ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
▓██░ ██▓▒▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄   ▒█░ █ ░█ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌      ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
▒██▄█▓▒ ▒░██▄▄▄▄██   ▒   ██▒  ▒   ██▒░█░ █ ░█ ▒██   ██░▒██▀▀█▄  ░▓█▄   ▌      ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
▒██▒ ░  ░ ▓█   ▓██▒▒██████▒▒▒██████▒▒░░██▒██▓ ░ ████▓▒░░██▓ ▒██▒░▒████▓       ░▒▓███▀▒░▒████▒▒██░   ▓██░
▒▓▒░ ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒        ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
░▒ ░       ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░  ▒ ░ ░    ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒         ░   ░  ░ ░  ░░ ░░   ░ ▒░
░░         ░   ▒   ░  ░  ░  ░  ░  ░    ░   ░  ░ ░ ░ ▒    ░░   ░  ░ ░  ░       ░ ░   ░    ░      ░   ░ ░ 
               ░  ░      ░        ░      ░        ░ ░     ░        ░                ░    ░  ░         ░ 
                                                                 ░                                      """
message = "\nHow many characters, Do you want in your password. (8 Character Minimum) \n--> "
ErrorMessage = "** 8 Character Minimum **"
ContinueMsg = "\n\n\n--Do you want to continue--\n1 - Yes\n2 - No\n"
ErrorMessageContinue = "**Invalid**"
redirectionMsg = "Redirection . . . . . . . . . . . . . . . . . . ."
retryMsg = "\n\n\n--Do you want retry--\n1 - Yes\n2 - No\n"
Anime.Fade(Center.Center(banner1), Colors.green_to_black, Colorate.Diagonal, enter=True)

while True:
    print(Colorate.Diagonal(Colors.red_to_purple,Title, 1))
    num = fonction.typewriter(message)
    num = input()
    num = int(num)
    print("\n\n\n")
    if num >= 8:
        print(Generate_Password(num))
        time.sleep(0.05)
        continueQ = fonction.typewriter(ContinueMsg)
        continueQ = input()
        continueQ = int(continueQ)
        if continueQ == 1:
            os.system("cls")
        elif continueQ == 2:
            Generate_Msg_RGB()
            
            break
        else:
            ErrorContinueQ = fonction.typewriter(ErrorMessageContinue)
            print("\n")
            time.sleep(1)
            redirection = fonction.typewriter(redirectionMsg)
            os.system("cls")
            print("\n")
            continueQ = fonction.typewriter(retryMsg)
            continueQ = input()
            continueQ = int(continueQ)
            if continueQ == 1:
                os.system("cls")
            elif continueQ == 2:
                Generate_Msg_RGB()
    else:
        fonction.typewriter(ErrorMessage)
        print("\n")
        time.sleep(1)
        fonction.typewriter(redirectionMsg)
        os.system("cls")