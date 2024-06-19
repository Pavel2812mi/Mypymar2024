"""Из молекулы в атомы"""


def parse_molecule(formula):
    """
    Breaks down a chemical formula string
    into its constituent atoms and their numbers

    Args:
        formula: A string representing the chemical formula
         of the molecule.

    Returns:
        A dictionary where the keys are symbols of atoms (strings),
        and the values are their number (integers) in the molecule.
    """
    stack = []
    current = {}
    i = 0

    while i < len(formula):
        if formula[i].isupper():
            atom = formula[i]
            i += 1
            while i < len(formula) and formula[i].islower():
                atom += formula[i]
                i += 1
            count = ""
            while i < len(formula) and formula[i].isdigit():
                count += formula[i]
                i += 1
            count = int(count) if count else 1
            current[atom] = current.get(atom, 0) + count
        elif formula[i] == "(" or formula[i] == "[" or formula[i] == "{":
            stack.append(current)
            current = {}
            i += 1
        elif formula[i] == ")" or formula[i] == "]" or formula[i] == "}":
            multiplier = ""
            i += 1
            while i < len(formula) and formula[i].isdigit():
                multiplier += formula[i]
                i += 1
            multiplier = int(multiplier) if multiplier else 1
            temp = current
            current = stack.pop()
            for key, value in temp.items():
                current[key] = current.get(key, 0) + value * multiplier
        else:
            i += 1

    return current


assert parse_molecule("H2O") == {"H": 2, "O": 1}, "Programm error"
assert parse_molecule("Mg(OH)2") == {"Mg": 1, "O": 2, "H": 2}, "Programm error"
assert (parse_molecule("K4[ON(SO3)2]2")
        == {"K": 4, "O": 14, "N": 2, "S": 4}), "Programm error"
