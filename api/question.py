from arg_fetcher import get_arg
from datetime import datetime
from exceptions import *
import math

CORRECT = 1
INCORRECT = 0
ERROR = -1
DEFAULT_MAX_ANSWERS = 2
MAX_CORRECT_ANSWER_POINTS = 100
INCORRECT_ANSWER_POINTS = 0

MICROS_PER_SECOND = 1000000
SECONDS_PER_DAY = 86400
MICROS_ALLOWED = 13 * MICROS_PER_SECOND


class Question:

    def from_dict(question_data):
        options = question_data["options"]
        question_num = question_data["question_num"]
        expected_answer = get_arg(
            question_data, "expected_answer", required=False)

        observed_answers = get_arg(
            question_data, "observed_answers", required=False, default=set())
        if observed_answers is None:
            observed_answers = []

        time_asked_str = get_arg(
            question_data, "time_asked", required=False)
        time_asked = Question._str_to_datetime(time_asked_str)

        time_answered_str = get_arg(
            question_data, "time_answered", required=False)
        time_answered = Question._str_to_datetime(time_answered_str)

        return Question(options, question_num, expected_answer=expected_answer, observed_answers=observed_answers, time_asked=time_asked, time_answered=time_answered)

    def __init__(self, options, question_num, expected_answer=None, observed_answers=None, max_answers=DEFAULT_MAX_ANSWERS, force_answers=False, time_asked=None, time_answered=None):
        self._options = options
        self._question_num = question_num
        self._expected_answer = expected_answer
        self._observed_answers = [] if observed_answers is None else observed_answers
        self._max_answers = max_answers
        self._force_answers = force_answers
        self._time_asked = time_asked if time_asked is not None else datetime.now()
        self._time_answered = time_answered

    # Returns a dictionary summarising the question/answer
    def to_dict(self):
        points = self.points_scored()
        return {
            "options": self._options,
            "question_num": self._question_num,
            "expected_answer": self._expected_answer,
            "observed_answers": self._observed_answers,
            "points": points,
            "potential": MAX_CORRECT_ANSWER_POINTS,
            "time_asked": type(self)._datetime_to_str(self._time_asked),
            "time_answered": type(self)._datetime_to_str(self._time_answered)
        }

    # Checks if the observed answer matches the expected answer.
    # If the question has already been correctly answered, the
    # expected answer will be compared against the previous accepted one
    # Returns the number of points scored.
    def check_answer(self, expected, observed):
        answer_time = datetime.now()

        if expected not in self._options:
            raise AnswerNotFoundError

        if observed not in self._options and self._force_answers:
            raise AnswerNotFoundError

        # If expected does not match the answer previously observed as expected,
        # some error or cheating has occurred.
        if self._expected_answer is not None and expected != self._expected_answer:
            raise AnswerNotFoundError

        self._set_expected_answer(expected)
        self._add_observed_answer(observed)

        if self.answers_match_and_valid(expected, observed):
            self._set_time_answered(answer_time)
        if self.answered_correctly() or expected == observed:
            return CORRECT
        else:
            return INCORRECT

    def answers_match_and_valid(self, expected, observed):
        if self._expected_answer not in (None, expected):
            return False
        elif expected != observed:
            return False
        elif self._force_answers == True and observed not in self._options:
            return False
        else:
            return True

    def points_scored(self):
        points = INCORRECT_ANSWER_POINTS

        if self.answered_correctly():
            try:
                micros_taken = self._micros_between(
                    self._time_asked, self._time_answered
                )
            except TypeError:
                micros_taken = MICROS_ALLOWED

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
        return int(math.ceil(points))

    def get_time_asked(self, format="datetime"):
        if format == "datetime":
            return self._time_asked
        elif format == "string":
            return type(self)._datetime_to_str(self._time_asked)

    def is_finished(self):
        if self.answered_correctly():
            return True
        elif self._max_answers_reached():
            return True
        elif self._time_expired():
            return True
        else:
            return False

    def answered_correctly(self):
        if self._expected_answer in self._observed_answers and self._expected_answer in self._options:
            return True
        else:
            return False

    def has_incorrect_guesses(self):
        if not self.answered_correctly() or len(self._observed_answers) != 1:
            return True
        else:
            return False

    @classmethod
    def _datetime_to_str(cls, dt):
        if type(dt) is not datetime:
            return dt
        return dt.isoformat()

    @classmethod
    def _str_to_datetime(cls, dt_string):
        if dt_string == "None":
            return None
        try:
            return datetime.strptime(dt_string, "%Y-%m-%dT%H:%M:%S.%f")
        except(TypeError):
            return dt_string

    # Sets the _expected_answer after ensuring it isn't set already.
    def _set_expected_answer(self, expected_answer):
        if self._expected_answer is None:
            self._expected_answer = expected_answer

    # Adds the observed_answer after ensuring it's not already picked
    # and the correct answer hasn't been given.
    def _add_observed_answer(self, observed_answer):
        if self.answered_correctly():
            pass
        elif self._max_answers_reached():
            pass
        elif observed_answer in self._observed_answers:
            pass
        elif observed_answer in self._options or not self._force_answers:
            self._observed_answers.append(observed_answer)

    def _max_answers_reached(self):
        if len(self._observed_answers) >= self._max_answers:
            return True
        else:
            return False

    def _set_time_answered(self, answer_time):
        if self._time_answered is None and self.answered_correctly():
            self._time_answered = answer_time

    def _time_expired():
        if self._time_asked is None:
            return None
        else:
            return self._micros_between(self._time_asked, datetime.now()) < MICROS_ALLOWED

    def _micros_between(self, t1, t2):
        diff = t2 - t1
        return (diff.days * SECONDS_PER_DAY * MICROS_PER_SECOND +
                diff.seconds * MICROS_PER_SECOND +
                diff.microseconds)
