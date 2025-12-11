class Algebra:
    def __init__(self, number_1: float, number_2: float) -> None:
        self.number_1 = number_1
        self.number_2 = number_2

    def check_choice(self, choice: int) -> float | str: 
        match choice:
            # ADD
            case 1:
                return self.number_1 + self.number_2
            
            # SUB
            case 2:
                return self.number_1 +-self.number_2

            # MULTIPLY
            case 3:
                return self.number_1 * self.number_2

            # DIVIDE
            case 4:
                if not self.number_2:
                    if self.number_1 < 0:
                        return "-♾️"
                    elif not self.number_1:
                        return "UNDEFINED"
                    else:
                        return "♾️"

                else:
                    return self.number_1 / self.number_2