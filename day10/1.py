from input import INPUT as MAP

Position = tuple[int, int]

class Node:
    def __init__(self, position: Position):
        self.position = position
        self.height: int = int(MAP[position[0]][position[1]])

    def __repr__(self):
        return f"{self.height}:({self.position[0]} {self.position[1]})"

    def left(self):
        i, j = self.position
        if j > 0:
            return Node(Position((i, j-1)))
        return None

    def right(self):
        i, j = self.position
        if j < len(MAP) - 1:
            return Node(Position((i, j+1)))
        return None

    def up(self):
        i, j = self.position
        if i > 0:
            return Node(Position((i-1, j)))
        return None

    def down(self):
        i, j = self.position
        if i < len(MAP) - 1:
            return Node(Position((i+1, j)))
        return None

    def traverse(self):
        peaks: set[Position] = set()
        if (self.height) == 9:
            peaks.add(self.position)
            return peaks

        nodes = [self.left(), self.right(), self.up(), self.down()]
        valid_nodes: list[Node] = [node for node in nodes if node is not None and node.height == self.height + 1]

        for node in valid_nodes:
            peaks.update(node.traverse())
        return peaks

def main():
    total = 0
    for i, row in enumerate(MAP):
        for j, char in enumerate(row):
            if char == '0':
                node = Node(Position((i, j)))
                total += len(node.traverse())
    print(total)

if __name__ == "__main__":
    main()
