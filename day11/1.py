from typing import Literal

from input import INPUT


def find_rule(stone) -> Literal[1, 2, 3]:
    if stone == 0:
        return 1
    if len(str(stone)) % 2 == 0:
        return 2
    return 3

def split_stone(stone) -> tuple[int, int]:
    stone = str(stone)
    l = int(len(stone) / 2)
    stone1 = int(stone[:l])
    stone2 = int(stone[l:])
    return stone1, stone2


def blink(stones: list[int]):
    i = 0
    while i < len(stones):
        rule = find_rule(stones[i])
        if rule == 1:
            stones[i] = 1
        elif rule == 2:
            stone1, stone2 = split_stone(stones[i])
            stones[i] = stone1
            stones.insert(i+1, stone2)
            i += 1
        else:
            stones[i] = stones[i] * 2024

        i += 1


BLINK_NUM = 25
def main():
    stones = INPUT
    for _ in range(BLINK_NUM):
        blink(stones)
    print(len(stones))

if __name__ == "__main__":
    main()
