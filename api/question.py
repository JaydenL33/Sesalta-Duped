from datetime import datetime

CORRECT = 1
INCORRECT = 0


class Question:

    def __init__(self, options):
        self._options = options
        self._correct_answer = None
        self._answered_correctly = None
        # self._time_asked = datetime.now()
        # self._time_answered = None

    # Checks if the observed answer matches the expected answer.
    # If the question has already been correctly answered, the
    # expected answer will be compared against the previous accepted one
    # Returns the number of points scored.
    def check_answer(self, expected, observed, key="name"):
        values = set([option[key] for option in self._options])

        # If expected does not match the answer previously given as expected,
        # some error or cheating has occurred.
        if self._correct_answer != None and expected != self._correct_answer:
            return INCORRECT

        # Sets the correct answer from expected even if the observed answer
        # is incorrect.
        self._correct_answer = expected

        if expected in values and observed in values and expected == observed:
            self.set_answered_correctly(True)
            return CORRECT
        else:
            return INCORRECT

    # Sets the _answered_correctly variable after ensuring it isn't set already.
    def set_answered_correctly(self, is_correct):
        if self._answered_correctly == None:
            return
        else:
            self._answered_correctly = is_correct
