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
        self.turns = []
        self.obstructions = set()
        self.loop_detected = False

    def move(self):
        """Make a single move"""
        while not self.can_move_forward():
            turn = (self.position, self.direction)
            if turn in self.turns:
                self.loop_detected = True
            self.turns.append(turn)
            self.turn_right()
        self.forward()

    def forward(self):
        will_exit_the_map = self.is_facing_the_edge()
        self.position = Guard.position_in_front(self.position, self.direction)
        if will_exit_the_map:
            self.is_within_bounds = False

    @staticmethod
    def position_in_front(position: Position, direction: Direction):
        i, j = position
        if direction == 'UP':
            position = Position([i-1, j])
        elif direction == 'RIGHT':
            position = Position([i, j+1])
        elif direction == 'DOWN':
            position = Position([i+1, j])
        else:
            position = Position([i, j-1])
        return position

    def turn_right(self):
        self.direction = Guard.right(self.direction)

    @staticmethod
    def right(direction: Direction):
        if direction == 'UP':
            return "RIGHT"
        if direction == 'RIGHT':
            return 'DOWN'
        if direction == 'DOWN':
            return 'LEFT'
        return 'UP'

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
            if self.loop_detected:
                return True
            self.visited.add(self.position)
            self.move()

def main():
    lab_map = Map(MAP)
    guard = Guard(lab_map)
    guard.traverse()
    obstructions = 0
    for i, j in guard.visited:
        if MAP[i][j] in ('#', '^'):
            continue
        map_cpy = MAP.copy()
        map_cpy[i] = map_cpy[i][:j] + '#' + map_cpy[i][j+1:]
        lab_map = Map(map_cpy)

        guard = Guard(lab_map)
        if guard.traverse():
            obstructions += 1

    print(obstructions)

if __name__ == "__main__":
    main()
