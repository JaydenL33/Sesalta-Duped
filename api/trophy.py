from abc import abstractmethod


class Trophy:

    @abstractmethod
    def game_satisfies(game):
        pass

    @abstractmethod
    def get_name():
        pass

    def to_dict(game):
        date = game.get_start_time(format="string")
        d["date"] = date

        return {
            "name": self.name,
            "date": date
        }


class AllQuestionsCorrectTrophy(Trophy):

    def get_name():
        return "All Questions Correct"

    def game_satisfies(game):
        if game.is_finished() and game.all_questions_correct():
            return True
        else:
            return False
