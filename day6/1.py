from typing import Literal

from input import INPUT as MAP

Position = tuple[int, int]
Direction = Literal['UP', 'DOWN', 'RIGHT', 'LEFT']

def get_starting_pos(guard_map) -> Position:
    """Returns a tupple containing the starting position"""
    for i, row in enumerate(guard_map):
        for j, _ in enumerate(row):
            if row[j] == '^':
                return i, j
    return (-1, -1)

def is_within_bounds(pos: Position, width: int, height: int) -> bool:
    """Returns True if a position is within bounds of the map"""
    i, j = pos
    return 0 <= i <= height and 0 <= j <= width

def can_move_forward(guard_map, pos: Position, direction: Direction) -> bool:
    """Returns True if there is no obstacle in front, even if the position in
    front is beyond the bounds of the map"""
    i, j = pos
    try:
        if direction == 'UP':
            return guard_map[i-1][j] != '#'
        if direction == 'RIGHT':
            return guard_map[i][j+1] != '#'
        if direction == 'DOWN':
            return guard_map[i+1][j] != '#'
        return guard_map[i][j-1] != '#'
    except IndexError:
        return True

def traverse(guard_map, start: Position, direction: Direction) -> set:
    """Traverse the map"""
    width = len(guard_map)
    height = len(guard_map[0])
    visited = set()
    current: Position = start
    while is_within_bounds(current, width, height):
        current, direction = move(guard_map, current, direction)
        visited.add(current)
    return visited

def turn_right(direction: Direction)-> Direction:
    if direction == 'UP':
        return 'RIGHT'
    if direction == 'RIGHT':
        return 'DOWN'
    if direction == 'DOWN':
        return 'LEFT'
    return 'UP'

def forward(pos: Position, direction: Direction) -> Position:
    i, j = pos
    if direction == 'UP':
        return i-1, j
    if direction == 'RIGHT':
        return i, j+1
    if direction == 'DOWN':
        return i+1, j
    return i, j-1

def move(guard_map, pos: Position, direction: Direction) -> tuple[Position, Direction]:
    """Make a single move"""
    if not can_move_forward(guard_map, pos, direction):
        direction = turn_right(direction)
    pos = forward(pos, direction)
    return pos, direction

def main():
    visited_positions = set()
    start = get_starting_pos(MAP)
    direction = 'UP'
    visited_positions = traverse(MAP, start, direction)
    print(len(visited_positions))

if __name__ == "__main__":
    main()
