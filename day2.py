from collections import Counter
from itertools import pairwise


def parse_input(lines):
    return [list(map(int, l.split(" "))) for l in lines]


def is_safe(report):
    is_increase = report[0] < report[-1]
    for a, b in pairwise(report):
        if a == b:
            return 0
        if is_increase and a > b:
            return 0
        if not is_increase and a < b:
            return 0
        if abs(a - b) > 3:
            return 0
    return 1


def is_safe_retry(report):
    if is_safe(report):
        return 1
    for i in range(len(report)):
        i_removed = report[0:i] + report[i + 1 :]
        if is_safe(i_removed):
            return 1
    return 0


def part1(lines):
    reports = parse_input(lines)
    return sum(is_safe(r) for r in reports)


def part2(lines):
    reports = parse_input(lines)
    return sum(is_safe_retry(r) for r in reports)


if __name__ == "__main__":
    with open("./inputs/day2.txt", encoding="utf-8") as f:
        lines = [l.strip() for l in f.readlines()]
    print("part 1")
    print(part1(lines))
    print("part 2")
    print(part2(lines))
