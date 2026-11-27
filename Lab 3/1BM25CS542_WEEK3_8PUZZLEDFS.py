def dfs(state, goal, max_depth, node_count, path):
    node_count[0] += 1

    if state == goal:
        return True, state

    if len(path) > max_depth:
        return False, None

    zero = state.index(0)
    row = zero // 3
    col = zero % 3

    moves = [
        (0, -1),   
        (-1, 0),   
        (0, 1),   
        (1, 0)   
    ]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero = new_row * 3 + new_col
            new_state = list(state)
            new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]
            new_state = tuple(new_state)

            if new_state not in path:
                path.add(new_state)
                
                found, result = dfs(new_state, goal, max_depth, node_count, path)
                if found:
                    return True, result

                path.remove(new_state)

    return False, None


def solve_dfs(start, goal):
    node_count = [0]
    path = set()
    path.add(start)

    max_depth = 25 

    found, result = dfs(start, goal, max_depth, node_count, path)

    if found:
        print("\nGoal found!")
        print("Total Nodes Explored:", node_count[0])
    else:
        print(f"\nGoal not found within a maximum depth of {max_depth}.")


print("Enter INITIAL state:")
start = []
for i in range(3):
    start.extend(map(int, input().split()))
start = tuple(start)

print("Enter GOAL state:")
goal = []
for i in range(3):
    goal.extend(map(int, input().split()))
goal = tuple(goal)

solve_dfs(start, goal)
