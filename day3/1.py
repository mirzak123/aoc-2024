import re

from input import INPUT


def main():
    muls = re.findall(r"mul\(\d{1,3},\d{1,3}\)", INPUT)

    total = 0
    for mul in muls:
        num1, num2 = mul[3:].strip("()").split(",")
        total += int(num1) * int(num2)

    print(total)

if __name__ == "__main__":
    main()
