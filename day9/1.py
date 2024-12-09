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

def compress(disk):
    i, j = 0, len(disk) - 1

    compressed_disk = disk.copy()

    while i < j:
        while compressed_disk[i] != '.':
            i += 1
        while compressed_disk[j] == '.':
            j -= 1

        if i >= j:
            break

        compressed_disk[i] = compressed_disk[j]
        compressed_disk[j] = '.'

        i += 1
        j -= 1

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
