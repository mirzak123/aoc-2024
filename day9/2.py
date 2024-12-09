from input import INPUT


def expand(disk):
    file_id = 0
    expanded = []
    for i, x in enumerate(disk):
        x = int(x)
        if i % 2 == 0:
            expanded.extend([file_id] * x)
            file_id += 1
        else:
            expanded.extend(['.'] * x)
    return expanded

def find_n_free_slots(disk, n, limit):
    for i in range(len(disk)):
        if i > limit:
            break
        if tuple(disk[i:i+n]) == ('.',) * n:
            return (i, i+n-1)
    return -1, -1


def fill_free_slots(disk, start, end, value):
    while start <= end:
        disk[start] = value
        start += 1

def free_occupied_slots(disk, start, end):
    while start <= end:
        disk[start] = '.'
        start += 1

def compress(disk):
    compressed_disk = disk.copy()
    j = len(disk) - 1

    while j > 0:
        while compressed_disk[j] == '.':
            j -= 1
        end_of_file = j

        file_id = compressed_disk[end_of_file]
        while compressed_disk[j-1] == file_id:
            j -= 1
        start_of_file = j

        j -= 1

        n = end_of_file - start_of_file + 1
        free_slots = find_n_free_slots(compressed_disk, n, j)
        if free_slots == (-1, -1):
            continue

        start_of_free, end_of_free = free_slots

        if end_of_free >= start_of_file:
            continue

        fill_free_slots(compressed_disk, start_of_free, end_of_free, file_id)
        free_occupied_slots(compressed_disk, start_of_file, end_of_file)

    return compressed_disk

def checksum(disk):
    total = 0
    for i, x in enumerate(disk):
        if x == '.':
            continue
        total += i * int(x)
    return total

def main():
    expanded = expand(INPUT)
    compressed = compress(expanded)
    print(checksum(compressed))


if __name__ == "__main__":
    main()
