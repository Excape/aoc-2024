word_to_search = "XMAS"
directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, 1), (1, -1)]


def search_pos(lines, y, x, dy, dx):
    yw, xw = y, x
    for c in word_to_search:
        if yw < 0 or xw < 0:
            return False
        try:
            if lines[yw][xw] != c:
                return False
        except IndexError:
            return False

        yw += dy
        xw += dx
    return True


def part1(lines):
    searches = []
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == word_to_search[0]:
                for dy, dx in directions:
                    searches.append(search_pos(lines, y, x, dy, dx))
    return len(list(filter(bool, searches)))


def part2(lines):
    pass


if __name__ == "__main__":
    with open("./inputs/day4.txt", encoding="utf-8") as f:
        lines = [l.strip() for l in f.readlines()]
    print("part 1")
    print(part1(lines))
    print("part 2")
    print(part2(lines))
