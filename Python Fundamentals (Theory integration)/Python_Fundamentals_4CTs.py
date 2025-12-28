print("Name: Python_Fundamentals_4CTs")
print("Description: Enter a choice and it shows the definition of the computational thinking techniques")
print("")

print("4 Computational Thinking Techniques")
print("")

#choice selector guide
print("Choice 1 - 'Decomposition'")
print("Choice 2 - 'Pattern Recognition'")
print("Choice 3 - 'Abstraction'")
print("Choice 4 - 'Algorithms'")

#input type: str (default) - to select one from below
choice = input ("Select a Choice: ")


#Decomposition if condition
if choice == "Decomposition":
    print("Breaking Down Complex Problem into Small Manageable Parts.")

    #Pattern Recognition - elif Condition
elif choice == "Pattern Recognition":
    print("Similarities Among and Within Problems.")

#Abstraction - elif condition
elif choice == "Abstraction":
    print("Focusing on Important info only, ignoring irrelevant detail.")

#Algorihms - elif condition
elif choice == "Algorithms":
    print("Developing a step by step solution / rules to solve problem.")

#Not in choices - else always executes
else:
    print("Not in the choice selected, please rerun the program.")
