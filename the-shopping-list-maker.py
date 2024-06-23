# question 2 task 1

shopping_list = []

choice1 = input("Would you like to add items to your shopping list?")

while choice1 == "yes":
    item = input("What would you like to add? (Type quit to exit)")
    if item != "quit":
        shopping_list.append(item)
    else:
        break


print(f"Current shopping list: {shopping_list}")

# question 2 task 2

shopping_list = []

choice = input("Would you like to add or remove items on your shopping list? (Type 'quit' to exit)")

while choice != "quit":
    if choice == "add":
        item = input("What would you like to add?")
        if item != "quit":
            shopping_list.append(item)
        else:
            break
    elif choice == "remove":
        item = input("What would you like to remove?")
        if item != "quit":
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print(f"{item} not in shopping list.")
        else:
            break
    else:
        break

print(f"Current shopping list: {shopping_list}")


# question 2 task 3
shopping_list = []

choice = input ("Would you like to add or remove items from your shopping list? (Type 'quit' to exit)")

while choice != quit:
    if choice == "add":
        item = input("What would you like to add?")
        if item != "quit":
            shopping_list.append(item)
        else:
            break
    elif choice == "remove":
        item = input("What would you like to remove?")
        if item != "quit":
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print(f"{item} is not in shopping list.")
        else:
            break
    else:
        break
    print(shopping_list)
    choice = input("Would you like to add more items from your shopping list? (Type 'quit' to exit)")

print("Current shopping list: ")
for item in shopping_list:
    print(item)
    print()
