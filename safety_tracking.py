def safety_tracking_agent():

    state = {
        "done": False,
        "stage": 0,
        "status": None
    }

    max_iters = 10

    for i in range(max_iters):

        state["stage"] += 1

        print(f"Iteration {state['stage']}")

        # Observe
        print("Observe")

        # Decide
        print("Decide")

        # Act
        print("Act")

        # Example success condition
        if state["stage"] == 3:
            state["done"] = True
            state["status"] = "success"
            return state

    # If maximum iterations are exceeded
    state["done"] = True
    state["status"] = "failure"

    return state


result = safety_tracking_agent()

print("Final State:")
print(result)