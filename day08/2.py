from collections import defaultdict

from input import INPUT as MAP

Position = tuple[int, int]

antinodes: set[Position] = set()
antennas = defaultdict(list)


def calculate_antinodes(pos1: Position, pos2: Position):
    d_i = pos2[0] - pos1[0]
    d_j = pos2[1] - pos1[1]

    new_antinodes: set[Position] = set()

    last_antinode = pos1
    while True:
        antinode = last_antinode[0] + d_i, last_antinode[1] + d_j
        if not is_within_bounds(antinode):
            break
        new_antinodes.add(antinode)
        last_antinode = antinode

    last_antinode = pos2
    while True:
        antinode = last_antinode[0] - d_i, last_antinode[1] - d_j
        if not is_within_bounds(antinode):
            break
        new_antinodes.add(antinode)
        last_antinode = antinode

    return(new_antinodes)


def group_antennas():
    for i, row in enumerate(MAP):
        for j, antenna in enumerate(row):
            if antenna == '.':
                continue
            antennas[antenna].append(Position((i, j)))

def is_within_bounds(position: Position):
    i, j = position
    height = len(MAP)
    width = len(MAP[0])
    return 0 <= i < height and 0 <= j < width

def main():
    group_antennas()
    for positions in antennas.values():
        for i, position1 in enumerate(positions):
            for j in range(i+1, len(positions)):
                antinodes.update(calculate_antinodes(position1, positions[j]))
    print(len(antinodes))


if __name__ == "__main__":
    main()
