import time
import os
import platform

def main():
    StartUp()

    while True: 
        arg = input()

        if arg == "s":
            os.system('cls' if os.name == 'nt' else 'clear')
            Session()
        elif arg == "h":
            os.system('cls' if os.name == 'nt' else 'clear')
            Help()
        elif arg == "q":
            os.system('cls' if os.name == 'nt' else 'clear')
            return 0
        else: 
            print("Not valid input, try again")

def Session():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("How long is your workphase in minutes?")
    worktime = input()

    if worktime.isdigit() == False:
        print("Invalid Input. Only Numbers are allowed!")
        print("Try again")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        Session()

    worktimeSeconds = int(worktime) * 60

    print("How long is your restphase in minutes?")
    restphase = input()

    if restphase.isdigit() == False:
        print("Invalid Input. Only Numbers are allowed!")
        print("Try again")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        Session()

    restphaseSeconds = int(restphase) * 60

    os.system('cls' if os.name == 'nt' else 'clear')

    while True: 

        #Workphase 
        for x in range(worktimeSeconds, 0, -1):
            
            Time = time.strftime("%H:%M:%S", time.gmtime(x))

            print("--------------------------")
            print("|       Work Phase       |")
            print("|                        |")
            print("|        " + Time + "        |")
            print("|                        |")
            print("--------------------------")
            
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')

        BeepBoop("Workphase ended", "Take a break, get some coffee or something else.")
        print("Rest Phase begins soon..")
        time.sleep(15)
        
        os.system('cls' if os.name == 'nt' else 'clear')

        #RestPhase
        for y in range(restphaseSeconds, 0, -1):

            Time = Time = time.strftime("%H:%M:%S", time.gmtime(y))

            print("--------------------------")
            print("|       Rest Phase       |")
            print("|                        |")
            print("|        " + Time + "        |")
            print("|                        |")
            print("--------------------------")
            
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')

        BeepBoop("Restphase ended", "Your break is over. Get back to work!")
        print("Rest Phase begins soon..")
        time.sleep(15)
        
        os.system('cls' if os.name == 'nt' else 'clear')



def BeepBoop(title, message):
    if platform.system() == "Darwin":
        os.system('osascript -e \'display notification "{}" with title "{}"\''.format(message, title))
    elif platform.system() == 'Linux':  
        os.system('notify-send "{}" "{}"'.format(title, message))
    elif platform.system() == 'Windows': 
        os.system('powershell -Command "New-BurntToastNotification -Text \'{}\' -Header \'{}\'"'.format(message, title))


def StartUp():

    print("---------------------------------------------------")
    time.sleep(0.15)
    print("|         Pomodoro Timer Terminal Program         |")
    time.sleep(0.15)
    print("|             For Software Developers             |")
    time.sleep(0.15)
    print("|                                                 |")
    time.sleep(0.15)
    print("|        Commands:                                |")
    time.sleep(0.15)
    print("|        (s) Start Session                        |")
    time.sleep(0.15)
    print("|        (h) Help/How to Use                      |")
    time.sleep(0.15)
    print("|        (q) quit                                 |")
    time.sleep(0.15)
    print("|                                                 |")
    time.sleep(0.15)
    print("|             written by Sven Lobbes              |")
    time.sleep(0.15)
    print("---------------------------------------------------")

def Help():
    print("This program runs as long as you want. The Phases changes in your definied timestamps.")
    print("It goes from the workphase to the restphase and then it repeats itself.")
    print("You can close the program anytime with CTRL + C")
    print("                      ")
    print("Enter 'c' to get back to main menu.")
    print("                      ")

    while True: 
        usrInput = input()

        if usrInput == "c":
            os.system('cls' if os.name == 'nt' else 'clear')
            main()
        else: 
            print("invalid Input")

if __name__ == "__main__":
    main()


