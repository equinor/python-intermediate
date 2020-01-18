#!/usr/bin/env python
from __future__ import print_function


def parse(fname):
    with open(fname, "r") as fin:
        return [int(x.strip()) for x in fin.readlines()]


def solve1(data):
    return sum(e // 3 - 2 for e in data)


def solve2(data):
    tot = []
    for e in data:
        t = 0
        e = e // 3 - 2
        while e > 0:
            t += e
            e = e // 3 - 2
        tot.append(t)
    return sum(tot)


def main(fname):
    data = parse(fname)

    ans = solve1(data)
    print("Day 1 pt 1", ans)

    ans = solve2(data)
    print("Day 1 pt 2", ans)


if __name__ == "__main__":
    from sys import argv

    if len(argv) < 2:
        exit("Usage: aoc fname")
    main(argv[1])
