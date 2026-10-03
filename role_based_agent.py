def role_based_agent(temperature):

    if temperature > 100:
        return "cool"
    else:
        return "idle"


temperatures = [80, 100, 101, 120]

for temp in temperatures:

    action = role_based_agent(temp)

    print(f"Temperature: {temp}")
    print(f"Agent action: {action}")
    print("-" * 30)