from fractions import Fraction
import os
from dataclasses import dataclass
from typing import Sequence

from calculator.geometry_core import Triangle, is_valid_triangle
from calculator.math_core import AlgebraCalculator, BinaryOperation, DEFAULT_OPERATIONS

RED = "\033[31m"
RESET = "\033[0m"
PINK = "\033[38;5;205m"


def format_num(value: float | str) -> str:
    if isinstance(value, (int, float)):
        return f"{value:.2f}"
    return str(value)


@dataclass
class ConsoleIO:
    def clear(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")

    def write(self, message: str) -> None:
        print(message)

    def read(self, prompt: str) -> str:
        return input(prompt)

    def pause(self) -> None:
        input("\nPress Enter to continue...")


class InputParser:
    def __init__(self, io: ConsoleIO) -> None:
        self._io = io

    def read_float(self, prompt: str) -> float:
        while True:
            self._io.clear()
            try:
                return float(Fraction(self._io.read(prompt)))
            except Exception as err:
                self._io.write(RED + "!!! PLEASE ENTER NUMBERS !!!" + RESET)
                self._io.write(f"Error type : {err}")
                self._io.pause()

    def read_int_in_range(self, prompt: str, minimum: int, maximum: int) -> int:
        while True:
            try:
                answer = int(self._io.read(prompt))
                if minimum <= answer <= maximum:
                    return answer
                options = ", ".join(str(i) for i in range(minimum, maximum + 1))
                self._io.write(
                    RED
                    + "!!! CHOOSE FROM THE NUMBERS DISPLAYED "
                    + PINK
                    + f"({options})"
                    + RED
                    + " !!!"
                    + RESET
                )
                self._io.pause()
            except Exception as err:
                self._io.write(RED + "!!! PLEASE ONLY NATURAL NUMBERS !!!" + RESET)
                self._io.write(f"Error type : {err}")
                self._io.pause()

    def read_yes_no(self, prompt: str) -> bool:
        while True:
            answer = self._io.read(prompt).lower()
            if answer == "n":
                return False
            if answer == "y":
                return True
            self._io.clear()
            self._io.write(
                RED
                + '!!! I AM NOT LEAVING THIS FUNCTION UNTIL I GET A CLEAR RESPONSE AS IN "Y" or "N" !!!'
                + RESET
            )


class AlgebraUI:
    def __init__(
        self,
        io: ConsoleIO,
        parser: InputParser,
        calculator: AlgebraCalculator,
    ) -> None:
        self._io = io
        self._parser = parser
        self._calculator = calculator

    def _show_menu(self, operations: Sequence[BinaryOperation]) -> int:
        self._io.clear()
        self._io.write("========================")
        for index, operation in enumerate(operations, start=1):
            self._io.write(f"[{index}] - {operation.name.upper()}")
        self._io.write("========================")
        return self._parser.read_int_in_range("\nAnswer : ", 1, len(operations))

    def run(self) -> None:
        number_1 = self._parser.read_float("First number = ")
        number_2 = self._parser.read_float("Second number = ")
        operations = self._calculator.operations()

        while True:
            choice = self._show_menu(operations)
            operation = operations[choice - 1]
            result = self._calculator.compute(choice, number_1, number_2)
            self._io.write("------------------")
            self._io.write(
                f"{format_num(number_1)} {operation.symbol} {format_num(number_2)} = {format_num(result)}"
            )
            self._io.write("------------------")

            if not self._parser.read_yes_no("\nContinue? [Y / N]: "):
                return


class GeometryUI:
    def __init__(self, io: ConsoleIO, parser: InputParser) -> None:
        self._io = io
        self._parser = parser

    def _read_triangle(self) -> Triangle:
        while True:
            side1 = self._parser.read_float("First side = ")
            side2 = self._parser.read_float("Second side = ")
            side3 = self._parser.read_float("Third side = ")
            if not is_valid_triangle(side1, side2, side3):
                self._io.write(RED + "The sides do not form a valid triangle" + RESET)
                self._io.pause()
                continue
            return Triangle(side1, side2, side3)

    def run(self) -> None:
        triangle = self._read_triangle()
        while True:
            self._io.clear()
            self._io.write("========================")
            self._io.write("[1] - Perimeter")
            self._io.write("[2] - Check if it's a right triangle")
            self._io.write("[3] - Calculate height")
            self._io.write("[4] - Area")
            self._io.write("========================")

            match self._parser.read_int_in_range("\nAnswer : ", 1, 4):
                case 1:
                    self._io.write(
                        f"The perimeter of the triangle is: {format_num(triangle.perimeter())}"
                    )
                case 2:
                    if triangle.check_right_triangle():
                        self._io.write("The triangle is right-angled!")
                    else:
                        self._io.write("The triangle is not right-angled!")
                case 3:
                    self._io.write(
                        "\nCoresponding base:\n"
                        f"[1] - AB = {format_num(triangle.side1)}\n"
                        f"[2] - BC = {format_num(triangle.side2)}\n"
                        f"[3] - AC = {format_num(triangle.side3)}"
                    )
                    match self._parser.read_int_in_range("\nAnswer : ", 1, 3):
                        case 1:
                            self._io.write(
                                f"The height for base = {format_num(triangle.side1)} is {format_num(triangle.calc_height(triangle.side1))}"
                            )
                        case 2:
                            self._io.write(
                                f"The height for base = {format_num(triangle.side2)} is {format_num(triangle.calc_height(triangle.side2))}"
                            )
                        case 3:
                            self._io.write(
                                f"The height for base = {format_num(triangle.side3)} is {format_num(triangle.calc_height(triangle.side3))}"
                            )
                case 4:
                    self._io.write(
                        f"The area of the triangle is: {format_num(triangle.area())}"
                    )

            if not self._parser.read_yes_no("\nContinue? [Y / N]: "):
                return


class CalculatorApp:
    def __init__(self) -> None:
        self._io = ConsoleIO()
        self._parser = InputParser(self._io)
        self._algebra = AlgebraUI(
            self._io,
            self._parser,
            AlgebraCalculator(DEFAULT_OPERATIONS),
        )
        self._geometry = GeometryUI(self._io, self._parser)

    def run(self) -> None:
        while True:
            self._io.clear()
            self._io.write("========================")
            self._io.write("[1] - Algebra")
            self._io.write("[2] - Geometry")
            self._io.write("[3] - Exit")
            self._io.write("========================")

            match self._parser.read_int_in_range("\nAnswer : ", 1, 3):
                case 1:
                    self._io.clear()
                    self._io.write("========================")
                    self._io.write("[1] - Basic Operations")
                    self._io.write("========================")
                    self._parser.read_int_in_range("\nAnswer : ", 1, 1)
                    self._algebra.run()
                case 2:
                    self._io.clear()
                    self._io.write("========================")
                    self._io.write("[1] - Triangle")
                    self._io.write("========================")
                    self._parser.read_int_in_range("\nAnswer : ", 1, 1)
                    self._geometry.run()
                case 3:
                    return


def run() -> None:
    CalculatorApp().run()


if __name__ == "__main__":
    run()
