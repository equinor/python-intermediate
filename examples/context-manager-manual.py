#!/usr/bin/env python
from __future__ import print_function
try:
    from collections.abc import Container
except ImportError:
    from collections import Container

class _universe:
    def __contains__(self, _):
        return True
UNIVERSE = _universe()

class DummyManager:

    def __init__(self, suppress=None):
        if not suppress:
            self.suppress = []
        elif suppress is True:
            self.suppress = UNIVERSE
        elif isinstance(suppress, Container):
            self.suppress = suppress
        else:
            raise ValueError('suppress must be bool or container')

    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print('exit')
        if exc_type in self.suppress:
            return True

def main():
    with DummyManager() as dm:
        pass
    with DummyManager(True) as dm:
        raise Exception()
    with DummyManager([ValueError]) as dm:
        raise ValueError()
    with DummyManager([IndexError, KeyError]) as dm:
        raise KeyError()
    with DummyManager([IndexError, KeyError]) as dm:
        raise ValueError()

if __name__ == '__main__':
    main()
