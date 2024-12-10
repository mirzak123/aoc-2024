from input import INPUT as MAP

Position = tuple[int, int]

class Node:
    peaks: set[Position] = set()
    def __init__(self, position: Position):
        self.position = position
        self.height: int = int(MAP[position[0]][position[1]])

    def left(self):
        i, j = self.position
        if j > 0:
            return Node(Position((i, j-1)))
        return (-1, -1)

    def right(self):
        i, j = self.position
        if j < len(MAP)-1:
            return Node(Position((i, j+1)))
        return (-1, -1)

    def up(self):
        i, j = self.position
        if i > 0:
            return Node(Position((i-1, j)))
        return (-1, -1)

    def down(self):
        i, j = self.position
        if i < len(MAP) - 1:
            return (Position((i+1, j)))
        return (-1, -1)

    def traverse(self):
        if (self.height) == 9:
            return self.position

        nodes = [self.left(), self.right(), self.up(), self.down()]
        for node in nodes:
            if node.position == (-1, -1):
                continue
            if node.height == self.height + 1:
                node.traverse()

def main():
    for i, row in enumerate(MAP):
        for j, char in enumerate(row):
            print(char)
            if char == '0':
                node = Node(Position((i, j)))
                node.traverse()
    print(Node.peaks)

if __name__ == "__main__":
    main()
