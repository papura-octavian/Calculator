YELLOW = "\033[33m"
RESET = "\033[0m"

def check_choice(choice, x, y):
    match choice:
        # ADD
        case 1:
            print("---------------------")
            print(f"{x} + {y} = {x + y}")
            print("---------------------")
        
        # SUB
        case 2:
            print("---------------------")
            print(f"{x} - {y} = {x - y}")
            print("---------------------")

        # MULTIPLY
        case 3:
            print("---------------------")
            print(f"{x} * {y} = {x * y}")
            print("---------------------")

        # DIVIDE
        case 4:
            print("---------------------")

            if not y:
                if x < 0:
                    print(f"{x} / {y} = -♾️")
                elif not x:
                    print(f"{x} / {y} = " + YELLOW + "UNDEFINED" + RESET)
                else:
                    print(f"{x} / {y} = ♾️")

            else:
                print(f"{x} / {y} = {x / y}")

            print("---------------------")