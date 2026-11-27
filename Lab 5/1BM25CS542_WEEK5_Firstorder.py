def unify(x, y, substitution=None):

    if substitution is None:
        substitution = {}

    if x == y:
        return substitution

    if isinstance(x, str) and x.islower():
        substitution[x] = y
        return substitution

    if isinstance(y, str) and y.islower():
        substitution[y] = x
        return substitution

    if isinstance(x, tuple) and isinstance(y, tuple):

        if x[0] != y[0] or len(x) != len(y):
            return None

        for a, b in zip(x[1:], y[1:]):
            substitution = unify(a, b, substitution)

            if substitution is None:
                return None

        return substitution

    return None


# Get input from user
print("Enter first predicate:")
p1 = input("Predicate name: ")
a1 = input("Argument 1: ")
b1 = input("Argument 2: ")

print("\nEnter second predicate:")
p2 = input("Predicate name: ")
a2 = input("Argument 1: ")
b2 = input("Argument 2: ")

# Create predicates
expr1 = (p1, a1, b1)
expr2 = (p2, a2, b2)

# Perform unification
result = unify(expr1, expr2)

# Display result
print("\nFirst Expression:", expr1)
print("Second Expression:", expr2)

if result is not None:
    print("\nUnification Successful!")
    print("Substitution:", result)
else:
    print("\nUnification Failed!")eats