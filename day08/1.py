from collections import defaultdict

from input import INPUT as MAP

Position = tuple[int, int]

antinodes: set[Position] = set()
antennas = defaultdict(list)

def calculate_antinodes(pos1: Position, pos2: Position):
    d_i = abs(pos1[0] - pos2[0])
    d_j = abs(pos1[1] - pos2[1])

    antinode1_i = None
    antinode1_j = None
    antinode2_i = None
    antinode2_j = None

    if pos1[0] < pos2[0]:
        antinode1_i = pos1[0] - d_i
        antinode2_i = pos2[0] + d_i
    else:
        antinode1_i = pos1[0] + d_i
        antinode2_i = pos2[0] - d_i

    if pos1[1] < pos2[1]:
        antinode1_j = pos1[1] - d_j
        antinode2_j = pos2[1] + d_j
    else:
        antinode1_j = pos1[1] + d_j
        antinode2_j = pos2[1] - d_j

    return((antinode1_i, antinode1_j), (antinode2_i, antinode2_j))

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
                antinode1, antinode2 = calculate_antinodes(position1, positions[j])
                if is_within_bounds(antinode1):
                    antinodes.add(antinode1)
                if is_within_bounds(antinode2):
                    antinodes.add(antinode2)
    print(len(antinodes))

if __name__ == "__main__":
    main()
