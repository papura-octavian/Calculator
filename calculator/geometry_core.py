from dataclasses import dataclass
from math import sqrt


def is_valid_triangle(side1: float, side2: float, side3: float) -> bool:
    return (
        side1 + side2 > side3
        and side1 + side3 > side2
        and side2 + side3 > side1
    )


@dataclass(frozen=True)
class Triangle:
    side1: float
    side2: float
    side3: float

    def perimeter(self) -> float:
        return self.side1 + self.side2 + self.side3

    def check_right_triangle(self) -> bool:
        x, y, z = pow(self.side1, 2), pow(self.side2, 2), pow(self.side3, 2)
        return (x + y) == z or (x + z) == y or (y + z) == x

    def calc_height(self, base: float) -> float:
        match base:
            case self.side1:
                x = (pow(self.side2, 2) - pow(self.side3, 2) + pow(self.side1, 2)) / (
                    2 * self.side1
                )
                return sqrt(pow(self.side2, 2) - pow(x, 2))
            case self.side2:
                x = (pow(self.side3, 2) - pow(self.side1, 2) + pow(self.side2, 2)) / (
                    2 * self.side2
                )
                return sqrt(pow(self.side3, 2) - pow(x, 2))
            case self.side3:
                x = (pow(self.side1, 2) - pow(self.side2, 2) + pow(self.side3, 2)) / (
                    2 * self.side3
                )
                return sqrt(pow(self.side1, 2) - pow(x, 2))

        raise ValueError("Base must be one of the triangle sides.")

    def area(self) -> float:
        p = self.perimeter() / 2
        return sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))
