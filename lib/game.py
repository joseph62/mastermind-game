from .guesses import Guess,Guesses,GuessValidator
from .number import Number

class Mastermind:
    def __init__(self):
        self._guesses = Guesses()
        self._number = Number()
        self._latest_guess = None

    def guess(self,guess):
        guess = str(guess)

        if len(guess) != self._number.size():
            return None

        if GuessValidator.validate(guess):
            result = self._number.compare(guess)
            self._guesses.add(result)
            return result
        else:
            return None

    def show_guesses(self):
        return str(self._guesses)

    def number_size(self):
        return self._number.size()

    def number(self):
        return str(self._number)

    def latest_guess(self):
        return self._guesses.last_guess()
    
class MasterController:
    def __init__(self,game):
        self._game = game

    def move(self,input_):
        if input_ == "!quit":
            return MasterResult.Quit
        elif input_ == "!help":
            return MasterResult.Help
        elif input_ == "!guesses":
            return MasterResult.Guesses
        elif input_ == "!restart":
            return MasterResult.Restart
        else:
            return self.guess(input_)

    def guess(self,guess):
        result = self._game.guess(guess)
        if result is None:
            return MasterResult.BadInput
        elif result.is_correct(self._game.number_size()):
            return MasterResult.Win

        return MasterResult.Continue


class MasterResult:
    BadInput = 0
    Win = 1
    Continue = 2
    Help = 3
    Quit = 4
    Guesses = 5
    Restart = 6
