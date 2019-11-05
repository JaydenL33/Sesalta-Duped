from datetime import datetime
from exceptions import *
import math

CORRECT = 1
INCORRECT = 0
DEFAULT_MAX_ANSWERS = 2
MAX_CORRECT_ANSWER_POINTS = 100
INCORRECT_ANSWER_POINTS = 0

MICROS_PER_SECOND = 1000000
SECONDS_PER_DAY = 86400
MICROS_ALLOWED = 20 * MICROS_PER_SECOND


class Question:

    def __init__(self, options, question_num, max_answers=DEFAULT_MAX_ANSWERS, force_answers=False):
        self._options = options
        self._question_num = question_num
        self._expected_answer = None
        self._observed_answers = set()
        self._max_answers = max_answers
        self._force_answers = force_answers
        self._time_asked = datetime.now()
        self._time_answered = None

    # Returns a dictionary summarising the question/answer
    def to_dict(self):
        points = self.points_scored()
        return {
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
        answer_time = datetime.now()

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
            self._set_time_answered(answer_time)
            return CORRECT
        else:
            return INCORRECT

    def points_scored(self):
        points = INCORRECT_ANSWER_POINTS

        if self._answered_correctly():
            micros_taken = self._micros_between(
                self._time_asked, self._time_answered
            )
            fraction_time_remaining = 1 - (micros_taken / MICROS_ALLOWED)

            points = (MAX_CORRECT_ANSWER_POINTS *
                      fraction_time_remaining /
                      len(self._observed_answers))

            # Additional checks to ensure that the score is in the allowed range
            if points > MAX_CORRECT_ANSWER_POINTS:
                points = MAX_CORRECT_ANSWER_POINTS

            elif points < INCORRECT_ANSWER_POINTS:
                points = INCORRECT_ANSWER_POINTS

        # Allow for rounding up before casting to int
        return math.ceil(round(points, 0))

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

    def _set_time_answered(self, answer_time):
        if self._time_answered is None and self._answered_correctly():
            self._time_answered = answer_time

    def _micros_between(self, t1, t2):
        diff = t2 - t1
        return (diff.days * SECONDS_PER_DAY * MICROS_PER_SECOND +
                diff.seconds * MICROS_PER_SECOND +
                diff.microseconds)
