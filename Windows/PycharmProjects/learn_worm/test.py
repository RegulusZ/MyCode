from selenium import webdriver
from functools import wraps


# def f(name="t1"):
#
#     def test1():
#         return "this is test1"
#
#     def test2():
#         return "this is test2"
#
#     if name == "t1":
#         return test1
#     else:
#         return test2

def hi():
    print("hi!")


def decorator(func):
    @wraps(func)
    def wrap_func(*args, **kwargs):
        if not can_run:
            return "not run"
        return func(*args, **kwargs)
        # print("do sth before")
        # func()
        # print("do sth after")
    return wrap_func


@decorator
def hello():
    print("hello!")


if __name__ == "__main__":
    can_run = True
    hello()
    print(hello())
    # print(hello.__name__)
    # print(hi.__name__)