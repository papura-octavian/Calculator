import os
from calculator.math_core import check_choice

RED = "\033[31m"
RESET = "\033[0m"

def clear_bash():
    os.system("cls" if os.name == "nt" else "clear")

def get_numbers():
    while True:
        clear_bash()
        try:
            a = float(input("First number = "))
            b = float(input("Second number = "))

            return a, b       
        except Exception as err:
            print(RED + "!!! PLEASE ENTER NUMBERS !!!" + RESET)
            print(f"Error type : {err}")
            input("\nPress a Enter to continue...")

def show_menu():
    clear_bash()
    print("========================")
    print("[1] - ADD")
    print("[2] - SUB")
    print("[3] - MULTIPLY")
    print("[4] - DIVIDE")
    print("========================")

def check_ans():   
    while True:
        show_menu() 
        try:
            answer = int(input("\nAnswer : "))
            if answer >= 1 and answer <= 4:
                return answer
            else:
                print(RED + "!!! CHOOSE FROM THE NUMBERS DISPLAYED (1, 2, 3, 4) !!!" + RESET)
                input("\nPress a Enter to continue...")
        except Exception as err:
            print(RED + "!!! PLEASE ONLY NATURAL NUMBERS !!!" + RESET)
            print(f"Error type : {err}")
            input("\nPress a Enter to continue...")



def continue_or_exit():
    while True:
        answer = input("Continue...[Y / N]: ").lower()

        if answer == "n":
            return False
        
        if answer == "y":
            return True

        clear_bash()
        print(RED + "!!! I AM NOT LEAVING THIS FUNCTION UNTIL I GET A CLEAR RESPONSE AS IN \"Y\" or \"N\" !!!" + RESET)


def run():
    while True:
        x, y = get_numbers()
        check_choice(check_ans(), x, y)
        if not continue_or_exit():
            return

