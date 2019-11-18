from abc import abstractmethod


class Trophy:

    def __init__(self, game):
        self._game = game

    @abstractmethod
    def game_satisfies():
        pass

    def get_name(self):
        return self._trophy_name

    def to_dict(self):
        date = self._game.get_start_time(format="string")

        return {
            "name": self._trophy_name,
            "date": date
        }


class GameCompletedTrophy(Trophy):

    def __init__(self, game):
        super().__init__(game)
        self._trophy_name = "Finished A Game"

    def game_satisfies(self):
        if self._game.is_finished():
            return True
        else:
            return False


class AllQuestionsCorrectTrophy(Trophy):

    def __init__(self, game):
        super().__init__(game)
        self._trophy_name = "All Questions Correct"

    def game_satisfies(self):
        if self._game.is_finished() and self._game.all_questions_correct():
            return True
        else:
            return False


class NoWrongAnswersTrophy(Trophy):

    def __init__(self, game):
        super().__init__(game)
        self._trophy_name = "No Incorrect Guesses"

    def game_satisfies(self):
        if self._game.is_finished() and not self._game.has_incorrect_guesses():
            return True
        else:
            return False
