rule = "All humans are mortal"
def forward_chaining(person, fact):
    print("Rule:", rule)
    print("Given Fact:", fact)
    if fact == "yes":
        print("Conclusion:", person, "is mortal")
    else:
        print("Conclusion cannot be proved")
person = input("Enter person name: ")
fact = input("Is " + person + " human? (yes/no): ").lower()
forward_chaining(person, fact)