from itertools import product

# Step 1: Get propositions
n = int(input("Enter number of propositions: "))

symbols = []
for i in range(n):
    p = input("Enter proposition name: ")
    symbols.append(p)

# Step 2: Get Knowledge Base
m = int(input("\nEnter number of KB statements: "))

kb = []
for i in range(m):
    statement = input("Enter KB statement: ")
    kb.append(statement)

# Step 3: Get query
query = input("\nEnter the query: ")

print("\nKnowledge Base:")
for statement in kb:
    print(statement)

print("\nQuery:", query)

# Step 4: Generate truth table
models_found = 0
entailed = True
truth_table = []

print("\nChecking all possible combinations...")

for values in product([False, True], repeat=n):

    assignment = dict(zip(symbols, values))

    # Check Knowledge Base
    kb_true = all(
        eval(statement, {"__builtins__": {}}, assignment)
        for statement in kb
    )

    # Check query
    result = eval(query, {"__builtins__": {}}, assignment)

    truth_table.append((values, kb_true, result))

    if kb_true:
        models_found += 1

        print("\nValid KB combination:", assignment)
        print("Query result:", result)

        if not result:
            entailed = False
            print("Counterexample found!")

# Step 5: Display result
print("\nRESULT:")

if models_found == 0:
    print("Knowledge Base is inconsistent.")
    print("No valid truth assignments exist.")

elif entailed:
    print("Knowledge Base entails the query.")
    print("ENTAILMENT: TRUE")

else:
    print("Knowledge Base does not entail the query.")
    print("ENTAILMENT: FALSE")

# Step 6: Display Truth Table
print("\nTRUTH TABLE:")

for s in symbols:
    print(f"{s:^10}", end="")

print(f"{'KB':^10}{'Query':^10}")
print("-" * (10 * (n + 2)))

for values, kb_result, query_result in truth_table:
    for value in values:
        print(f"{str(value):^10}", end="")

    print(f"{str(kb_result):^10}{str(query_result):^10}")
