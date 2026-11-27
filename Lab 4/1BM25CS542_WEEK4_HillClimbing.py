import random

# Take number of queens
N = int(input("Enter number of queens (N): "))


# Calculate conflicts between queens
def calculate_conflicts(state):
    conflicts = []

    for i in range(N):
        for j in range(i + 1, N):
            if state[i] == state[j]:
                conflicts.append((i + 1, state[i] + 1,
                                  j + 1, state[j] + 1,
                                  "Same row"))

            elif abs(state[i] - state[j]) == abs(i - j):
                conflicts.append((i + 1, state[i] + 1,
                                  j + 1, state[j] + 1,
                                  "Diagonal"))

    return conflicts


# Cost = total number of attacking pairs
def calculate_cost(state):
    return len(calculate_conflicts(state))


# Generate neighboring states
def get_neighbors(state):
    neighbors = []

    for col in range(N):
        for row in range(N):
            if row != state[col]:
                neighbor = list(state)
                neighbor[col] = row
                neighbors.append(tuple(neighbor))

    return neighbors


# Display chessboard and queen positions
def display_board(state):
    print("\nChessboard:")

    for row in range(N):
        for col in range(N):
            if state[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

    print("\nQueen positions (x, y):")
    for col in range(N):
        print(f"Queen {col + 1}: ({col + 1}, {state[col] + 1})")


# Display conflicting queen pairs
def display_conflicts(state):
    conflicts = calculate_conflicts(state)

    print("\nConflicts:")

    if not conflicts:
        print("No conflicts. All queens are safe!")
    else:
        for q1x, q1y, q2x, q2y, reason in conflicts:
            print(
                f"Queen at ({q1x}, {q1y}) and "
                f"Queen at ({q2x}, {q2y}) -> {reason}"
            )

    print("Total conflicts:", len(conflicts))


# Hill Climbing with random restarts
def hill_climbing():
    restart = 0

    while True:
        restart += 1
        current = tuple(random.randrange(N) for _ in range(N))

        print("\nRestart", restart)

        while True:
            current_cost = calculate_cost(current)

            print("\nCurrent state:", current)
            print("Current cost:", current_cost)

            if current_cost == 0:
                print("\nGoal state reached!")
                display_board(current)
                display_conflicts(current)
                return current

            neighbors = get_neighbors(current)
            best_cost = min(calculate_cost(n) for n in neighbors)

            if best_cost >= current_cost:
                print("Local minimum reached. Restarting...")
                break

            best_neighbors = [
                n for n in neighbors
                if calculate_cost(n) == best_cost
            ]

            current = random.choice(best_neighbors)


# Main program
if N < 1:
    print("N must be at least 1.")
else:
    solution = hill_climbing()

    print("\nFinal solution:", solution)
    print("Number of attacking pairs:", calculate_cost(solution))
