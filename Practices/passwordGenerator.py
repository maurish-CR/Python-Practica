import random
import pyfiglet
import time
import datetime

def upper_cases():
    try:
        num = int(input("How many upper case letters?: "))
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if num >= 0:   
            global new_pass
            new_pass = new_pass + ''.join(random.choice(upper) for _ in range(num))
    except ValueError:
        print("Please enter only numbers...")

def lower_cases():
    try:
        num = int(input("How many lower case letters?: "))
        lower = "abcdefghijklmnopqrstuvwxyz"
        if num >= 0:   
            global new_pass
            new_pass = new_pass + ''.join(random.choice(lower) for _ in range(num))
    except ValueError:
        print("Please enter only numbers...")

def numbers():
    try:
        num = int(input("How many numbers?: "))
        numbers = "1234567890"
        if num >= 0:   
            global new_pass
            new_pass = new_pass + ''.join(random.choice(numbers) for _ in range(num))
    except ValueError:
        print("Please enter only numbers...")
    
def symbol():
    try:
        num = int(input("How many symbols?: "))
        symbols = "`~!@#$%^&*()_+-=[]:,./{;}<>?"

        if num >= 0:   
            global new_pass
            new_pass = new_pass + ''.join(random.choice(symbols) for _ in range(num))
    except ValueError:
        print("Please enter only numbers...")

def pass_gen():   
    global new_pass
    new_pass = ''.join(random.sample(new_pass,len(new_pass)))

def save_pass(password):
    save = str(input("Would you like to save your password? (Y/N): "))
    global new_pass
    ans_possitive = ["Y","y","yes","Yes","YES"]
    ans_negative = ["N","n","no","No","NO"]
    if save in ans_possitive or save in ans_negative: 
        if save in ans_possitive:
            time.sleep(0.5)
            desc = str(input("Description for password(optional): "))
            file1 = open("/home/mauriciof/Documents/Important/passwords", "a")
            date = datetime.datetime.now()
            wr = f"{desc} ({date}): {new_pass}\n"
            file1.writelines(wr)
            file1.close()
            time.sleep(0.5)
            print("Password saved correctly!")
        elif save in ans_negative:
            print("Warning: Your password would be eliminated...")
            confirm = str(input("Confirm elimination (Y/N): "))
            if confirm in ans_possitive:
                print("Password deleted...")
            elif save in ans_negative:
                print("Returning to saving process...")
                time.sleep(0.5)
                save_pass(new_pass)
    else:
        print('Error: Wrong value for password saving... \nIt can ONLY be Yes or No, please try again')
        save_pass(new_pass)


ascii_banner = pyfiglet.figlet_format("xXpassgenXx")
pass_len = 0
new_pass = ""
print(ascii_banner)
upper_cases()
lower_cases()
numbers()
symbol()
pass_gen()
print("New password generated: " + new_pass)
save_pass(new_pass)