class ModelBasedVacuumAgent:

    def __init__(self):
        # Internal model of the environment
        self.model = {
            "A": "Unknown",
            "B": "Unknown"
        }

    def act(self, location, actual_state):
        # Update internal model using perception
        self.model[location] = actual_state

        # If current room is dirty, clean it
        if actual_state == "Dirty":
            print(f"At {location}: Dirty -> CLEAN")
            self.model[location] = "Clean"
            return "Clean"

        # If current room is clean, check other room
        other_room = "B" if location == "A" else "A"

        if self.model[other_room] != "Clean":
            print(f"At {location}: Clean -> Move to {other_room}")
            return f"Move to {other_room}"

        print("All rooms are clean.")
        return "Stop"


# Create agent
agent = ModelBasedVacuumAgent()

# Environment
environment = {
    "A": "Dirty",
    "B": "Dirty"
}

# Run the agent
location = "A"

for i in range(10):

    action = agent.act(location, environment[location])

    if action == "Clean":
        environment[location] = "Clean"

    elif action.startswith("Move"):
        location = "B" if location == "A" else "A"

    elif action == "Stop":
        break

print("\nFinal Environment:", environment)
print("Agent's Internal Model:", agent.model)
