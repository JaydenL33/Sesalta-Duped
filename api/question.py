from datetime import datetime
from exceptions import *
import math

CORRECT = 1
INCORRECT = 0
DEFAULT_MAX_ANSWERS = 2
MAX_CORRECT_ANSWER_POINTS = 100
INCORRECT_ANSWER_POINTS = 0


class Question:

    def from_dict(question_data):
        options = question_data["options"]
        question_num = question_data["question_num"]
        expected_answer = question_data["expected_answer"]
        observed_answers = question_data["observed_answers"]
        return Question(options, question_num, expected_answer, observed_answers)

    def __init__(self, options, question_num, expected_answer=None, observed_answers=set() max_answers=DEFAULT_MAX_ANSWERS, force_answers=False):
        self._options = options
        self._question_num = question_num
        self._expected_answer = expected_answer
        self._observed_answers = observed_answers
        self._max_answers = max_answers
        self._force_answers = force_answers
        # self._time_asked = datetime.now()
        # self._time_answered = None

    # Returns a dictionary summarising the question/answer
    def to_dict(self):
        points = self.points_scored()
        return {
            "options": self._options,
            "question_num": self._question_num,
            "expected_answer": self._expected_answer,
            "observed_answers": list(self._observed_answers),
            "points": points,
            "potential": MAX_CORRECT_ANSWER_POINTS
        }

    # Checks if the observed answer matches the expected answer.
    # If the question has already been correctly answered, the
    # expected answer will be compared against the previous accepted one
    # Returns the number of points scored.
    def check_answer(self, expected, observed):
        if expected not in self._options:
            raise AnswerNotFoundError(expected, self._options)

        if observed not in self._options and self._force_answers:
            raise AnswerNotFoundError(observed, self._options)

        # If expected does not match the answer previously observed as expected,
        # some error or cheating has occurred.
        if self._expected_answer is not None and expected != self._expected_answer:
            return INCORRECT

        self._set_expected_answer(expected)
        self._add_observed_answer(observed)

        if expected in self._options and observed == expected:
            return CORRECT
        else:
            return INCORRECT

    def points_scored(self):
        if self._answered_correctly():
            points = min(MAX_CORRECT_ANSWER_POINTS,
                         math.ceil(MAX_CORRECT_ANSWER_POINTS / len(self._observed_answers)))
        else:
            points = INCORRECT_ANSWER_POINTS
        return points

    # Sets the _expected_answer after ensuring it isn't set already.
    def _set_expected_answer(self, expected_answer):
        if self._expected_answer is None:
            self._expected_answer = expected_answer

    # Adds the observed_answer after ensuring it's a valid choice.
    def _add_observed_answer(self, observed_answer):
        if self._answered_correctly():
            return
        if self._max_answers_reached():
            return
        elif observed_answer in self._options or not self._force_answers:
            self._observed_answers.add(observed_answer)

    def _answered_correctly(self):
        if self._expected_answer in self._observed_answers and self._expected_answer in self._options:
            return True
        else:
            return False

    def _max_answers_reached(self):
        if len(self._observed_answers) >= self._max_answers:
            return True
        else:
            return False
