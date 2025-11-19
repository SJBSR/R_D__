# Creating my first decorator in Python

def my_decorator(func):
    def wrapper():
        print(f"Running {func.__name__} function")
        func()
        print("Completed")
    return wrapper

@my_decorator
def do_this():
    print("Doing this")

@my_decorator
def do_that():
    print("Doing that")

do_this()
do_that()