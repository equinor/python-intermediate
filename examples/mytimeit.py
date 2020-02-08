import time
import datetime


def timeit(func):
    def myfunc(*args, **kwargs):
        start = datetime.datetime.now()
        result = func(*args, **kwargs)
        stop = datetime.datetime.now()
        print(func.__name__, "took", stop - start)
        return result

    return myfunc


@timeit
def slow(n):
    time.sleep(0.4 + n / 100)
    return n ** 2


print(slow(5))
print(slow(30))


def fibonacchi(m):
    if m <= 1:
        return 1
    return fibonacchi(m - 1) + fibonacchi(m - 2)


@timeit
def fib(n):
    return fibonacchi(n)


print(fib(37))
