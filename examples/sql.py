#!/usr/bin/env python
from __future__ import print_function
import contextlib
import sqlite3
import os.path
from collections import namedtuple


def exit_with_usage():
    msg = """\
Usage: sql title author year publisher
       sql --list
"""
    exit(msg)


Book = namedtuple("Book", "title author year publisher")

DB_FILE = ".books.db"


def _dao_create():
    create_str = ", ".join("{} text".format(field) for field in Book._fields)

    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    with conn:
        c.execute(
            """CREATE TABLE books
            (title text, author text, year text, publisher text)"""
        )
        conn.commit()


@contextlib.contextmanager
def dao():
    if not os.path.isfile(DB_FILE):
        _dao_create()
    conn = sqlite3.connect(DB_FILE)
    try:
        yield conn.cursor()
        conn.commit()
    finally:
        conn.close()


def dao_add(book):
    with dao() as cursor:
        design = "('{}','{}','{}','{}')".format(*book)
        cursor.execute("INSERT INTO books VALUES {}".format(design))


def dao_list():
    with dao() as cursor:
        cursor.execute("""SELECT * FROM books;""")
        rows = cursor.fetchall()
    for row in rows:
        yield Book(*row)


def run_list():
    for b in dao_list():
        print(b)


def main(title, author, year, publisher):
    book = Book(title, author, year, publisher)
    dao_add(book)


if __name__ == "__main__":
    from sys import argv

    if len(argv) < 2:
        exit_with_usage()
    if "--list" in argv:
        run_list()
    else:
        main(*argv[1:])
