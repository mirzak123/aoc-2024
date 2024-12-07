from typing import Literal

from input import INPUT as MAP

Position = tuple[int, int]
Direction = Literal['UP', 'DOWN', 'RIGHT', 'LEFT']

class Map:
    def __init__(self, lab_map) -> None:
        self.map: list[str] = lab_map
        self.start: Position = self.get_starting_pos()
        self.height: int = len(self.map)
        self.width: int = len(self.map[0])

    def get_starting_pos(self) -> Position:
        """Returns a tupple containing the starting position"""
        for i, row in enumerate(self.map):
            for j, _ in enumerate(row):
                if row[j] == '^':
                    return i, j
        return (-1, -1)

    def is_obstacle(self, position: Position):
        i, j = position
        return self.map[i][j] == '#'

class Guard:
    def __init__(self, lab_map: Map):
        self.map = lab_map
        self.position: Position = lab_map.get_starting_pos()
        self.direction: Direction = "UP"
        self.is_within_bounds = True
        self.visited = set()

    def move(self):
        """Make a single move"""
        if not self.can_move_forward():
            self.turn_right()
        will_exit_the_map = self.is_facing_the_edge()
        self.forward()
        if will_exit_the_map:
            self.is_within_bounds = False

    def forward(self):
        i, j = self.position
        if self.direction == 'UP':
            self.position = Position([i-1, j])
        elif self.direction == 'RIGHT':
            self.position = Position([i, j+1])
        elif self.direction == 'DOWN':
            self.position = Position([i+1, j])
        else:
            self.position = Position([i, j-1])

    def turn_right(self):
        if self.direction == 'UP':
            self.direction = 'RIGHT'
        elif self.direction == 'RIGHT':
            self.direction = 'DOWN'
        elif self.direction == 'DOWN':
            self.direction = 'LEFT'
        else:
            self.direction = 'UP'

    def is_facing_the_edge(self) -> bool:
        i, j = self.position
        if self.direction == 'UP':
            return i == 0
        if self.direction == 'LEFT':
            return j == 0
        if self.direction == 'DOWN':
            return i == self.map.height - 1
        return j == self.map.width - 1

    def can_move_forward(self) -> bool:
        """Returns True if there is no obstacle in front, or if making a move
        would take you off the map"""

        # We want to allow the guard to get out of the map
        if self.is_facing_the_edge():
            return True

        i, j = self.position
        if self.direction == 'UP':
            return not self.map.is_obstacle(Position([i-1, j]))
        if self.direction == 'RIGHT':
            return not self.map.is_obstacle(Position([i, j+1]))
        if self.direction == 'DOWN':
            return not self.map.is_obstacle(Position([i+1, j]))
        return not self.map.is_obstacle(Position([i, j-1]))

    def traverse(self):
        """Traverse the map"""
        while self.is_within_bounds:
            self.visited.add(self.position)
            self.move()

def main():
    lab_map = Map(MAP)
    guard = Guard(lab_map)
    guard.traverse()
    print(len(guard.visited))

if __name__ == "__main__":
    main()
