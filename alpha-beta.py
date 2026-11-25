def alpha_beta(node, depth, alpha, beta, maximizing, values):

    if depth == 0:
        print("Evaluating leaf node:", values[node])
        return values[node]

    if maximizing:
        best = float('-inf')
        print("\nMAX NODE")

        for i in range(2):
            val = alpha_beta(
                node * 2 + i, depth - 1,
                alpha, beta, False, values
            )

            best = max(best, val)
            alpha = max(alpha, best)

            print("MAX value:", best,
                  "| Alpha:", alpha, "| Beta:", beta)

            if alpha >= beta:
                print("PRUNED: Remaining nodes")
                break

        return best

    else:
        best = float('inf')
        print("\nMIN NODE")

        for i in range(2):
            val = alpha_beta(
                node * 2 + i, depth - 1,
                alpha, beta, True, values
            )

            best = min(best, val)
            beta = min(beta, best)

            print("MIN value:", best,
                  "| Alpha:", alpha, "| Beta:", beta)

            if beta <= alpha:
                print("PRUNED: Remaining nodes")
                break

        return best


# MAIN PROGRAM
print("========== ALPHA-BETA PRUNING ==========")

n = int(input("Enter number of leaf nodes: "))

if n < 1 or (n & (n - 1)) != 0:
    print("Number of leaf nodes must be a power of 2")

else:
    values = list(map(int, input(
        "Enter leaf node values separated by spaces: "
    ).split()))

    if len(values) != n:
        print("Invalid number of values")

    else:
        depth = n.bit_length() - 1

        print("\n========== EVALUATION ==========")

        result = alpha_beta(
            0, depth,
            float('-inf'),
            float('inf'),
            True, values
        )

        print("\n--------------------------------")
        print("FINAL OPTIMAL VALUE:", result)
        print("================================")

