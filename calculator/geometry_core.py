from math import sqrt


class Triangle:

    # Constructor
    def __init__(self, s1: float, s2: float, s3: float) -> None:
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3

    def perimeter(self) -> float:
        return self.side1 + self.side2 + self.side3

    def check_right_triangle(self) -> bool:
        x, y, z = pow(self.side1, 2), pow(self.side2, 2), pow(self.side3, 2)
        return (x + y) == z or (x + z) == y or (y + z) == x
        
            
    # x is the base's side we don't know after we draw the height
    # so the other side is: (base - x)
    # if the base is side3 then:
    # h^2 = side1^2 - x^2
    # h^2 = side2^2 - (base - x)^2  
    def calc_height(self, base: float) -> float:
        match base:
            case self.side1:
                x = ( pow(self.side2, 2) - pow(self.side3, 2) + pow(self.side1, 2) ) / (2 * self.side1)
                return sqrt( pow(self.side2, 2) - pow(x, 2) )

            case self.side2:
                x = ( pow(self.side3, 2) - pow(self.side1, 2) + pow(self.side2, 2) ) / (2 * self.side2)
                return sqrt( pow(self.side3, 2) - pow(x, 2) )

            case self.side3:
                x = ( pow(self.side1, 2) - pow(self.side2, 2) + pow(self.side3, 2) ) / (2 * self.side3)
                return sqrt( pow(self.side1, 2) - pow(x, 2) )
                
    def area(self) -> float:
        # semiperimeter
        p = (self.side1 + self.side2 + self.side3) / 2

        area = sqrt(p * (p - 1) * (p - 2) * (p - 3))

        return area

