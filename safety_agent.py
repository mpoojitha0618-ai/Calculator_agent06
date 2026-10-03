def observe():
    return "SAFE"


def decide(observation):

    if observation == "SAFE":
        return "success"

    elif observation == "WARNING":
        return "alert"

    elif observation == "DANGER":
        return "emergency"

    return "unknown"


def act(decision):

    if decision == "alert":
        print("Safety warning!")

    elif decision == "emergency":
        print("Emergency action required!")

    else:
        print("No action required.")


def agent_loop():

    max_iters = 10

    for i in range(max_iters):

        observation = observe()

        decision = decide(observation)

        if decision == "success":
            return "success"

        act(decision)

    return "failure"


result = agent_loop()
print("Agent result:", result)