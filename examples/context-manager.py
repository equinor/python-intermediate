import contextlib


@contextlib.contextmanager
def mgr():
    print("hello")
    try:
        yield  # yield something
    finally:
        print("goodbye")


def myfun():
    print("pre")
    with mgr():
        x = 1
        print(x)
        int("ca")
        x = 2
        print(x)
    print("post")


myfun()
