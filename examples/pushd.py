import os


def pushd(folder):
    def decorator(func):
        def inner(*args, **kwargs):
            previous_dir = os.getcwd()
            os.chdir(folder)
            result = func(*args, **kwargs)
            os.chdir(previous_dir)
            return result

        return inner

    return decorator


def function1():
    return os.getcwd()


@pushd("/tmp")
def function2():
    return os.getcwd()


def function3():
    return os.getcwd()


if __name__ == "__main__":
    print(function1())
    print(function2())
    print(function3())
