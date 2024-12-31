from collections import Counter
import re


def part1(memory):
    r = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(r, memory)
    return sum(int(m[0]) * int(m[1]) for m in matches)


def part2(memory):
    split_do = memory.split("do()")
    do_blocks = [d.split("don't()")[0] for d in split_do]
    return sum(part1(d) for d in do_blocks)


if __name__ == "__main__":
    with open("./inputs/day3.txt", encoding="utf-8") as f:
        memory = f.read()
    print("part 1")
    print(part1(memory))
    print("part 2")
    print(part2(memory))
