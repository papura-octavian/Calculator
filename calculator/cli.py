from fractions import Fraction
import os
from calculator.math_core import Algebra
from calculator import geometry_core

RED = "\033[31m"
RESET = "\033[0m"
PINK = "\033[95m"   # light magenta

#   ----------- Bash options ----------------------

def clear_bash() -> None:
    os.system("cls" if os.name == "nt" else "clear")


#   ------------- Algebra -------------------------

def get_numbers() -> Algebra:
    while True:
        clear_bash()
        try:
            a = float(Fraction(input("First number = ")))
            b = float(Fraction(input("Second number = ")))

            return Algebra(a, b)       
        except Exception as err:
            print(RED + "!!! PLEASE ENTER NUMBERS !!!" + RESET)
            print(f"Error type : {err}")
            input("\nPress Enter to continue...")

def menu_algebra() -> int:
        clear_bash()
        print("========================")
        print("[1] - ADD")
        print("[2] - SUB")
        print("[3] - MULTIPLY")
        print("[4] - DIVIDE")
        print("========================")

        return check_ans(4)   
    
def show_menu_algebra() -> int:
        clear_bash()
        print("========================")
        print("[1] - Basic Operations")
        print("========================")

        return check_ans(1)

def check_operation_type(choice: int) -> str:
        match choice:
            case 1:
                return "+"
            case 2:
                return "-"
            case 3:
                return "*"
            case 4:
                return "/"

def show_result(operation: str, x: float, y: float, result: float) -> None:
        print("------------------")
        print(f"{x} {operation} {y} = {result}")
        print("------------------")


# ---------------- Geometry --------------------------

def check_ans_shape(choice: int) -> geometry_core.Triangle:
        match choice:
            # triangle
            case 1:
                while True:
                    clear_bash()
                    try:
                        a = float(Fraction(input("First side = ")))
                        b = float(Fraction(input("Second side = ")))
                        c = float(Fraction(input("Third side = ")))

                        if a + b <= c or a + c <= b or b + c <= a:
                            print(RED + "The sides do not form a valid triangle" + RESET)
                            input("\nPress Enter to continue...")
                            continue

                        return geometry_core.Triangle(a, b, c)
                    except Exception as err:
                        print(RED + "!!! PLEASE ENTER NUMBERS !!!" + RESET)
                        print(f"Error type : {err}")
                        input("\nPress Enter to continue...")

def show_menu_geometry():
        clear_bash()
        print("========================")
        print("[1] - Triangle")
        print("========================")

        return check_ans_shape(check_ans(1))

def menu_geometry(shape) -> None:
        clear_bash()
        match shape:
            # ============ TRIUNGHI =====================
            case geometry_core.Triangle() as triangle:

                while True:
                    clear_bash()
                    print("========================")
                    print("[1] - Perimeter")
                    print("[2] - Check if it's a right triangle")
                    print("[3] - Calculate height")
                    print("[4] - Area")
                    print("========================")

                    match check_ans(4):
                        case 1:
                            print(f"The perimeter of the triangle is: {triangle.perimeter()}")
                        case 2:
                            if triangle.check_right_triangle():
                                print("The triangle is right-angled!")
                            else:
                                print("The triangle is not right-angled!")

                        case 3:
                            print(f"\nCoresponding base:\n[1] - AB = {triangle.side1}\n[2] - BC = {triangle.side2}\n[3] - AC = {triangle.side3}")
                            match check_ans(3):
                                case 1:
                                    print(f"The height for base = {triangle.side1} is {triangle.calc_height(triangle.side1)}")
                                case 2:
                                    print(f"The height for base = {triangle.side2} is {triangle.calc_height(triangle.side2)}")
                                case 3:
                                    print(f"The height for base = {triangle.side3} is {triangle.calc_height(triangle.side3)}")
                        case 4:
                            print(f"The area of the triangle is: {triangle.area()}")

                    if not continue_or_exit():
                        return
        
# ============== UI Funcions ====================

def show_menu() -> bool:
        clear_bash()
        print("========================")
        print("[1] - Algebra")
        print("[2] - Geometry")
        print("[3] - Exit")
        print("========================")

        match check_ans(3):
            case 1:
                match show_menu_algebra():
                    case 1:
                        algebra = get_numbers()
                        while True:
                            calculus_sign = menu_algebra()
                            show_result(check_operation_type(calculus_sign), algebra.number_1, algebra.number_2, algebra.check_choice(calculus_sign))

                            if not continue_or_exit():
                                return False
            case 2:
                shape = show_menu_geometry()
                menu_geometry(shape)
            
            # Exit Program
            case 3:
                return True

def check_ans(no_chocices) -> int:   
    while True: 
        try:
            answer = int(input("\nAnswer : "))
            if answer >= 1 and answer <= no_chocices:
                return answer
            else:
                options = ", ".join(str(i) for i in range(1, no_chocices + 1))
                print(RED + f"!!! CHOOSE FROM THE NUMBERS DISPLAYED" + PINK + options + RESET + "!!!")
                input("\nPress Enter to continue...")
        except Exception as err:
            print(RED + "!!! PLEASE ONLY NATURAL NUMBERS !!!" + RESET)
            print(f"Error type : {err}")
            input("\nPress Enter to continue...")



def continue_or_exit() -> bool:
    while True:
        answer = input("\nContinue? [Y / N]: ").lower()

        if answer == "n":
            return False
        
        if answer == "y":
            return True

        clear_bash()
        print(RED + "!!! I AM NOT LEAVING THIS FUNCTION UNTIL I GET A CLEAR RESPONSE AS IN \"Y\" or \"N\" !!!" + RESET)

def run() -> None:
    while True:
        if show_menu():
            return

