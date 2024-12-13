from input import INPUT as FARM

Position = tuple[int, int]

class Node:
    visited: set[Position] = set()

    def __init__(self, position: Position):
        self.position = position
        self.type = FARM[position[0]][position[1]]

    def __repr__(self):
        return f"{self.type}:({self.position[0]} {self.position[1]})"

    def left(self):
        i, j = self.position
        if j > 0:
            return Node(Position((i, j-1)))
        return None

    def right(self):
        i, j = self.position
        if j < len(FARM[0]) - 1:
            return Node(Position((i, j+1)))
        return None

    def up(self):
        i, j = self.position
        if i > 0:
            return Node(Position((i-1, j)))
        return None

    def down(self):
        i, j = self.position
        if i < len(FARM) - 1:
            return Node(Position((i+1, j)))
        return None

    def visit(self):
        if self.position in Node.visited:
            return 0, 0
        Node.visited.add(self.position)
        plants = [self.left(), self.right(), self.up(), self.down()]
        same_region_plants = [plant for plant in plants if plant is not None and plant.type == self.type]
        plant_count = 1
        fences = 4 - len(same_region_plants)
        for plant in same_region_plants:
            a, b = plant.visit()
            plant_count += a
            fences += b
        return plant_count, fences


def main():
    price = 0
    for i, row in enumerate(FARM):
        for j, _ in enumerate(row):
            plant = Node(Position((i, j)))
            plant_count, fences = plant.visit()
            price += plant_count * fences
    print(price)


if __name__ == "__main__":
    main()
