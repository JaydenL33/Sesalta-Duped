from datetime import datetime

CORRECT = 1
INCORRECT = 0

CORRECT_ANSWER_POINTS = 100
INCORRECT_ANSWER_POINTS = 0


class Question:

    def __init__(self, options):
        self._options = options
        self._expected_answer = None
        self._observed_answer = None
        # self._time_asked = datetime.now()
        # self._time_answered = None

    # Returns a dictionary summarising the question/answer
    def to_dict(self):
        if self._answered_correctly():
            points = CORRECT_ANSWER_POINTS
        else:
            points = INCORRECT_ANSWER_POINTS

        return {
            "points": points,
            "potential": CORRECT_ANSWER_POINTS
        }

    # Checks if the observed answer matches the expected answer.
    # If the question has already been correctly answered, the
    # expected answer will be compared against the previous accepted one
    # Returns the number of points scored.
    def check_answer(self, expected, observed):
        # If expected does not match the answer previously observed as expected,
        # some error or cheating has occurred.
        if self._expected_answer != None and expected != self._expected_answer:
            return INCORRECT

        # Expected and observed answer can only be set once each
        self._set_expected_answer(expected)
        self._set_observed_answer(observed)

        if expected in self._options and observed in self._options and observed == expected:
            return CORRECT
        else:
            return INCORRECT

    # Sets the _expected_answer after ensuring it isn't set already.
    def _set_expected_answer(self, expected_answer):
        if self._expected_answer is None:
            self._expected_answer = expected_answer

    # Sets the _observed_answer variable after ensuring it isn't set already.
    def _set_observed_answer(self, observed_answer):
        if self._observed_answer is None:
            self._observed_answer = observed_answer

    def _answered_correctly(self):
        if self._observed_answer == self._expected_answer and self._observed_answer in self._options and self._expected_answer in self._options:
            return True
        else:
            return False
