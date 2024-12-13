from input import INPUT as MACHINES
from sympy import Matrix


def price(a_count, b_count):
    return a_count * 3 + b_count

def find_winning_combination(a, b, prize):
    # solve a system of 2 equations with 2 unknowns using sympy which doesn't
    # have fraction issues that occur with numpy.linalg.solve
    offset = 10000000000000
    left_side = Matrix([[a[0], b[0]], [a[1], b[1]]])
    right_side = Matrix([prize[0]+offset, prize[1]+offset])
    solution = left_side.LUsolve(right_side)

    a_count, b_count = solution
    if solution[0].is_Integer:
        return int(a_count), int(b_count)
    return None

def push_buttons(a, b, a_count, b_count):
    return a[0] * a_count + b[0] * b_count, a[1] * a_count + b[1] * b_count

def main():
    tokens_spent = 0
    for machine in MACHINES:
        a = machine[0]
        b = machine[1]
        prize = machine[2]
        solution = find_winning_combination(a, b, prize)
        tokens_spent += price(solution[0], solution[1]) if solution is not None else 0
    print(tokens_spent)

if __name__ == "__main__":
    main()
