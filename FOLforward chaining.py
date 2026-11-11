
# First Order Logic using Forward Chain

# Take initial facts from user
facts = set()

n = int(input("Enter number of initial facts: "))

print("\nEnter facts in the given format:")
print("Example: American Robert")
print("         Enemy A America")
print("         Missile T1")
print("         Owns A T1")

for i in range(n):
    fact = tuple(input(f"Enter fact {i+1}: ").split())
    facts.add(fact)


# Forward Chaining Algorithm
def forward_chaining(facts):

    new_facts = True

    while new_facts:
        new_facts = False

        for fact in list(facts):

            # Rule 1: Enemy of America is Hostile
            if fact[0] == "Enemy" and len(fact) == 3:
                if fact[2] == "America":
                    new_fact = ("Hostile", fact[1])

                    if new_fact not in facts:
                        facts.add(new_fact)
                        print("Inferred:", new_fact)
                        new_facts = True

            # Rule 2: Missiles are Weapons
            if fact[0] == "Missile" and len(fact) == 2:
                new_fact = ("Weapon", fact[1])

                if new_fact not in facts:
                    facts.add(new_fact)
                    print("Inferred:", new_fact)
                    new_facts = True

        # Rule 3: Missiles owned by A are sold by Robert to A
        for missile in list(facts):
            if missile[0] == "Missile" and len(missile) == 2:

                item = missile[1]

                if ("Owns", "A", item) in facts:
                    new_fact = ("Sells", "Robert", item, "A")

                    if new_fact not in facts:
                        facts.add(new_fact)
                        print("Inferred:", new_fact)
                        new_facts = True

        # Rule 4: American selling weapons to hostile nations
        # is a criminal
        for person in list(facts):
            if person[0] == "American" and len(person) == 2:

                name = person[1]

                for sale in list(facts):
                    if sale[0] == "Sells" and len(sale) == 4:

                        if sale[1] == name:
                            item = sale[2]
                            country = sale[3]

                            if (("Weapon", item) in facts and
                                ("Hostile", country) in facts):

                                new_fact = ("Criminal", name)

                                if new_fact not in facts:
                                    facts.add(new_fact)
                                    print("Inferred:", new_fact)
                                    new_facts = True

    return facts


# Display initial facts
print("\nInitial Knowledge Base:")
for fact in sorted(facts):
    print(fact)


# Apply Forward Chaining
print("\nApplying Forward Chaining...")
facts = forward_chaining(facts)


# Take query from user
print("\nEnter query in the format: Criminal Robert")
query = tuple(input("Enter query: ").split())


# Check query
print("\nResult:")

if query in facts:
    print("Query Proved Successfully!")
else:
    print("Query Cannot Be Proved!")
