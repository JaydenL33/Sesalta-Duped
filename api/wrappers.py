from datetime import datetime
import functools


def timer(func):
    @functools.wraps(func)
    def wrapper(*args):
        t1 = datetime.now()

        response = func(*args)

        t2 = datetime.now()
        print(
            f"- Function {func.__name__}() ran in:\t{(t2 - t1).total_seconds()} seconds")
        return response
    return wrapper


def mini_timer(func):
    @functools.wraps(func)
    def wrapper(*args):
        t1 = datetime.now()

        response = func(*args)

        t2 = datetime.now()
        print(
            f" - Function {func.__name__}() ran in:\t{(t2 - t1).total_seconds()} seconds")
        return response
    return wrapper

# Testing the wrapper:
# @timer
# def print_wait_print(a, b):
#     print(a)
#     for i in range(10000000):
#         pass
#     print(b)
# print_wait_print("hello", "world")
