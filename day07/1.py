from itertools import product

from input import INPUT

OPERATORS = {'+', '*'}

def operator_combinations(num_of_operators):
    return product(OPERATORS, repeat=num_of_operators)

def result(equation):
    total = 0
    operator = None
    for x in equation:
        if x in OPERATORS:
            operator = x
        elif not operator:
            total = x
        elif operator == '+':
            total += x
        elif operator == '*':
            total *= x
    return total
            

def construct_equation(operands, operators):
    equation = []
    for i, operator in enumerate(operators):
        equation.append(operands[i])
        equation.append(operator)
    equation.append(operands[-1])

    return equation

def is_valid(test_value, operands):
    for operators in operator_combinations(len(operands) - 1):
        equation = construct_equation(operands, operators)
        if result(equation) == test_value:
            return True
    return False

def main():
    total = 0
    for test_value, *operands in INPUT:
        if is_valid(test_value, operands):
            total += test_value
    print(total)

if __name__ == "__main__":
    main()
