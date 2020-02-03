# Python intermediate 2 days course

Welcome to the Python Intermediate 2 days course for Equinor ASA.  This
entire course is available under the _**Creative Commons** Attribution Share
Alike 4.0 International license_ (cc-by-4.0).

>**You are free to:**
>
>* **Share** — copy and redistribute the material in any medium or
>  format
>* **Adapt** — remix, transform, and build upon the material for any
>  purpose, even commercially.
>
>This license is acceptable for Free Cultural Works.
>
>The licensor cannot revoke these freedoms as long as you follow the
>license terms.
>
>**Under the following terms:**
>
>* **Attribution** — You must give appropriate credit, provide a link to
>  the license, and indicate if changes were made. You may do so in any
>  reasonable manner, but not in any way that suggests the licensor
>  endorses you or your use.
>* **No additional restrictions** — You may not apply legal terms or
>  technological measures that legally restrict others from doing
>  anything the license permits.
>
>**Notices:**
>
> You do not have to comply with the license for elements of the
> material in the public domain or where your use is permitted by an
> applicable exception or limitation.
>
> No warranties are given. The license may not give you all of the
> permissions necessary for your intended use. For example, other rights
> such as publicity, privacy, or moral rights may limit how you use the
> material.




## About this course

This course is an intermediate level course in Python programming.  We
will go through and learn _intermediate_ concepts, and get hands-on
experience with these concepts.  Obviously, reading about topics and
concepts in programming is _never a substitute for programming_!  You
will not be an intermediate level programmer after this course, but you
will have the tools available to become one.

As this is not the basic course in Python,
we _assume familiarity with all basic types_ of Python, including `set`, `dict`,
`tuple`, some functional programming tools in Python such as `map`, `filter`,
`zip`, object oriented programming, organization of Python modules as well as
file management.
We also assume a certain level of programming maturity; the _Warming up_
exercise should be quite feasible.

Most sections have a _reference_ section for further reading, e.g.

