from typing import Any
from collections import deque


class Stack:

    def __init__(self, maxlen: int = 256) -> None:
        self.capacity = maxlen
        self.__stk = deque([], maxlen)

    def __len__(self) -> int:
        return len(self.__stk)

    def is_empty(self) -> bool:
        return not self.__stk

    def is_full(self)-> bool:
        return len(self.__stk) == self.__stk.maxlen

    def push(self,value:Any) -> None:
        self.__stk.append(value)