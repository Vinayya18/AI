from sympy import symbols
from sympy.logic.boolalg import (
    And, Or, Not, Implies, Equivalent, to_cnf
)
from sympy.parsing.sympy_parser import parse_expr
import re

print("CNF Conversion")
print("Operators:")
print("&  = AND")
print("|  = OR")
print("~  = NOT")
print(">> = Implication")
print("Equivalent(P,Q) = Bidirectional implication")
user_input = input("\nEnter logical expression: ")

try:
    # Find all propositional variables
    variables = set(re.findall(r'\b[A-Z]\b', user_input))

    # Create SymPy symbols
    local_dict = {
        var: symbols(var)
        for var in variables
    }

    # Add logical operators
    local_dict.update({
        "And": And,
        "Or": Or,
        "Not": Not,
        "Implies": Implies,
        "Equivalent": Equivalent
    })

    # Parse expression
    expression = parse_expr(
        user_input,
        local_dict=local_dict,
        evaluate=False
    )

    print("\nOriginal Expression:")
    print(expression)

    # Convert into CNF
    cnf_expression = to_cnf(
        expression,
        simplify=True
    )

    print("\nConjunctive Normal Form (CNF):")
    print(cnf_expression)

except Exception as e:
    print("Invalid expression:", e)

