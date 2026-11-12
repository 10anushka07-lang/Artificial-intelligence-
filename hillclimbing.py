def hill_climbing(start, goal):
    current = start
    while current != goal:
        print("Current State:", current)
        neighbors = [current + 1, current - 1]
        best = current

        for neighbor in neighbors:
            if abs(goal - neighbor) < abs(goal - best):
                best = neighbor

        if best == current:
            print("Goal not found")
            return current

        current = best

    print("Goal Reached:", current)


start = 1
goal = 5
hill_climbing(start, goal)