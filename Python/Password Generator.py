import string
import subprocess 
import random
import pyperclip
from os import system


def _copy_(data):
    pyperclip.copy("{}".format(data))

def clear_screen():     # clear Screen
    return system("cls")

class stringc:
    def Num_of_lowercase(self, _String):
        return len([i for i in _String if i in string.ascii_lowercase])

    def Num_of_lowercase(self, _String):
        return len([i for i in _String if i in string.ascii_lowercase])

    def Num_of_uppercase(self, _String):
        return len([i for i in _String if i in string.ascii_uppercase])

    def Num_of_letters(self, _String):
        return len([i for i in _String if i in string.ascii_letters])

    def Num_of_digits(self, _String):
        return len([i for i in _String if i in string.digits])

    def Num_of_punctuation(self, _String):
        return len([i for i in _String if i in string.punctuation]) 

    def Num_of_whitespace(self, _String):
        return len([i for i in _String if i in string.whitespace])


#-  -   -   Password Checking  -   -   -   -#

class Password_Checking(stringc):
    def __init__(self):
        self._lowercase = {1:0.5, 2:0.5, 4:2, 6:3}
        self._uppercase = {1:0.5, 2:0.5, 4:2, 6:3}
        self._letters = {4:2, 6:2, 8:2, 12:4}
        self._digits = {1:0.5, 2:0.5, 4:2, 6:3}
        self._whitespace = {1:1, 2:1.5, 4:2}
        self._special_character = {1:1, 2:1.5, 4:2}

        self.keys_group = [self._lowercase, self._uppercase, 
            self._letters, self._digits, self._whitespace, 
            self._special_character]

    def get_strength_point(self, Password):
        self.Key_data = [self.Num_of_lowercase(Password), self.Num_of_uppercase(Password),
            self.Num_of_letters(Password), self.Num_of_digits(Password), 
            self.Num_of_whitespace(Password), self.Num_of_punctuation(Password)]
        # print(Key_data)
        
        self.Points = 0
        for ii in range(len(self.keys_group)):
            self.kgro = self.keys_group[ii]

            for i in self.kgro:
                if i <= self.Key_data[ii]:
                    self.Points += self.kgro[i]
        
        if 20 >= len(Password):
            self.Points += (len(Password)/2)
        else :
            self.Points += 10

        return self.Points

    def Password_strength(self, Points):
        if Points <= 10: return "Strength: Weak"
        elif Points > 10 and Points <= 15: return "Strength: Normal"
        elif Points > 15 and Points <= 20: return "Strength: Good"
        elif Points > 20 and Points <= 30: return "Strength: Strong"
        elif Points > 30 and Points <= 44.5: return "Strength: Strongest"
        elif Points >= 45:  return "Strength: Super Strong"

    def main(self):
        while True:
            print('\n')
            print("q | STOP".center(20,'-'))    
            self._Password = input(":")
            self.Points = self.get_strength_point(self._Password)
            
            print("Points : ",self.Points)
            print("Length : ",len(self._Password))
            print(self.Password_strength(self.Points))
            
            if self._Password == "q": 
                clear_screen()
                break


#-  -   -    Password_genrator   -   -   -#

#Information About Password
class Password_Genrator(Password_Checking):

    def About_Password(self):
        # global Length_pass      #length of the password | used in Genrates_password()
        # global yn_list          # yes/No list created with loop | used in Genrates_password()

        print(("-"*20) + "q | Stop" + ("-"*20) )  

        print("\nWhat You Want InTo our Password:")
        self.Length_pass = int(input("Length: "))

        self.querys =["Digits (y/n):", "lowercase (y/n):", "uppercare (y/n):", 
                "Spical Charaters (y/n):", "whitespace (y/n):"]      #printing To get Input
        self.yn_list = list()

        for i in range(5):      # Getting Input using loop
            _input = input(self.querys[i])
            if _input != 'y' and _input != 'Y': self.yn_list.append('n')
            else: self.yn_list.append(_input)

        # print(yn_list)
        self.Genrates_password()

    # Password Genrates Here:
    def Genrates_password(self):
        clear_screen()
        self.Keyboard = [list(string.digits), list(string.ascii_lowercase), list(string.ascii_uppercase), 
                list(string.punctuation), [' ']]   #data get from inbuilt string module
        self.Demand_list = []        #demand list which user has demand for digits or lowercase or..., {y/n}
        
        for i in range(5):
            if self.yn_list[i] == 'y' or self.yn_list[i] == 'Y':
                for ii in range(self.Length_pass):
                    rrc = random.choice(self.Keyboard[i])
                    self.Demand_list.append(rrc)
        
        self.password_ = []          #final Password list choice from Demand_list using random
        for o in range(self.Length_pass):
            rp = random.choice(self.Demand_list)
            self.password_.append(rp)

        # Finnaly Print : STUF :

        print('-' * (10+len(self.password_)))
        #printing password and points and strength
        PP = "".join(self.password_)
        print("Password: {}".format(PP))

        point = Password_Checking().get_strength_point(self.password_)
        print("Points : ",point)
        print(Password_Checking().Password_strength(point))
        
        print('-' * (10+len(self.password_)))

        print("Password Is Copy To Clipboard\n")        #To Copy Password
        data = "".join(self.password_)
        # subprocess.run("clip",universal_newlines=True, input=data)
        _copy_(data)
        #genrate again or not ? 
        dec = input("\nPress Enter To Gen Again\nPress ' cn ' To Create New :")
        if dec == 'cn' : self.About_Password()    
        else: return self.Genrates_password()

if __name__ == '__main__':
    while True:
        try:
            clear_screen()
            print("\n1 | Check Password Strength\n2 | Generate Password")
            ur = int(input(":"))    
            if ur == 1:
                Password_Checking().main()
            elif ur == 2:
                Password_Genrator().About_Password()
        except: pass