import os

def logo():
    print('''
  ▄████  ██▀███   ▒█████   █    ██  ██▓███  ▓█████  ██▀███  
 ██▒ ▀█▒▓██ ▒ ██▒▒██▒  ██▒ ██  ▓██▒▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▓██ ░▄█ ▒▒██░  ██▒▓██  ▒██░▓██░ ██▓▒▒███   ▓██ ░▄█ ▒
░▓█  ██▓▒██▀▀█▄  ▒██   ██░▓▓█  ░██░▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒░██▓ ▒██▒░ ████▓▒░▒▒█████▓ ▒██▒ ░  ░░▒████▒░██▓ ▒██▒
 ░▒   ▒ ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ░▒ ░ ▒░  ░ ▒ ▒░ ░░▒░ ░ ░ ░▒ ░      ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░░   ░ ░ ░ ░ ▒   ░░░ ░ ░ ░░          ░     ░░   ░ 
      ░    ░         ░ ░     ░                 ░  ░   ░                                                         
    ''')

cwdir =  os.getcwd()

print("\nCWD : {}\n".format(cwdir))

_, _, filenames = next(os.walk(cwdir))

ignore_file = []

while True:
    os.system("cls")
    logo()
    print("| 1 | Ignore files with extension")
    if len(ignore_file) > 0:
        print("\tignore Files : ",ignore_file)
    print("\n| [ Enter ] To Start Grouping |")

    command = input("\n? ")

    if command == '1':
        os.system("cls")
        logo()
        print("\nEnter file Extensions\n\nExample :\n\tmkv\n\tmp3\n\tmp4\n\tpng")
        print("\npress 0 to stop")
        file = None
        while(file!='0'):
            file = input("\n:")
            if file == '0':
                break
            if file != '':
                ignore_file.append(file)
    elif command == "":
        break
    else:
        continue
        
os.system("cls")
logo()

for i in filenames:   
    a = i.split(".")
    try :
        try:    # Make Folder If not their
            if a[-1] not in ignore_file:
                b = "{}\\".format(cwdir)
                path = os.path.join(b,a[-1])
                os.makedirs(path)
                print("$ Folder Created : ",a[-1])
        finally:    # replace File Place To Correct Folder
            if a[-1] not in ignore_file:
                if a[0] != "Grouper":       
                    c_file_place = os.path.join(cwdir,"{}.{}".format(".".join(a[:-1]),a[-1]))
                    new_file_place = os.path.join(cwdir,"{}\\{}.{}".format(a[-1],".".join(a[:-1]),a[-1]))
                    os.rename(c_file_place,new_file_place)
    except Exception as e:
        pass

input("\n\n\nPress Enter To Exit : ")
