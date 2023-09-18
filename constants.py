from enum import Enum


class BaseConst(Enum):
    @classmethod
    def values(cls):
        return [item.value for item in cls]


class BoardSize(BaseConst):
    A = 5
    B = 10
    C = 15
