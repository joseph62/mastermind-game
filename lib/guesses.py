import re

class Guess:
    def __init__(self,guess,spades,fame):
        self._guess = guess
        self._spades = spades
        self._fame = fame

    def __str__(self):
        return "{} - Spades: {} Fame: {}".format(
                "".join(self._guess),
                self._spades,
                self._fame
                )
    __repr__ = __str__

    def is_correct(self,size):
        return self._fame == size

class Guesses:
    def __init__(self):
        self._guesses = []

    def add(self,guess):
        self._guesses.append(guess)

    def last_guess(self):
        if len(self._guesses) == 0:
            return None
        return self._guesses[-1]

    def __str__(self):
        results = ["Guesses:"]
        for guess in self._guesses:
            results.append(str(guess))

        return "\n".join(results)

class GuessValidator:
    def validate(guess):
        match = re.match("^[0-9]+$",guess)
        if match is not None:
            return True
        return False
