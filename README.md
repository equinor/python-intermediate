# Warming up

Log into Advent of Code

## Exercises

1. Read a file containing one int per line, make into a list of ints.
1. Solve Day 1


# Function and class decorators

A _decorator_ is a "metafunction"; a way to alter the behavior of a function
that you write.  A decorator can change the behavior completely, change the
inputs, and the return value of the function.

Consider the very simple decorator `timeit` which prints the time a function
uses to return:

```python
@timeit
def fib(n):
    return 1 if n <= 2 else fib(n-1) + fib(n-2)
```

Calling `fib(35)` should result in the following in the terminal:
```
>>> fib(35)
fib took 2.1 sec to complete on input 35
9227465
```

First we observe that
```python
@timeit
def fib(n):
    pass
```
is syntactic sugar for

```python
def fib(n):
    pass
fib = timeit(fib)
```

The main idea is that we implement `timeit` something like this:
```python
def timeit(fib):
    def new_fib(n):
        start = now()
        result = fib(n)
        stop = now()
        print(stop-start)
        return result
    return new_fib
```


## Exercises

1. Create a decorator that hijacks a function, printing and returning
1. Create a decorator that takes a string and hijacks a function, printing the string and returning the string
1. Create a decorator that prints a string before the execution of the original function
1. Create a decorator that takes a string and prints the string before and after the execution of the original function
1. Create a decorator that takes a function as an argument, calls the function before and after the execution of the original function
1. Create a decorator that takes a function `f` and returns `f(val)` where val is the output of the original function
1. Create a class that acts like a decorator (see also callable objects)
1. Use the `decorator` functool.
1. Create a decorator `pushd` that changes `cwd` before and after function call.

# Closures

Explain nested functions and their scope

See the scope of non-local variables

Overwrite the variable in the inner function and see what happens with the variable in the outer function:

```python
def fun():
    a = 1
    def infun():
        a = 2
        print(a)
    infun()
    print(a)
fun()
```

(prints `2` and `1`, obviously)

Now,
```python
def fun():
    a = 1
    def infun():
        nonlocal a
        a = 2
        print(a)
    infun()
    print(a)
fun()
```



## Exercises

1. Create a function that defines an inner function and returns that function
1. Create a function that defines a variable and an inner function and the inner function refers to the variable; return that function
1. Experiment with the keywords `global` and `nonlocal`.
1. Define two variables `a` and `b`, change their value from inside a function.  What happens with `a` and `b`? Try with `global a` later.


# Creating context managers

Show use of `with open`.

What is actually `finally`?

Open file, in the end of function scope close the file.

Open database connection, in the end of function scope close the database connection.

Show a manual context manager.

Show using `@contextlib.contextmanager`.  (show with 0,1,2 `yield` statements)

```python
import contextlib

@contextlib.contextmanager
def mgr():
    print('hello')
    try:
        yield  # yield something
    finally:
        print('goodbye')


def myfun():
    print('pre')
    with mgr():
        x = 1
        print(x)
        int('ca')
        x = 2
        print(x)
    print('post')


myfun()
```


## Exercise

1. Create a context manager using the `contextmanager` decorator
1. Print before and after yield, observe
1. Raise an exception and observe the post-print is present
1. Implement the `pushd` decorator as a context manager.
1. Is it possible to have the name `pushd` as both a decorator and a context manager?
1. Implement `tmpdir` as a context manager.

# Packaging and distribution of Python packages

Introduce _virtual environments_.

Show a small package `xl` and its `setup.py`.

Add tests.

Run `python setup.py build test install`

Show `python setup.py -e install`

Show documentation for [setuptools](https://setuptools.readthedocs.io/en/latest/).

## Exercises

1. Write a module
1. Write a `setup.py` file
1. Create a virtual environment, install package, delete virtual environment
1. Add dependencies to module
1. Show GitHub and `pip install` from GitHub.
1. Install `black` and run on your module.  Why can it be good to use `black` in a project?


# Callable objects, lambdas, and extended argument syntax

Create a class `X`, instantiate an object `x` and try `x()`.

Implement `__call__` on `X`.

Show `lambda x: x**2`, e.g. `sorted([random.randint(-5, 5) for _ in range(10)], key=lambda x: x**2)`

Explain wtf this is: `def f(a, /, b, *, c): pass` (keyword-only arguments, no-pos-only) [`f(1, b=2, c=3)`]

Explain `*args, **kwargs` as params.  Show `zip(*[[1,2,3], 'abc', [3,4,5]])`

Show EBNF: https://docs.python.org/3.9/reference/compound_stmts.html#function-definitions

## Exercises

1. Create a function that takes a list (mutable obj) as default argument.
1. Create a class whose instances are callable.
1. Experiment with `filter`, `map`, `reduce` on `lambda`s.
1. Create functions that take keyword-only arguments.
1. Use `zip` with `*list`.  Explain what happens.
1. Write a decorator that takes arbitrary arguments and keyword arguments.


# Properties, class methods, and static methods

Define a class `Pos` with "private" members `_x` and `_y`.  Explain the
concept of "visibility" and namespaces.

Add _getters_ and _setters_.

Use `@property` decorator.

Explain `__eq__` and `return NotImplemented`


## Exercises

1. Create a Position class with `dist`, `norm`, `__add__`, with `@property`
1. Add `repr`, `str` and `hash`, `eq`
1. Implement the same class with `@dataclass` decorator


# String representations of objects

Explain the difference between `repr` and `str`.

Explain benefits of implementing a good `repr`.


## Exercises

1. Print a Pandas dataframe and a Numpy matrix.
1. Print a function.
1. Print a class (the class, not an object).
1. Create a class and define the `repr` and `str` methods.  What are the differences?
1. Use `str(·)` on the object and observe.
1. Use `repr(·)` on the object and observe.  Conclude.
1. Return non-string in `str`.
1. Print a class.  Which method is being called?
1. Create a class with only one of the two methods, see what happens.


# Specialized numeric and scalar types
# Functional-style programming tools
# The iteration and iterable protocols
# Multiple inheritance, method resolution order, and super()
# Collection protocols and implementing collections
# Advanced error handling with exceptions
# Introspection