> **References**
> 1. [Programming FAQ](https://docs.python.org/3/faq/programming.html)

It is recommended that you take some time to read through the material.




## Table of contents


1. [Warming up](#warming-up)
1. [The iteration and iterable protocols](#the-iteration-and-iterable-protocols)
1. [Error handling and exceptions](#error-handling-and-exceptions)
1. [Closures](#closures)
1. [Creating context managers](#creating-context-managers)
1. [Packaging and distribution of Python packages](#packaging-and-distribution-of-python-packages)
1. [Calling, lambdas, and functions](#calling-lambdas-and-functions)
1. [Decorators](#decorators)
1. [Object oriented programming members](#object-oriented-programming-members)
1. [String representations and format strings](#string-representations-and-format-strings)
1. [Specialized numeric and scalar types](#specialized-numeric-and-scalar-types)
1. [Functional programming](#functional-programming)
1. [Containers ABC](#containers-abc)
1. [SQL and `sqlite`](#sql-and--sqlite-)
1. [Test driven development](#test-driven-development)
1. [Multiple inheritance, method resolution order, and super()](#multiple-inheritance--method-resolution-order--and-super--)
1. [Python 3.7, 3.8, 3.9 and beyond](#python-37--38--39-and-beyond)
   * [Python 3.7](#python-37)
   * [Python 3.8](#python-38)
   * [Python 3.9](#python-39)


# Warming up

Log into [Advent of Code, 2019](https://adventofcode.com/2019)!

To start this course, we will warm up with a very basic exercise in programming.
Start by logging in to your [GitHub](https://github.com) account, and then
proceed to log in to Advent of Code by authenticating yourself using GitHub.

You need to download a file, let's call it `'input'`, and your program should
take the file path as input, i.e., you call your program like this:

```bash
$ python aoc01.py input
<answer>
```

... and out comes your answer.  Remember a proper use of functions, and that you
should use the
`__name__ == '__main__'`
idiom as in all other scripts we write.

(To get it out of the way, the _double underscores_ are pronounced _dunder_.  We
often skip saying the trailing dunder, and we thus pronounce the above idiom as
"_dunder name equals dunder main_".  We will see lots of dunders in this
course.)

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


From the Python manual:

> An object capable of returning its members one at a time. Examples of
> iterables include all sequence types (such as `list`, `str`, and `tuple`) and
> some non-sequence types like `dict`, `file` objects, and objects of any
> classes you define with an `__iter__()` method or with a `__getitem__()`
> method that implements Sequence semantics.
>
> Iterables can be used in a for loop and in many other places where a sequence
> is needed (`zip()`, `map()`, …). When an iterable object is passed as an
> argument to the built-in function `iter()`, it returns an iterator for the
> object. This iterator is good for one pass over the set of values. When using
> iterables, it is usually not necessary to call `iter()` or deal with iterator
> objects yourself. The for statement does that automatically for you, creating
> a temporary unnamed variable to hold the iterator for the duration of the
> loop.





## Exercises

1. Iterate over lists, sets, strings, tuples
1. Iterate over dicts using raw iteration, over `dict.keys` and `dict.items`
1. Iterate over `dict.items` and `zip` with tuple unpacking
1. Create a class whose instances are iterable using `__getitem__`.  Raise `IndexError` when you have no more items.
1. Create a class whose instances are iterators, i.e., implements `__next__` and an `__iter__` that returns itself.  Remember to _raise_ `StopIteration`.


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

Suppose that you want to create the function `int_divide` that always returns an
integer:

```python
def int_divide(a: int, b:int) -> int:
    if b == 0:
        return 0  # ?? ... that's not correct‽
    return a//b
```

Obviously, this is not a good idea, since `3/0 ≠ 0`.  Indeed, `3/0` is
_undefined_, so the function should simply not return a value, but signal an
error.  We could of course push the responsibility over to the callsite and say
that if the user calls this function with illegal arguments, the output is
undefined.  However, this is not always possible.  Consider this scenario:

```python
def count_lines_in_file(filename : str) -> int:
    return len(open(filename, 'r').readlines())
```

But what is the file doesn't exist?  What should we then return?  We could again
try to force the responsibility over to the user, but in this situation, that
would not necessarily work due to possible _race conditions_.

```python
if os.exists(filename):
    # between line 1 and 3, the file could be deleted, the filesystem unmounted
    wc = count_lines_in_file(filename)
```

It is for these situations that exceptions exist.  (Students asking
about _monads_ are kindly asked to leave the premises.)


**A bit of warning**: Never _ever_ catch an exception you don't know how
to deal with.  A program that crashes is nearly always better than a
program that is wrong but doesn't inform you.  The best is of course to
have a bugfree program, but that is often unattainable; the second best
(since there will be bugs) is a program that crashes on errors,
informing users and developers that something went wrong!

Eric Lippert categorises exceptions into four classes:

<dl>
<dt>fatal exceptions</dt>
<dd>Exceptions you cannot do anything about (e.g. out of memory error,
corruption, etc), so do nothing about them</dd>
<dt>boneheaded exceptions</dt>
<dd>Exceptions that you could avoid being raised, such as index errors, name
errors, etc.  Write your code properly so that they are not triggered, and avoid
catching them</dd>
<dt>vexing exceptions</dt>
<dd>Exceptions that arise due often to poorly written library code that are
raised in non-exceptional cases.  Catch them, but it is vexing.</dd>
<dt>exogenous exceptions</dt>
<dd>Exceptions that you need to deal with, such as I/O errors, network errors,
corrupt files, etc.  Try your operation and try to deal with any exception that
comes.</dd>
</dl>


It should be mentioned that in the past, it was considered normal program flow
in Python to use exceptions.  The opinions on this matter is today under debate
with many programmers arguing it to be an _anti-pattern_.  You will often come
across the advise "never use exceptions for program flow".  An experienced
developer can decide for themselves; In this course we recommend using
exceptions for exceptional situations.



**Exception handling in Python**

The simplest way to trigger an exception in your terminal is to simply
write `1/0`.  You are asking Python to divide a number by zero, which
Python determines it cannot deal with gracefully, and throws a _division
by zero_ error.

Another easy way to trigger an exception is to run `[][0]`, asking for
the first element of an empty list.  Again, Python doesn't know what to
answer, so throws an `IndexError`.

All exceptions in Python derive from `BaseException`.  For example,
`ZeroDivisionError` is an `ArithmeticError` which in turn is an
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
* [Vexing Exceptions](https://blogs.msdn.microsoft.com/ericlippert/2008/09/10/vexing-exceptions/)







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

## References

1. [Python data model](https://docs.python.org/3/reference/datamodel.html?highlight=closure)





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

(See the section on _exception handling_ if the `finally` keyword eludes you.)


The above scenario is handled with a _context manager_ which uses the `with`
keyword:

```python
with open('file.txt', 'r') as fh:
    value = int(fh.readlines()[0])
```

Unsurprisingly, there are many more examples where we need to _remember to
release or clean up stuff_.  A couple of examples are
* open a database connection: remember to close it lest we risk losing commits
* acquire a lock: remember to release it lest we get a dead/livelock
* start a web session: forgetting to close might result in temporary lockout
* temporarily modifying state (`pushd` example in exercises)


**The context manager**

A _context manager_ is a class which has the methods
* `__enter__(self)`
* `__exit__(self, type, value, traceback)`

The `__enter__` method is called when the object is used in a context manager
setting, and the return value of `__enter__` can be bound using the `as <name>`
assignment.

Here is how to implement `open(·, 'r')` by ourselves:

```python
class Open:
    def __init__(self, fname):
        self._fname = fname
        self._file = None

    def __enter__(self):
        self._file = open(self._fname, 'r')
        print('\n\nFILE OPENED!\n\n')
        return self._file

    def __exit__(self, type, value, traceback):
        self._file.close()
        print('\n\nFILE CLOSED!\n\n')

with Open('myopen.py') as f:
    print(''.join(f.readlines()))
```

Now, we can force an exception by mis-spelling `readlines` and observe that the
file is actually closed.

```python
with Open('myopen.py') as f:
    print(''.join(f.readxxxlines()))
```


**Defining context manager with `contextlib` decorator**

The `contextlib` library gives us a way to write context managers without
needing to define a class, and without specifying `__enter__` and `__exit__`.

Using the `@contextmanager` decorator, we can create a function that can `yield`
once, and whatever is above the `yield` is interpreted as `__enter__` and
whatever comes after `yield` is interpreted as `__exit__`.  By `yield`-ing a
value, we allow binding in the `as [name]` expression.

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

As a programmer, we constantly need to install packages; this is after all one
of the greatest benefits of open source software.  We all benefit from the
combined efforts of the software community!

At the same time as we would like to install _all the packages_, when doing
actual development, we need to have full control of our _environment_, which
packages do we actually use, which versions of these packages, and which do we
not need?

Especially when we are working on several projects with different requirements,
could this potentially become problematic.  Enter _virtual environments_.


**Virtual environments**

A virtual environment is a what it sounds; it is like a virtual machine that you
can _activate_ (or _enable_), install a lot of packages, and then the packages
are only installed _inside_ that environment.  When you are done, you can
_deactivate_ the environment, and you do no longer see the packages.

_(By the way, a virtual environment is only a folder!)_

There are, in other words, three steps:
1. _create_ a virtual environment
1. _activate_ the virtual environment
1. _deactivate_ the virtual environment

```bash
[trillian@iid ~]$ python3 -m venv my_evn
[trillian@iid ~]$ source my_evn/bin/activate
(my_evn) [trillian@iid ~]$ which python
/home/trillian/my_evn/bin/python
(my_evn) [trillian@iid ~]$ which pip
/home/trillian/my_evn/bin/pip
(my_evn) [trillian@iid ~]$ pip install numpy
Collecting numpy
 ...
Installing collected packages: numpy
Successfully installed numpy-1.18.1
(my_evn) [trillian@iid ~]$ python -c "import numpy as np; print(np.__version__)"
1.18.1
```

### Creating your own (proper) package

A _module_ in Python is a folder with a file named `__init__.py`

We will create a very short package `xl` containing _one_ module called `xl`.
The file tree in our project looks like this:
```
[trillian@iid ~/proj]$ tree
.
├── requirements.txt
├── setup.py
├── tests
│   ├── __init__.py
│   └── test_units.py
└── xl
    └── __init__.py

2 directories, 5 files
```

You can for now ignore the tests, which we will come back to in the section about _Test Driven Development_.

The `setup.py` file is the one that makes Python able to build this as a
package, and it is very simple:

```python
# setup.py
import setuptools

setuptools.setup(
    name='xl',
    packages=['xl'],
    description='A small test package',
    author='Trillian Astra (human)',
)
```

Run `python setup.py install` to install it (remember to activate your virtual
environment first).

## Exercises

1. Create two virtual environments where we install different versions of `numpy`
1. Write a module
1. Write a `setup.py` file
1. Create a virtual environment, install package, delete virtual environment
1. Add dependencies to module (`xlrd`, `pandas`)
1. Implement `entry_points` to call a function in `xl`.
1. Make `xl` read an excel file (input argument) and output its columns.
1. `pip install` a package directly from GitHub.
1. Install `black` and run on your module.  Why can it be good to use `black` in a project?

## References

1. [`venv`](https://docs.python.org/3/library/venv.html)
1. [`setuptools`](https://setuptools.readthedocs.io/en/latest/)
1. [Black](https://black.readthedocs.io/en/stable/)


# Calling, lambdas, and functions

```python
class X:
    pass

x = X()
x()  # raises TypeError: 'X' object is not callable
```

Okay, so `x`, which is of type `X` is not _callable_.  What is callable?
Clearly functions, methods, and constructors?  Even `type`s are callable!

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


### Lambdas

Occasionally we want to create functions, but do not care to name them.  Suppose
for some reason that you would like to pass the _Euclidean distance_ function
into a function call.  Then you could be tempted to do something like this:

```python
def the_function_we_currently_are_in(values, ...):
    def dist(a, b):
        return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

    return do_things(values, dist)
```

However, the _name_ of the function `dist` is not really necessary.  In
addition, it is slightly annoying to write functions inside other functions.  A
_lambda_ is an _anonymous function_, i.e. a function without a name, that we
specify inline.  With a lamda, the function call would look like this:


```python
return do_things(
    values, lambda a, b: math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)
)
```

A lambda expression is an inline function declaration with the form
`lambda [arguments_list] : expression`
and the lambda expression returns a function.

```
>>> type(lambda : None)
function
```

We can assign bind the function to a name as usual:

```
>>> dist = lambda a, b: abs(a - b)
>>> dist(5, 11)
6
```

If we want to sort a list by a special key, e.g. _x²_, we can simply use the
lambda `lambda x: x**2` as input to `sorted`, i.e.

```python
>>> import random
>>>
>>> sorted([random.randint(-5, 5) for _ in range(10)], key=lambda x: x**2)
[-1, 1, 3, 3, 4, -5, -5, 5, -5, 5]
```

_(Note that `sorted` is a *stable* sort in Python ...)_

### Argument syntax

**Varargs, or `*args, **kwargs`.**

You will occasionally need to create functions that are _variadic_, i.e., a
function that takes _any number of arguments_, and in fact, any kind of keyword
argument.  How can we make a function, say, `log`, which could accept both
`log("hello")` and also `log("hello", a, b, c=x, d=y, e=z)` and so on?

Enter _varargs_.  Consider this function:
```python
def summit(v1, v2=0, v3=0, v4=0, v5=0, v6=0, v7=0, v8=0):
    return v1+v2+v3+v4+v5+v6+v7+v8
```
It _almost_ does the work, but not completely.  It only handles eight arguments, and it only handles a few keyword argument.

In Python, we _actually_ implement the function like this:
```python
def summit(v1, *vals):
    return v1 + sum(vals)
```

Now, we can call it like this:

```
>>> summit(2, 3, 4, 5, 6, 7, 8)
35
```

Let's inspect:
```pyton
>>> def summit(v1, *vals):
>>>     print(type(vals))
>>>     return v1 + sum(vals)
>>>
>>>
>>> summit(2, 3, 4, 5, 6, 7, 8)
<class 'tuple'>
35
```

As you can see, `vals` becomes a `tuple` of the values the user provides.

However, it doesn't fix all our problems:
```
>>> summit(2, x=2)
TypeError: summit() got an unexpected keyword argument 'x'
```

For this, we use the `**` operator:
```python
def summit(v1, *vals, **namedvals):
    return v1 + sum(vals) + sum([val for _,val in namedvals.items()])
```

Calling it:
```
>>> summit(2, 3, 4, x=2, y=1000)
1011
```


You can also do the _"opposite"_, namely using the `*` and `**` operators on the
_callsite_.  Recall our `dist(a, b)` from above.  If we have a list
`pair = [Pos(1,0), Pos(0,1)]`,
we can call `dist` simply like this: `dist(*pair)`.

You will very often see `zip` being called with the `*` operator, we leave the
decoding of this as an exercise to the reader.



**Keyword-only**

In Python 3.6, the _asterisk_ keyword-only symbol `*` as a separator between the
parameters and the keyword-only parameters.  A _keyword-only parameter_ is a
parameter that has to be given to a function with the keyword:

The following function call uses keyword-only arguments in the call:
```python
dist(a=Pos(0,1), b=Pos(1,0))
```

As opposed to this call which uses _positional_ arguments:

```python
dist(Pos(0,1), Pos(1,0))
```

To _force_ the user to call functions with keyword-only arguments, we use the
asterisk:

```python
def dist(a, b, *, scalar):
    return scalar * math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)
```

Now Python would not allow you to call this function with positional-only
arguments; `scalar` _has_ to be declared using the keyword:

```python
>>> dist(Pos(1,0), Pos(0,1), 2.71828)
#  TypeError: dist() takes 2 positional arguments but 3 were given
```

```python
>>> dist(Pos(1,0), Pos(0,1), scalar=2.71828)
3.844228442327537
```

**Positional-only**

In Python 3.8, they extended the idea about _keyword-only_ parameters to also
include _positional-only_ parameters.

The idea is then that it could be made illegal to call
`dist(a = Pos(1,0))`
forcing the user to call the function without the keyword, in other words,
`dist(Pos(1,0))`.

Similar to the _asterisk_, the _slash_ is being used as a delimiter between the _positional-only_, and the _no-positional-only_.

```python
def dist(a, b, /):
    ...
```

Combining the two ideas, yields this result:
```python
def dist(a, b, /, *, scalar):
    return scalar * math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)
```

Now, the only way to call `dist` is as `dist(p1, p2, scalar=val)`.



## Exercises

1. Create a function that takes a list (mutable obj) as default argument.
1. Create a class whose instances are callable.
1. Experiment with `filter`, `map`, `reduce` on `lambda`s.
1. Create functions that take keyword-only arguments.
1. Experiment with things like this: `zip(*[[1,2,3], 'abc', [3,4,5]])`
1. Spell out in detail what happens here:
   ```
   >>> zip( *[(1,2), (3,4), (5,6)] )
   [(1, 3, 5), (2, 4, 6)]
   >>> zip( [(1,2), (3,4), (5,6)] )
   [((1, 2),), ((3, 4),), ((5, 6),)]
   ```



## References

1. [EBNF](https://docs.python.org/3/reference/compound_stmts.html#function-definitions)
1. [varargs](https://docs.python.org/3/reference/expressions.html#calls)
1. [positional-only](https://docs.python.org/3/faq/programming.html#faq-positional-only-arguments)

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


# String representations and format strings

When you try to `print` an object `obj`, Python calls `str(obj)`, which
looks for _two_ functions, in order:

* `__str__`
* `__repr__`

The former function, `__str__` is meant to provide a _string representation_ of
an object that is _usable for an end user_.  The `__str__` function may choose
to discard parts of the state of `obj`, and try to make the string "nice to look
at".

However, the latter function, `__repr__` is meant as a _debugging string
representation_, and is intended for developers to look at.  If possible, it is
a good idea to make the object constructable using only the information provided
by `__repr__`.  The `__repr__` function can explicitly be called by using the
built-in associated function `repr`.

Take a look at how Python implements `__str__` and `__repr__` for `datetime`:

```python
import datetime
now = datetime.datetime.now()

str(now)
# '2020-02-03 09:03:43.147668'

repr(now)
# 'datetime.datetime(2020, 2, 3, 9, 3, 43, 147668)'
```

Observe that the latter returns a string that you could actually `eval`
(warning: bad practice), and which would return an identical object (see also:
`__eq__`).


```python
now == eval(repr(now))
#  True
```

**Format strings**

You have probably seen that it is possible to _concatenate_ two strings using `+`:

```python
'Hello, ' + 'world'
#  'Hello, world'
```

You should also have seen that it is possible to use the _string modulo
operator_ `%`:

```python
name = 'Arthur Dent'
print('Hello, %s, how are you?' % name)
# Hello, Arthur Dent, how are you?
```

The modulo operator introduces its own mini-language for dealing with
_integers_, _floating point numbers_ (e.g. rounding), for padding and centering
strings, etc.

```python
print('Integer: %2d, rounding float: %3.2f' % (1, 3.1415))
#  Integer:  1, rounding float: 3.14
print('Percent: %.2f%%, (E/e)xponential: %5.2E' % (2.718281828459045, 149597870700))
#  Percent: 2.72%, (E/e)xponential: 1.50E+11
```

However, the _modulo_ operator gets confusing to work with when you have many
arguments, and especially if some arguments are repeated.  That is why the
_format strings_ where introduced:

```python
print('Here x is {x}, and x*y, {x}*{y} = {mulxy}'.format(x=2, y=3, mulxy=2*3))
#  Here x is 2, and x*y, 2*3 = 6
```

As you can see, it supports _repeated_ arguments, and the arguments do not have
to be in the same order:
```python
print('a = {a}, b = {b}'.format(b=4.12, a='A'))
#  a = A, b = 4.12
```
It even nicely handles different types.

Occasionally (predominantly while debugging), we can even throw our entire
environment into the format string:

```python
print('x={x}, y={y}, a={a}'.format(**locals()))
#  'x=12, y=13, a=A str'
```

However, this is not good practice.

**`f`-strings**

As of Python 3.6, we get something which is _even nicer_ than _format strings_,
namely **`f`-strings**.  When prefixing a string with a single `f`, you ask
Python to replace all _expressions_ in `{·}` with the evaluated expression:

```python
x = 3.14
out = f'Here x is {x}, and x**2 is {x**2}'
print(out)
#  Here x is 3.14, and x**2 is 9.8596
```

This is very convenient to write, and even more convenient to read, as we now
can read everything _inline_ and do not have to jump back and forth between
braces and the format arguments.

You can even see now how easy it is to make nice `__str__` and `__repr__`
strings by just writing:

```python
    def __repr__(self):
        return f'Class(a={self.a}, b={self.b})'
```

Note that by default, `f`-strings use `str`, but can be forcesd to use `repr` by
specifying the conversion flag `!r` (recall `now` from above):

```python
f'{now}'
#  '2020-02-03 09:05:54.206678'
f'{now!r}'
#  'datetime.datetime(2020, 2, 3, 9, 5, 54, 206678)'
```

And of course, you can use the same type specifiers with `f`-strings to limit
the number of decimals using a single `:` in the expression:

```python
e = 2.718281828459045
f'{e:.5f}'
#  '2.71828'
```

Finally, [in Python 3.8, f-strings support = for self-documenting expressions
and debugging]
(https://docs.python.org/3/whatsnew/3.8.html#f-strings-support-for-self-documenting-expressions-and-debugging).
Notice how the returned string prints the variable name as well.

```python
x = 3.14
y = 2.71828
a = 'A str'
print(f'My vars are {x=}, {y=}, {a=}')
#  My vars are x=3.14, y=2.71828, a='A str'
```


## Exercises

1. Print a Pandas dataframe and a Numpy matrix.
1. Print a function.
1. Print a class (the class, not an object).
1. Create a class and define the `repr` and `str` methods.  What are the differences?
1. Use `str(·)` on the object and observe.
1. Use `repr(·)` on the object and observe.  Conclude.
1. Center a short string using `f`-strings, pad left using `f`-strings.
1. Return non-string in `str`.
1. Print a class.  Which method is being called?
1. Create a class with only one of the two methods, see what happens.
1. Create a very simple `Complex` class and implement `__eq__`, `__str__`, and
   `__repr__`.  Ensure that `eval(repr(c)) == c`.

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



# Functional programming

In _functional programming_ we put a higher focus on input and output of
functions, with little _storing_ of information.  We are familiar with
many examples that are "purely functional", e.g. `dist(a, b) →
abs(a-b)`, `max`, `+`, etc.  These functions take some argument, and
return a new value without modifying the input argument.

Here is a non-functional example:
```python
def __iadd__(a: Pos, b: Pos) -> None:
    a.x += b.x
    a.y += b.y
```

Here is the functional "equivalent":
```python
def __add__(a: Pos, b: Pos) -> Pos:
    return Pos(a.x + b.x, a.y + b.y)
```

While both examples are easy to grasp and understand, the latter is much
simpler to reason about; In the second example, the _state_ never
changes.  This makes the second version much easier to test as well!

An object which can be modified (like in the first example) is called a
_mutable_ object.  The problem with mutable objects in Python is that
you never really know who holds a reference to the object, which means
that the object can be modified right under your own nose from far away.

An object which cannot be modified is called _immutable_.  You will
experience that immutable data is much easier to reason about and to
deal with.  An immutable object can safely be passed around to other
functions and threads without worrying that they might change its
content.

As a correctness-focused developer you should strongly prefer immutable
data structures over mutable.  Your code will be safer with fewer bugs,
easier to understand, and easier to test.

Notice that even though a tuple is _immutable_, if its data is
_mutable_, the tuple will only be reference-immutable: it will forever
point to the same objects, but the object may be changed (under your
nose).

```
>>> l = [1,2,3]
>>> t = (0, l, 4)
>>> print(t)
(0, [1, 2, 3], 4)
>>> l[0] = 5
>>> print(t)
(0, [5, 2, 3], 4)
```

In this example, the _list_ `l` is the "same" list, but, being mutable,
its content changed.


**Tuples**

You should by now be aware of the `tuple` type: the _"immutable list"_.
A tuple behaves the same as a list, it is iterable, it has an order, you
can slice, etc, just as you would with a list.  However, a tuple cannot
be changed once it is created:

```python
>>> t = (1,2,3)
>>> t[0] = 0
TypeError: 'tuple' object does not support item assignment
```

You can neither change its content, nor its size.  A tuple is a great
way to store _vectors_ and other short lists that you do not want
changed.  However, once you start adding more data, it can become
problematic.  Suppose that you decide to store Employees as tuples:

```python
employee = ('Alice', 1980, 'junior software developer')
# must remember which index corresponds to which field
position = employee[1]  # d'oh
```

As you can see, it becomes difficult to remember how to interpret the
tuple.  Enter `namedtuple`.  The `namedtuple` is a very neat data
structure which is essentially a tuple, but instead of using indices as
keys to look up, we pick our own names:

```python
from collections import namedtuple
Employee = namedtuple('Employee', ['name', 'date_of_birth', 'position'])
alice = Employee('Alice', 1980, 'senior software developer')
position = alice.position
```

You can even see that due to her use of `namedtuple`, Alice has been
promoted.  Being immutable, we cannot change the content of the tuple:

```python
alice.position = 'fired'
AttributeError: can't set attribute
```



**Keys of a dictionary**

There is another reason for why immutability of a data structure is
good; the _hash_ function.  Hashing an object is a way of assigning a
unique* integer value to an object:

```python
>>> hash("hello")
-8980137943331027800
>>> hash("hellu")
-3140687082901657771
```

This makes it possible to create a very simple way of making a set, or
hash maps (aka dictionary).  This (homemade) set has _O(1)_ (constant
time) lookup, insertion, and deletion.  We leave it as an exercise to
the reader to fix bugs and complete the implementation with `__len__`
and `__repr__`.  The latter function should make it clear why this set
is "unordered".

```python
class Set:
    _size = 127

    def __init__(self):
        self._data = [None for _ in range(Set._size)]

    def add(self, elt):
        self._data[hash(elt) % Set._size] = elt

    def remove(self, elt):
        self._data[hash(elt) % Set._size] = None

    def __contains__(self, elt):
        return self._data[hash(elt) % Set._size] is not None
```

This implementation of `set` works very well (except for the bugs), and
see what happens if we try to add a tuple, a string and a list:

```python
s = Set()
s.add('hello')
print(s)
s.add((1,2,3))
print(s)
s.add([4])
```

output:
```python
Set(['hello'])
Set(['hello', (1, 2, 3)])
TypeError: unhashable type: 'list'
```


**Command–query separation**

Since we occasionally need to work with mutable data, it can be good to
try to write your functions and methods so that they are of one of two
types, either a command, or a query.  In QCS, a _command_ is a function
which changes its input data, and does not return anything, whereas a
_query_ is a function which returns a value, but does not moduify its
input data.

As with functional programming and immutable data, query functions are
much simpler to reason about, and to test.  They are also "completely
safe" to call; Since there are no side-effects, there can be no
_unintended_ side-effects.

There are examples where it's beneficial to write a function that both
modifies its input and returns a value (such as `pop`), but it can very
often be avoided.


**Fluent style programming**

There is a programming style referred to as _fluent programming_ that
allows for very smooth creation and "modification" of objects, at the
same time improving readability.  In this style, you always _return_ an
object (even if it is the same object you got as input) to enable
_chaining_ of operations.  An API that allows for this chaining is
called a _fluent interface_.

Suppose that you have an SQL-like query object where you want to select,
order, limit, and modify the data.  In a "traditional" style, you would
do something like this (pseudocode):

```python
data = select("*")
only_cats = data.where("type = cat")
ascending_cats = only_cats.order_by("age")
youngest_cats = ascending_cats.limit(10)
result = youngest_cats.filter(str.upper)
```

Although the example is contrived, the following _fluent style_ example
illustrates the idea behind a fluent interface.  Suppose that all
function calls above returned a new query instance:

```python
result = (
    select("*")
    .where("type = cat")
    .order_by("age")
    .limit(10)
    .filter(str.upper)
)
```

It is not only easier to read and understand, but it neither overwrites
any variables, nor does it introduce any "temporary" variables.



## Exercises

1. Use `namedtuple` for a `Pos` type
1. Implement the `Pos` class immutable.
1. Implement the `Pos` class immutable using `dataclasses`, add `__add__` and `distance` (Euclidean).
1. Create lists `a = b = [1,2,3]` and experiment with `a.append` and `b.append`.
1. Complete the implementation of `Set` with `__len__` and `__repr__` and make it _iterable_.
1. Fix the obvious bug in `Set`.  (Hint: `for i in range(128): s.add(i)`.  Is `1000 in s` true?)
1. Make your own implementation of `Dictionary`.
1. Implement a fluent interface for a light bulb with properties hue, saturation, and lightness.

## References

1. [reduce](https://docs.python.org/3/library/functools.html#functools.reduce)
1. [fluent interface](https://www.martinfowler.com/bliki/FluentInterface.html)
1. [dataclasses](https://docs.python.org/3/library/dataclasses.html)










# Containers ABC

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


**Data Access Object**

When working with data, the data is almost always stored in a way which is not
easy to work with as an end-user and higher-order programmer.  For example, to
find a specific book, you need specified join and select queries, sometimes also
pagination.  If you don't take care to design an API, before you start coding,
you might find that your query strings (SQL) are scattered around your entire
project, making it hard (and error prone) to change the design of your database.

A _data access object_ (DAO) is an API that makes your data model concrete by
abstracting away all the SQL specific tasks.  This also makes it possible to
easily change from (e.g.) SQLite to Postgres, or even to a completely different
backend like a different API or a file.  The DAO is a clear separation between the data backend and the more abstract functionality.


## Exercises

1. import `sqlite3`
1. create book database with one table, books, `author`, `year`, `title`, `publisher`, `genre`
1. create a DAO for the book database
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


Copyright 2020 Equinor ASA, (cc-by-4.0)
