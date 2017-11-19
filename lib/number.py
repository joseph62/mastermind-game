
from random import randint
from .guesses import Guess

class Number:
    def __init__(self,size=5):
        if size > 10:
            size = 5
        self._size = size
        possibilities = [str(num) for num in range(10)]
        self._number = []
        while len(self._number) < size:
            self._number.append(
                    possibilities.pop(randint(0,len(possibilities)-1))
                    )

    def __str__(self):
        return "".join(self._number)
    
    __repr__ = __str__

    def compare(self,guess):
        guess = list(guess)[:self._size]
        spades = 0
        fame = 0
        for idx,number in enumerate(guess):
            if number == self._number[idx]:
                fame += 1
            elif number in self._number:
                spades += 1

        return Guess(guess,spades,fame)

    def size(self):
        return self._size

