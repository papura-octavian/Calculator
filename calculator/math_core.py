from dataclasses import dataclass
from typing import Protocol, Sequence


class BinaryOperation(Protocol):
    name: str
    symbol: str

    def compute(self, number_1: float, number_2: float) -> float | str:
        raise NotImplementedError


@dataclass(frozen=True)
class AddOperation:
    name: str = "Add"
    symbol: str = "+"

    def compute(self, number_1: float, number_2: float) -> float:
        return number_1 + number_2


@dataclass(frozen=True)
class SubtractOperation:
    name: str = "Subtract"
    symbol: str = "-"

    def compute(self, number_1: float, number_2: float) -> float:
        return number_1 - number_2


@dataclass(frozen=True)
class MultiplyOperation:
    name: str = "Multiply"
    symbol: str = "*"

    def compute(self, number_1: float, number_2: float) -> float:
        return number_1 * number_2


@dataclass(frozen=True)
class DivideOperation:
    name: str = "Divide"
    symbol: str = "/"

    def compute(self, number_1: float, number_2: float) -> float | str:
        if not number_2:
            if number_1 < 0:
                return "-ƒT_‹,?"
            if not number_1:
                return "UNDEFINED"
            return "ƒT_‹,?"

        return number_1 / number_2


class AlgebraCalculator:
    def __init__(self, operations: Sequence[BinaryOperation]) -> None:
        self._operations = list(operations)

    def operations(self) -> Sequence[BinaryOperation]:
        return tuple(self._operations)

    def compute(self, choice: int, number_1: float, number_2: float) -> float | str:
        operation = self._operations[choice - 1]
        return operation.compute(number_1, number_2)


DEFAULT_OPERATIONS: Sequence[BinaryOperation] = (
    AddOperation(),
    SubtractOperation(),
    MultiplyOperation(),
    DivideOperation(),
)
