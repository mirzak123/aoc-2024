import re

from input import INPUT


def main():
    buffer = re.split(r"do\(\)", INPUT)
    huffer = [i.split("don't()")[0] for i in buffer]

    muls = re.findall(r"mul\(\d{1,3},\d{1,3}\)", "".join(huffer))

    total = 0
    for mul in muls:
        num1, num2 = mul[3:].strip("()").split(",")
        total += int(num1) * int(num2)

    print(total)

if __name__ == "__main__":
    main()
