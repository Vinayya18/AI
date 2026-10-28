
from heapq import heappush, heappop

# Input initial state
print("Enter initial state (3x3 matrix, use 0 for blank):")
initial_state = []
for i in range(3):
    initial_state.extend(map(int, input().split()))
initial_state = tuple(initial_state)

# Input goal state
print("Enter goal state (3x3 matrix, use 0 for blank):")
goal_state = []
for i in range(3):
    goal_state.extend(map(int, input().split()))
goal_state = tuple(goal_state)

# Validate input
if (len(initial_state) != 9 or len(goal_state) != 9
        or set(initial_state) != set(range(9))
        or set(goal_state) != set(range(9))):
    print("Invalid input! Enter numbers 0 to 8 exactly once.")
    raise SystemExit


# Manhattan distance heuristic h(n)
def manhattan_distance(state):
    distance = 0

    for i, tile in enumerate(state):
        if tile == 0:
            continue

        row, col = divmod(i, 3)
        goal_i = goal_state.index(tile)
        goal_row, goal_col = divmod(goal_i, 3)

        distance += abs(row - goal_row) + abs(col - goal_col)

    return distance


# Generate neighboring states
def get_neighbors(state):
    blank = state.index(0)
    row, col = divmod(blank, 3)
    neighbors = []

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        r, c = row + dr, col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            new_pos = r * 3 + c
            new_state = list(state)

            new_state[blank], new_state[new_pos] = (
                new_state[new_pos], new_state[blank]
            )

            neighbors.append(tuple(new_state))

    return neighbors


# Display state in matrix form
def display(state):
    for i in range(0, 9, 3):
        print(*state[i:i + 3])


# A* search algorithm
def astar(start, goal):
    pq = []
    heappush(pq, (manhattan_distance(start), 0, start))

    parent = {start: None}
    g_cost = {start: 0}
    visited = set()

    while pq:
        f, g, current = heappop(pq)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            path = []
            node = current

            while node is not None:
                path.append(node)
                node = parent[node]

            return path[::-1]

        for neighbor in get_neighbors(current):
            new_g = g + 1

            if new_g < g_cost.get(neighbor, float("inf")):
                g_cost[neighbor] = new_g
                parent[neighbor] = current

                h = manhattan_distance(neighbor)
                new_f = new_g + h

                heappush(pq, (new_f, new_g, neighbor))

    return None


# Main program
solution = astar(initial_state, goal_state)

if solution:
    print("\nSolution found!")
    print("Total moves:", len(solution) - 1)
    print("\nCost values for all states in solution path:\n")

    for step, state in enumerate(solution):
        g = step
        h = manhattan_distance(state)
        f = g + h

        print("Step", step)
        display(state)
        print("g(n) =", g)
        print("h(n) =", h)
        print("f(n) = g(n) + h(n) =", f)
        print("-" * 30)

else:
    print("No solution exists.")

