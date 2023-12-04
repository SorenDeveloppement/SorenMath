from typing import Union


class Fraction:
    def __init__(self, a: Union[int, float, "Fraction"], b: Union[int, float, "Fraction", None] = 1) -> None:
        self.numerator: int | float | "Fraction" = a

        if not b == 0:
            self.denominator: int | float | "Fraction" = b
        else:
            raise ValueError("The denominator can't be 0")

        if isinstance(a, self.__class__) and isinstance(b, self.__class__):
            self.numerator = a.numerator * b.denominator
            self.denominator = a.denominator * b.numerator
        elif isinstance(a, self.__class__):
            self.numerator = a.numerator
            self.denominator = a.denominator * b
        elif isinstance(b, self.__class__):
            self.numerator = a * b.denominator
            self.denominator = b.numerator
        else:
            self.numerator = a
            self.denominator = b

    def decimal(self) -> int | float:
        return self.numerator / self.denominator

    def pgcd(self) -> int:
        a = self.numerator
        b = self.denominator
        while b != 0:
            a, b = b, a % b
        return a

    def irreducible(self) -> "Fraction":
        pgcd = self.pgcd()
        return Fraction(int(self.numerator / pgcd), int(self.denominator / pgcd))

    def __truediv__(self, other: Union[int, float, "Fraction"]) -> "Fraction":
        if isinstance(other, self.__class__):
            return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
        elif isinstance(other, int or float):
            return Fraction(self.numerator * 1, self.denominator * other)
        else:
            raise ValueError("Can only divide by Fraction or by in and float")

    def __idiv__(self, other: Union[int, float, "Fraction"]) -> "Fraction":
        if isinstance(other, self.__class__):
            return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
        elif isinstance(other, int or float):
            return Fraction(self.numerator * 1, self.denominator * other)
        else:
            raise ValueError("Can only divide by Fraction or by in and float")

    def __rdiv__(self, other: Union[int, float, "Fraction"]) -> "Fraction":
        if isinstance(other, self.__class__):
            return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
        elif isinstance(other, int or float):
            return Fraction(self.numerator * 1, self.denominator * other)
        else:
            raise ValueError("Can only divide by Fraction or by in and float")

    def __mul__(self, other: Union[int, float, "Fraction"]) -> "Fraction":
        if isinstance(other, self.__class__):
            return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        elif isinstance(other, int or float):
            return Fraction(self.numerator * other.numerator, self.denominator * 1)
        else:
            raise ValueError("Can only divide by Fraction or by in and float")

    def __imul__(self, other: Union[int, float, "Fraction"]) -> "Fraction":
        if isinstance(other, self.__class__):
            return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        elif isinstance(other, int or float):
            return Fraction(self.numerator * other.numerator, self.denominator * 1)
        else:
            raise ValueError("Can only divide by Fraction or by in and float")

    def __rmul__(self, other: Union[int, float, "Fraction"]) -> "Fraction":
        if isinstance(other, self.__class__):
            return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        elif isinstance(other, int or float):
            return Fraction(self.numerator * other.numerator, self.denominator * 1)
        else:
            raise ValueError("Can only divide by Fraction or by in and float")

    def __add__(self, other: Union[int, float, "Fraction"]) -> "Fraction":
        if isinstance(other, self.__class__):
            if self.denominator == other.denominator:
                return Fraction(self.numerator + other.numerator, self.denominator)
            else:
                # TODO: Fix this
                if self.denominator is None:
                    self.denominator = 1
                return Fraction(self.numerator * other.denominator + other.numerator * self.denominator,
                                self.denominator * other.denominator)
        elif isinstance(other, int or float):
            return Fraction(self.numerator + other * self.denominator, self.denominator)
        else:
            raise ValueError("Can only divide by Fraction or by in and float")

    def __iadd__(self, other: Union[int, float, "Fraction"]) -> "Fraction":
        if isinstance(other, self.__class__):
            if self.denominator == other.denominator:
                return Fraction(self.numerator + other.numerator, self.denominator)
            else:
                return Fraction(self.numerator * other.denominator + other.numerator * self.denominator,
                                self.denominator * other.denominator)
        elif isinstance(other, int or float):
            return Fraction(self.numerator + other.numerator * self.denominator, self.denominator)
        else:
            raise ValueError("Can only divide by Fraction or by in and float")

    def __radd__(self, other: Union[int, float, "Fraction"]) -> "Fraction":
        if isinstance(other, self.__class__):
            if self.denominator == other.denominator:
                return Fraction(self.numerator + other.numerator, self.denominator)
            else:
                return Fraction(self.numerator * other.denominator + other.numerator * self.denominator,
                                self.denominator * other.denominator)
        elif isinstance(other, int or float):
            # print(other, self.denominator)
            return Fraction(self.numerator + other * self.denominator, self.denominator)
        else:
            raise ValueError("Can only divide by Fraction or by in and float")

    def __sub__(self, other: Union[int, float, "Fraction"]) -> "Fraction":
        if isinstance(other, self.__class__):
            if self.denominator == other.denominator:
                return Fraction(self.numerator - other.numerator, self.denominator)
            else:
                return Fraction(self.numerator * other.denominator - other.numerator * self.denominator,
                                self.denominator * other.denominator)
        elif isinstance(other, int or float):
            return Fraction(self.numerator - other.numerator * self.denominator, self.denominator)
        else:
            raise ValueError("Can only divide by Fraction or by in and float")

    def __repr__(self) -> str:
        return f"<Fraction a:{self.numerator} b:{self.denominator}"

    def __str__(self) -> str:
        if isinstance(self.numerator, self.__class__) and isinstance(self.denominator, self.__class__):
            return f"{self.numerator.numerator * self.denominator.denominator}/" \
                   f"{self.numerator.denominator * self.denominator.numerator}"
        elif isinstance(self.numerator, self.__class__):
            return f"{self.numerator.numerator}/{self.numerator.denominator * self.denominator}"
        elif isinstance(self.denominator, self.__class__):
            return f"{self.numerator * self.denominator.denominator}/{self.denominator.numerator}"
        return f"{self.numerator}/{self.denominator}"
