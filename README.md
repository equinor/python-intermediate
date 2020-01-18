# Python intermediate 2 days course

We assume familiarity with all basic types of Python, including `set`, `dict`,
`tuple`, some functional programming tools in Python such as `map`, `filter`,
`zip`, object oriented programming, organization of Python modules as well as
file management.


## Table of contents


- [Warming up](#warming-up)
- [Function and class decorators](#function-and-class-decorators)
- [Closures](#closures)
- [Creating context managers](#creating-context-managers)
- [Packaging and distribution of Python packages](#packaging-and-distribution-of-python-packages)
- [Callable objects, lambdas, and extended argument syntax](#callable-objects--lambdas--and-extended-argument-syntax)
- [Properties, class methods, and static methods](#properties--class-methods--and-static-methods)
- [String representations of objects](#string-representations-of-objects)
- [Specialized numeric and scalar types](#specialized-numeric-and-scalar-types)
- [Functional-style programming tools](#functional-style-programming-tools)
- [The iteration and iterable protocols](#the-iteration-and-iterable-protocols)
- [Multiple inheritance, method resolution order, and super()](#multiple-inheritance--method-resolution-order--and-super--)
- [Collection protocols and implementing collections](#collection-protocols-and-implementing-collections)
- [Advanced error handling with exceptions](#advanced-error-handling-with-exceptions)
- [SQL and `sqlite`](#sql-and--sqlite-)
- [Python 3.7, 3.8, 3.9 and beyond](#python-37--38--39-and-beyond)
  * [Python 3.7](#python-37)
  * [Python 3.8](#python-38)
  * [Python 3.9](#python-39)


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

```python
>>> 1.2 - 1.0
0.19999999999999996
```


We know the `bool`, `int`, `float` (and `None`?) types.

There are also the `complex`, `decimal`, and `fraction`

> Squeezing infinitely many real numbers into a finite number of bits requires
> an approximate representation.
>
> — What Every Computer Scientist Should Know About Floating-Point Arithmetic.


* `complex(1,2)` creates the number _1 + 2i_ (denoted `(1+2j)`)
* `c.conjugate()` gives the complex conjugate
* `decimal.Decimal(1.1)` → `Decimal('1.100000000000000088817841970012523233890533447265625')`
* `fractions.Fraction(42,12)` → `Fraction(7, 2)`



# Functional-style programming tools

* Query-command separation

Why is query good?

* Immutable types

Why is immutability good?

A dictionary can only hold immutable types.  Why?

Introduce `namedtuple`.

## Exercises

1. Use `namedtuple` for a `Pos` type
1. Implement the `Pos` class immutable




# The iteration and iterable protocols
# Multiple inheritance, method resolution order, and super()
# Collection protocols and implementing collections
# Advanced error handling with exceptions

# SQL and `sqlite`

SQL, or Structured Query Language, is a language for reading from and writing to
databases, which usually are collections of tables of data, and the data we are
reading and writing are relational data, meaning that there exists relations
within the database we are interested in.

Python comes bundled with
[`sqlite3`](https://docs.python.org/3/library/sqlite3.html),
a wrapper around the public domain database `sqlite`.  This database is a
_local_ database living exclusively in a file on your file system.


```python
import sqlite3
conn = sqlite3.connect('example.db')
```

```python
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
```

The data you’ve saved is persistent and is available in subsequent sessions:

```python
import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
```


## Exercises

1. import sqlite3
1. create book database with one table, books, `author`, `year`, `title`, `publisher`, `genre`
1. normalize the database to 1NF, 2NF, 3NF, ...





# Python 3.7, 3.8, 3.9 and beyond

It is important to be up to date on changes to the language and as quickly as
possible move on to the newest released runtime.

## Python 3.7
* PEP 539, new C API for thread-local storage
* PEP 545, Python documentation translations
* New documentation translations: Japanese, French, and Korean.
* PEP 552, Deterministic pyc files
* PEP 553, Built-in breakpoint()
* PEP 557, Data Classes
* PEP 560, Core support for typing module and generic types
* PEP 562, Customization of access to module attributes
* PEP 563, Postponed evaluation of annotations
* PEP 564, Time functions with nanosecond resolution
* PEP 565, Improved DeprecationWarning handling
* PEP 567, Context Variables
* Avoiding the use of ASCII as a default text encoding (PEP 538, legacy C locale coercion and PEP 540, forced UTF-8 runtime mode)
* The insertion-order preservation nature of dict objects is now an official part of the Python language spec.
* Notable performance improvements in many areas.

## Python 3.8

* PEP 572, Assignment expressions
* PEP 570, Positional-only arguments
* PEP 587, Python Initialization Configuration (improved embedding)
* PEP 590, Vectorcall: a fast calling protocol for CPython
* PEP 578, Runtime audit hooks
* PEP 574, Pickle protocol 5 with out-of-band data
* Typing-related: PEP 591 (Final qualifier), PEP 586 (Literal types), and PEP 589 (TypedDict)
* Parallel filesystem cache for compiled bytecode
* Debug builds share ABI as release builds
* f-strings support a handy = specifier for debugging
* continue is now legal in finally: blocks
* on Windows, the default asyncio event loop is now ProactorEventLoop
* on macOS, the spawn start method is now used by default in multiprocessing
* multiprocessing can now use shared memory segments to avoid pickling costs between processes
* typed_ast is merged back to CPython
* LOAD_GLOBAL is now 40% faster
* pickle now uses Protocol 4 by default, improving performance

## Python 3.9

Lots of security improvements, documentation enhancements, optimizations, some deprecations...

* `dict1 | dict2` or `dict1 + dict2` (under discussion)

TBA
