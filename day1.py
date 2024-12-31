from collections import Counter


def parse_input(lines):
    return [list(map(int, l.split("   "))) for l in lines]


def part1(lines):
    pairs = parse_input(lines)
    left = sorted([x[0] for x in pairs])
    right = sorted([x[1] for x in pairs])
    sorted_pairs = zip(left, right)
    return sum(abs(a - b) for a, b in sorted_pairs)


def part2(lines):
    pairs = parse_input(lines)
    right_counter = Counter([x[1] for x in pairs])
    left = [x[0] for x in pairs]
    return sum(right_counter[l] * l for l in left)


if __name__ == "__main__":
    with open("./inputs/day1.txt", encoding="utf-8") as f:
        lines = [l.strip() for l in f.readlines()]
    print("part 1")
    print(part1(lines))
    print("part 2")
    print(part2(lines))
