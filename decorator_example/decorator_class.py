# https://realpython.com/primer-on-python-decorators/

import functools


class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)


@CountCalls
def say_whee():
    print("Whee!")


say_whee()
# Call 1 of 'say_whee'
# Whee!

say_whee()
# Call 2 of 'say_whee'
# Whee!

print(say_whee.num_calls)
#2