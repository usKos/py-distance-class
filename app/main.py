from __future__ import annotations


class Distance:
    # Write your code here
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int) -> Distance:
        if not isinstance(other, Distance):
            other = Distance(other)
        return Distance(
            km=self.km + other.km
        )

    def __iadd__(self, other: Distance | int) -> Distance:
        if not isinstance(other, Distance):
            other = Distance(other)
        self.km = self + other
        return self

    def __mul__(self, other: Distance | int) -> Distance:
        self.km = self.km * other
        return self

    def __truediv__(self, other: Distance | int) -> Distance:

        self.km = round(self.km / other, 2)
        return self

    def __lt__(self, other: Distance | int) -> bool:
        if not isinstance(other, Distance):
            other = Distance(other)
        return self.km < other.km

    def __gt__(self, other: Distance | int) -> bool:
        if not isinstance(other, Distance):
            other = Distance(other)
        return self.km > other.km

    def __eq__(self, other: Distance | int) -> bool:
        if not isinstance(other, Distance):
            other = Distance(other)
        return self.km == other.km

    def __le__(self, other: Distance | int) -> bool:
        if not isinstance(other, Distance):
            other = Distance(other)
        return self.km <= other.km

    def __ge__(self, other: Distance | int) -> bool:
        if not isinstance(other, Distance):
            other = Distance(other)
        return self.km >= other.km
