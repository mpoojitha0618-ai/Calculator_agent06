def agent_loop():
    log = []

    for step in range(2):
        log.append(f"Step {step + 1}: Observe")
        log.append(f"Step {step + 1}: Act")

    return log


result = agent_loop()

for item in result:
    print(item)