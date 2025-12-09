def check_choice(choice, x, y):
    match choice:
        # ADD
        case 1:
            return x + y
        
        # SUB
        case 2:
            return x - y

        # MULTIPLY
        case 3:
            return x * y

        # DIVIDE
        case 4:
            if not y:
                if x < 0:
                    return "-♾️"
                elif not x:
                    return "UNDEFINED"
                else:
                    return "♾️"

            else:
                return x / y