from input import INPUT as MACHINES


def price(a_count, b_count):
    return a_count * 3 + b_count

def find_cheapest_winning_combination(a, b, prize):
    lowest_price = None
    for i in range(1, 101):
        for j in range(1, 101):
            if push_buttons(a, b, i, j) == prize:
                current_price = price(i, j)
                if (lowest_price is None or current_price < lowest_price):
                    lowest_price = current_price
    return lowest_price

def push_buttons(a, b, a_count, b_count):
    return a[0] * a_count + b[0] * b_count, a[1] * a_count + b[1] * b_count

def main():
    tokens_spent = 0
    for machine in MACHINES:
        a = machine[0]
        b = machine[1]
        prize = machine[2]
        current_price = find_cheapest_winning_combination(a, b, prize)
        tokens_spent += current_price if current_price is not None else 0
    print(tokens_spent)

if __name__ == "__main__":
    main()
