# Truth tables (4 points)
# Coban, Omer Furkan
# WiSe 24/25
# CS4Science - Team B2

# Define the logical operators as functions
def nand(a, b):
    return not (a and b)


def nor(a, b):
    return not (a or b)


def implies(a, b):
    return not a or b


def equivalent(a, b):
    return implies(a, b) and implies(b, a)


# Generate the truth tables for each operator
def generate_truth_table():
    operators = {
        "NAND": nand,
        "NOR": nor,
        "-->": implies,
        "<-->": equivalent
    }

    # Loop through operators
    for name, func in operators.items():
        print(f"Operator {name}:")
        print(f"{'op1':<8}{'op2':<8}{'op1 ' + name + ' op2':<15}")
        for op1 in [False, True]:
            for op2 in [False, True]:
                result = func(op1, op2)
                print(f"{op1:<8}{op2:<8}{result}")
        print()  # Blank line between operators


# Print the truth tables
generate_truth_table()
