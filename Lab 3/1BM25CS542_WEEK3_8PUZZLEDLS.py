def dls(state, goal, limit, node_count, path):

    node_count[0] += 1

    if state == goal:
        return True, state

    if limit == 0:
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

            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            new_state = tuple(new_state)

            if new_state not in path:

                path.add(new_state)

                found, result = dls(
                    new_state,
                    goal,
                    limit - 1,
                    node_count,
                    path
                )

                if found:
                    return True, result

                path.remove(new_state)

    return False, None


def ids(start, goal):

    limit = 1

    while True:

        node_count = [0]

        path = set()
        path.add(start)

        found, result = dls(start,goal,limit,node_count,path)

        if found:

            print("Limit", limit, "found")
            print()
            print("Goal found at Depth:", limit)
            print("Goal found at Node:", node_count[0])

            return

        else:

            print("Limit", limit, "not found")

        limit += 1



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


ids(start, goal)
