rule = "All humans are mortal"
def backward_chaining(goal, person, fact):
    print("Rule:", rule)
    print("Initial Goal:", goal, person)
    print("Subgoal: Is", person, "human?")
    if fact == "yes":
        return True
    return False
person = input("Enter person name: ").lower()
fact = input("Is " + person + " human? ").lower()

if backward_chaining("mortal", person, fact):
    print(person, "is mortal")
else:
    print("Goal Not Proved")