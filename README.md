# Python intermediate 2 days course

We assume familiarity with all basic types of Python, including `set`, `dict`,
`tuple`, some functional programming tools in Python such as `map`, `filter`,
`zip`, object oriented programming, organization of Python modules as well as
file management.


## Table of contents


1. [Warming up](#warming-up)
1. [The iteration and iterable protocols](#the-iteration-and-iterable-protocols)
1. [Error handling and exceptions](#error-handling-and-exceptions)
1. [Closures](#closures)
1. [Creating context managers](#creating-context-managers)
1. [Packaging and distribution of Python packages](#packaging-and-distribution-of-python-packages)
1. [Callable objects, lambdas, and extended argument syntax](#callable-objects--lambdas--and-extended-argument-syntax)
1. [Decorators](#decorators)
1. [Object oriented programming members](#object-oriented-programming-members)
1. [String representations of objects](#string-representations-of-objects)
1. [Specialized numeric and scalar types](#specialized-numeric-and-scalar-types)
1. [Functional-style programming tools](#functional-style-programming-tools)
1. [Multiple inheritance, method resolution order, and super()](#multiple-inheritance--method-resolution-order--and-super--)
1. [Collection protocols and implementing collections](#collection-protocols-and-implementing-collections)
1. [SQL and `sqlite`](#sql-and--sqlite-)
1. [Test driven development](#test-driven-development)
1. [Python 3.7, 3.8, 3.9 and beyond](#python-37--38--39-and-beyond)
   * [Python 3.7](#python-37)
   * [Python 3.8](#python-38)
   * [Python 3.9](#python-39)


# Warming up

Log into Advent of Code, 2019!

## Exercises

1. Read a file containing one int per line, make into a list of ints.
1. Solve Day 1, parts 1 and 2 of 2019, receiving a _gold star_.
1. [optional] Solve the rest of Advent of Code 2019.

## References

* [Advent of Code 2019, Day 1](https://adventofcode.com/2019/day/1)






# The iteration and iterable protocols

Iterating is one of the most fundamental things we do in programming.  It means
to consider one item at a time of a sequence of items.  The question then
becomes "what is a _sequence_ of items"?

We are certainly familiar with some types of _sequences_, like `range(4)`, or
the list `[0, 1, 2, 3]`, or the tuple `(0, 1, 2, 3)`, and you might know that
strings are sequences of one-character strings.

These are things that we can do the following with:

```python
for element in sequence:
    print(element)
```

But there are more sequences, like sets of the type `set` (which don't have a
pre-determined order), dictionaries (whose sequence becomes a sequence of the
keys in the dictionary).

Whenever we use `for`, `map`, `filter`, `reduce`, list comprehensions, etc.,
Python _iterates_ through an _iterable_.  The _iterable_ is any object that
implements an `__iter__` function (or the `__getitem__`, but we will skip that
for now).

The `__iter__` function returns an _iterator_.  An _iterator_ is any type
implementing `__next__`.  That function returns elements in order, halting the
iteration by returning `StopIteration`.


## Exercises

1. Iterate over lists, sets, strings, tuples
1. Iterate over dicts using raw iteration, over `dict.keys` and `dict.items`
1. Iterate over `dict.items` and `zip` with tuple unpacking
1. Create a class whose instances are iterable.


## References

1. [Iterator types](https://docs.python.org/3/library/stdtypes.html#typeiter)
1. [`iter`](https://docs.python.org/3/library/functions.html#iter)
1. [`next`](https://docs.python.org/3/library/functions.html#next)




# Error handling and exceptions


Any function or method can throw an exception if it likes.  An exception
signals an _exceptional_ situation, a situation that the function does
not know how to deal with.


There is no way to completely avoid such situations: the users can give
the program malformed input, the filesystem or a file on the computer
can be corrupt, the network connection can go down.


**A bit of warning**: Never _ever_ catch an exception you don't know how
to deal with.  A program that crashes is nearly always better than a
program that is wrong but doesn't inform you.  The best is of course to
have a bugfree program, but that is often unattainable; the second best
(since there will be bugs) is a program that crashes on errors,
informing users and developers that something went wrong!

The simplest way to trigger an exception in your terminal is to simply
write `1/0`.  You are asking Python to divide a number by zero, which
Python determines it cannot deal with gracefully, and throws a _division
by zero_ error.

Another easy way to trigger an exception is to run `[][0]`, asking for
the first element of an empty list.  Again, Python doesn't know what to
answer, so throws an `IndexError`.

All exceptions in Python derive from `BaseException`.  For example,
`ZeroDivisionError` in an `ArithmeticError` which in turn is an
`Exception` (which is a `BaseException`).  The `IndexError` derives from
`LookupError` which again is an `Exception`.  The _exception hierarchy_
allows for very fine-grained error handling, you can for example catch
any `LookupError` (`IndexError` or `KeyError` or maybe one you define
yourself?), and avoid catching an `ArithmeticError` in case you don't
know how to deal with such an error.

```python
def throwing():
    raise ValueError('This message explains what went wrong')

throwing()
```

The above will "crash" your Python instance.  We can "catch" the error,
and either suppress it, or throw a different exception, or even re-throw
the same exception:

```python
try:
    throwing()
except ValueError:
    print('Caught an exception')
    #raise  # <-- a single `raise` will re-throw the ValueError
```

To catch the specific error to get its message, we type
`except ValueError as err`,
where `err` is you variable name of choosing.

```python
try:
    throwing()
except ValueError as err:
    print(err.message)
```

**Warning again**: The above is _very bad practice in general; never do
that!!_

`try...finally`: The `try` statement has three optional blocks,
1. `except`,
1. `else`, and
1. `finally`.


**Cleaning up:**  The `finally` block is a block that is always* run.

```python
try:
    raise ValueError()
finally:
    print('Goodbye')
```

Since the `finally` block is always run, you should be very careful with
_returning_ from the finally block.  Quiz: what is returned?
```python
def throwing():
    try:
        return True
    finally:
        return False
```

The only block we haven't considered up until this point is the `else`
block.  The `else` is executed if and only if the `try` block does not
throw an exception.

```python
def throwing(n):
    value = float('inf')
    try:
        value = 1/n
    except ZeroDivisionError:
        print('Division by zero')
    else:
        print('Divided successfully')
    finally:
        print('Returning', value)
    return value
```

Note that if you call `x = throwing('a')`, an exception will leak
through, and the `else` block is skipped, and `x` will remain undefined.


## Exercises

1. Write a program that reads input from the user until the user types
   an integer.  In case the user types a single `q`, the program should
   quit.
1. An `except` clause can have several handlers.  Write a program that
   catches `IndexError` and `ValueError` and does different things
   depending on which error was thrown.
1. Define your own exception class and throw and catch it.

## References

* [Errors and exceptions](https://docs.python.org/3/tutorial/errors.html)
* [Built-in exceptions](https://docs.python.org/3/library/exceptions.html)








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

**Creating functions with special behaviour**

A more typical example for closures is the following

```python
def n_multiplier(n):
    def mul(x):
        return x * n
    return mul

quadruple = n_multiplier(4)
print(quadruple(100))  # prints 400
```




## Exercises

1. Create a function that defines an inner function and returns that function
1. Create a function that defines a variable and an inner function and the inner function refers to the variable; return that function
1. Experiment with the keywords `global` and `nonlocal`.
1. Define two variables `a` and `b`, change their value from inside a function.  What happens with `a` and `b`? Try with `global a` later.
1. Bind up a mutable variable.  Change it outside the function.  Observe the behavior.

# Creating context managers

The use case of context managers is any situation where you find yourself
writing one line of code and thinking "now I need to remember to do
[something]".  The most usual example is the following:

```python
fh = open('file.txt', 'r')  # now I must remember to close it
value = int(fh.readlines()[0])
```

See how easy it is to forget to close `fh`?

Indeed, we can try harder to remember to close it:

```python
fh = open('file.txt', 'r')
value = int(fh.readlines()[0])
fh.close()  # phew, I remembered
```

However, when the `int` raises a `ValueError`, the file isn't closed after all!

How do we deal with this situation?  Well, we have to do the following:

```python
fh = open('file.txt', 'r')
try:
    value = int(fh.readlines()[0])
finally:
    fh.close()  # closes the file even if exception is thrown
```

The above scenario is handled with a _context manager_ which uses the `with`
keyword:

```python
with open('file.txt', 'r') as fh:
    value = int(fh.readlines()[0])
```


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
1. Implement the `open` context manager as `my_open`.
1. Implement the `pushd` decorator as a context manager.
1. Is it possible to have the name `pushd` as both a decorator and a context manager?
1. Implement `tmpdir` as a context manager.

## References

1. [`functools.wraps`](https://docs.python.org/3/library/functools.html#functools.wraps)
1. [`ContextDecorator`](https://docs.python.org/3/library/contextlib.html#contextlib.ContextDecorator)


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

```python
class X:
    pass

x = X()
x()  # raises TypeError: 'X' object is not callable
```

Okay, so `x`, which is of type `X` is not callable.  What is callable?  Clearly
functions, methods, and constructors?  Even `type`s are callable!

Can we create a class of, e.g., _signals_ that you _could_ call?  Yes, indeed, by simply implementing `__call__`:

```python
class Signal:
    def __init__(self, val):
        self.val = val
    def __call__(self):
        return self.val


s = Signal(4)

s()  # returns 4  !
```

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



# Decorators

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

1. Use `lru_cache` to memoize `fib`
1. Create a decorator that hijacks a function, printing and returning
1. Create a decorator that takes a string and hijacks a function, printing the string and returning the string
1. Create a decorator that prints a string before the execution of the original function
1. Create a decorator that takes a string and prints the string before and after the execution of the original function
1. Create a decorator that takes a function as an argument, calls the function before and after the execution of the original function
1. Create a decorator that takes a function `f` and returns `f(val)` where val is the output of the original function
1. Create a class that acts like a decorator (see also callable objects)
1. Use the `decorator` functool.
1. Create a decorator `pushd` that changes `cwd` before and after function call.
1. Use the `singledispatch` functionality from `functools` to _overload_ several functions
1. Think about how you would _implement_ `singledispatch` yourself.
1. Use `functools.wraps` to define a decorator.
1. Write a decorator that takes arbitrary arguments and keyword arguments.


## References

* [functools](https://docs.python.org/3/library/functools.html)




# Object oriented programming members

When we create a class `Pos` with members `x` and `y`, we allow a user to update
`x` and `y` at will.  In other words, it would be totally reasonable for a user
of `Pos` to do the following:

```python
location = Pos(0, 2)
location.x = 1
```

But occasionally, we don't want people to touch our private parts, in which case
we can call a member `_x` (or even `__x`).  This tells the user that if you
modify the content of `_x` (or `__x`), we no longer guarantee that the object
will work as expected.  This is called the _visibility_ of the member `x`.

Now, in Java, one would add two _methods_ (per member) called `getMember` and
`setMember` (in this case `get_x` and `set_x`), but in Python, we can actually
add an object _that appears to be a member_, `x`, but whose altering triggers a
function call.

To make this a more concrete example, consider the class called `Square`, which
has two properties, `width` and `height`.  Obviously, since this is a square,
they should be the same.  So implementing it like this would be a bad idea:
```python
class Square:
    def __init__(self, width, height):
        if width != height:
            raise ValueError('heigh and width must be the same')
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
```

However, a user may do the following:
```python
s = Square(3,3)
s.width = 4
s.get_area()  # returns 12
```

Using private members with _getters_ and _setters_ looks like this, which is much better:

```python
class Square:
    def __init__(self, width, height):
        if width != height:
            raise ValueError('heigh and width must be the same')
        self._width = width
        self._height = height

    def set_width(self, width):
        self._width = width
        self._height = width

    def set_height(self, height):
        self._width = height
        self._height = height

    def get_height(self):
        return self._height

    def get_width(self):
        return self._width

    def get_area(self):
        return self._width * self._height
```

Now, the user cannot make an _illegal square_, unless they access the private
members.

However, the getters and setters belong to the Java community, in Python we can
do something that looks nicer.

```python
class Square:
    def __init__(self, width, height):
        if width != height:
            raise ValueError('heigh and width must be the same')
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width
        self._height = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height
        self._width = height

    @property
    def area(self):
        return self.width * self.height
```

Using the `@property` decorator allows a user to write

```
>>> s = Square(5,5)

>>> s.area
25

>>> s.width
5

>>> s.height
5

>>> s.width = 100

>>> s.area
10000

>>> s.height
100
```

Note that using properties is a great way to make a public member variable
private after users have started to (ab)use your (leaky) implementation!

Other examples where you want to hide your privates are in classes where you
want to keep some additional book-keeping.  For example if you implement a
collection and you allow people to add elements, but you want to keep track of
this.



**Comparing objects**

One interesting thing about our `Square` implementation above, is that if we
make to "identical" objects, `s = Square(10,10)` and `t = Square(10, 10)`, we
can observe that `s != t`.  This is "counter-intuitive" on first sight,
especially since every (both) members of `Square` have the same value.

To be able to compare objects like this (equality), we implement the `__eq__`
method:

```python
class Square:
    # ...
    def __eq__(self, other):
        return self.width == other.width and self.height == other.height
```

This adds the following property to the class:
* squares that are the same are equal
* squares that are not the same are non-equal

Which sounds like all you want.  But it has a bug:

```python
's' == s
```
makes your application crash!

When Python is asked to evaluate `a == b`, it first checks if `a.__eq__(b)`
returns `True` or `False`.  However, `a.__eq__` can choose to return a special
symbol `NotImplemented` which tells Python to instead check `b.__eq__(a)`.

In the case above, `'s' == s`, the `str.__eq__` methods returns
`NotImplemented`, so Python calls `s.__eq__('s')` which in turn checks `s.width
== 's'.width`.  However, the `str` object has no property `width`, so an
`AttributeError` is raised.

Here is a better implementation:

```python
class Square:
    # ...
    def __eq__(self, other):
        if type(self) != type(other):
            return NotImplemented  # leave decision to `other`
        return self.width == other.width and self.height == other.height
```



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

## References

1. [reduce](https://docs.python.org/3/library/functools.html#functools.reduce)





# Multiple inheritance, method resolution order, and super()

A class can inherit from an existing class.  In this instance we call the class
that inherits the _subclass_ of the class it inherits from, the _superclass_.

```python
class A:
    pass

class B(A):
    pass
```

But a class can inherit from several classes:

```python
class C(A, B):
    pass
```

The inheritance order determines the _method resolution order_ of methods calls
on objects.  See `C.__mro__`:

>`(__main__.C, __main__.A, __main__.B, object)`)

Multiple inheritance is too difficult (maybe not for you, but for your
colleagues), so there's rarely a need to use it.


## Exercises

1. Make a class that inherits from two classes.  Test it with several MROs.
1. Create shared variable names, and play with and without `super`




## References

* [Method resolution order](http://python-history.blogspot.com/2010/06/method-resolution-order.html) by Guido






# Collection protocols and implementing collections

We already know what an _iterable_ and an _iterator_ is.  In general,
programming has much to do with collections of things, and our treatment of
these collections.  A _container_ is the most general type of collection, with
only one "requirement", namely that we can ask whether an object `o` is
_contained_ in the container `c`, or in Python: `o in c`.

In Python, a _collection_ is a _sized iterable_.  To be _sized_ means that we
can find out a container's size.  Why couldn't we find out any iterable's size
programmatically?

This question, `in`, can also be asked about _iterables_ and _iterators_.  Why?
How can you implement this `in` for an object you can iterate over?

To make Python be able to answer `in`-questions for your home-made classes, you simple need to implement the method  `__getitem__(self, o)`.

There are many other _specializations_ we could imagine for a container and
iterables.  Some examples:
* We want to iterate backwards: implement `__reversed__`
* We want to know a container's size: implement `__len__`
* Until now, we haven't been able to actually modify a collection: implement `__[get|set|del]item__` and `insert`


## Exercises

1. Implement a function `my_in(iterable, object)` which checks if an object is contained in an iterable.
1. Implement a class that implements the `__getitem__` method.
1. Experiment with the above examples, with `len`, `reversed`, `in`, `iter`, `next`, etc.
1. Implement a `multiset` collection.
1. Implement a linked list.


## References

* [Abstract Base Classes for Containers](https://docs.python.org/3/library/collections.abc.html)













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


_A short note about SQL_: Very often, it may be beneficial to simply go
for an ORM like SQLAlchemy, Peewee, PonyORM, however, before introducing
an ORM in your
project,
[_The Vietnam of Computer Science_](http://blogs.tedneward.com/post/the-vietnam-of-computer-science/)
is mandatory reading.


## Exercises

1. import sqlite3
1. create book database with one table, books, `author`, `year`, `title`, `publisher`, `genre`
1. normalize the database to 1NF, 2NF, 3NF, ...

## References

1. [`sqlite`](https://www.sqlite.org/index.html)
1. [`sqlite3`](https://docs.python.org/3/library/sqlite3.html) (DB-API in Python)
1. ORMs
   1. [SQLAlchemy](https://www.sqlalchemy.org/)
   1. [peewee](https://peewee.readthedocs.io/en/latest/)
   1. [PonyORM](https://ponyorm.org/)
   1. [SQLObject](http://sqlobject.org/)
   1. [O/R Mapping](http://www.agiledata.org/essays/mappingObjects.html)
   1. [_The Vietnam of Computer Science_](http://blogs.tedneward.com/post/the-vietnam-of-computer-science/)

# Test driven development

In test driven development (TDD), we write the tests before writing the actual
implementation.  This helps us create a better design, and to better think about
the problem before starting writing code.

In this session, we will simply solve a bunch of problems, writing as strong
tests as possible before implementing, and seeing how that helps us become
better programmers.

In the real world, TDD is even more beneficial as the design is often
non-trivial, and it can help us design our API.

## Exercises

1. Implement `FizzBuzz` with a test-driven development style
1. Implement `fromroman` that parses a string such as `'vii'` and returns a number, e.g. 7
1. Implement a simple calculator that takes input such as `'2 + (3 * 4)'` and returns its value.  For simplicity, you may use polish notation
1. Write a password strength function that approves or rejects a password if it has or does not have at least one upper and one lower case letter, a non-leading non-trailing digit and a non-leading non-trailing special character.

## References

1. [pytest](https://docs.pytest.org/en/latest/)
1. [unittest](https://docs.python.org/3/library/unittest.html)
1. [travis-ci](https://travis-ci.com/plans)
1. [circleci](https://circleci.com/)


# Python 3.7, 3.8, 3.9 and beyond

It is important to be up to date on changes to the language and as quickly as
possible move on to the newest released runtime.

Therefore it is crucial that everyone who programs Python compiles the
newest version from time to time and test new functionality, and verify
that your old systems still work.

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
