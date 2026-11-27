
import math
import random

def objective(x):
    return x * x

def simulated_annealing():

    current = random.uniform(-10, 10)

    initial_temp = float(input("Enter Initial Temperature: "))
    cooling_rate = float(input("Enter Cooling Rate (0 to 1): "))
    min_temp = float(input("Enter Minimum Temperature: "))

    if initial_temp <= 0 or not (0 < cooling_rate < 1) or min_temp <= 0 or min_temp >= initial_temp:
        print("Invalid Input!")
        return

    temp = initial_temp

    while temp > min_temp:

        new = current + random.uniform(-1, 1)

        current_cost = objective(current)
        new_cost = objective(new)

        if new_cost < current_cost:
            current = new
        else:
            probability = math.exp(
                (current_cost - new_cost) / temp
            )

            if random.random() < probability:
                current = new

        temp = temp * cooling_rate

    print("\nBest Solution:", current)
    print("Minimum Value:", objective(current))

simulated_annealing()