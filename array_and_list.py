# DATA STRUCTURE- LABORATORY EXERCISE
print("PROGRAMMED BY:")
print("IREANNE N. OMEGA")
print("BSCOE 2-2\n")

def menu():
    print("[1, 12, 22, 32, 42, 52, 62, 72, 82, 92]\n")
    print("What would you like to do?: ")
    print("1. Add an Element")
    print("2. Insert an Element")
    print("3. Modify an Element")
    print("4. Delete an Element")
    print("5. Arrange in ascending order")
    print("6. Arrange in descending order")

while True:
    try:
        menu()
        choice = int(input("\nEnter your choice: "))

        if choice in (1, 2, 3, 4, 5, 6):
            if choice == 1:
                list1 = [1, 12, 22, 32, 42, 52, 62, 72, 82, 92]
                list1.append(11)
                c1 = int(input("Enter the index you want to add: "))
                print("The element has been added.")
                print("This is the new list:")
                print(list1)

            elif choice == 2:
                list1 = [1, 12, 22, 32, 42, 52, 62, 72, 82, 92]
                c2 = int(input("Enter the index you want to insert: "))
                list1.insert(98)
                print("The element has been inserted.")
                print("This is the new list:")
                print(list1)

            elif choice == 3:
                list1 = [1, 12, 22, 32, 42, 52, 62, 72, 82, 92]
                print("Original List:")
                print(list1)
                # changing the first value
                list1[1] = 2
                modify = int(input("What index you want to modify (0-9): "))
                item = int(input("Enter the element you want to modify: "))
                list1[modify] = item
                print("The element has been modified. ")
                print("This is the changed list:")
                print(list1)

            elif choice == 4:
                c4 = int(input("Enter the index you want to remove: "))
                list1 = [1, 12, 22, 32, 42, 52, 62, 72, 82, 92]
                list1.remove()
                print("The element has been deleted.")
                print("This is the new list:")
                print(list1)

            elif choice == 5:
                list1 = [1, 12, 22, 32, 42, 52, 62, 72, 82, 92]
                list1.sort()
                print("The element has been arranged in ascending order.")
                print("This is the new list: ")
                print(list1)

            elif choice == 6:
                list1 = [1, 12, 22, 32, 42, 52, 62, 72, 82, 92]
                list1.reverse()
                print("The element has been arranged in descending order.")
                print("This is the new list: ")
                print(list1)

            else:
                print("Select another valid choice:")

        ask = str(input("\nWant to try again? (yes/no): "))
        if ask == "yes":
            continue

    except:
        print("Invalid! Please try again.")

    else:
        print("Thank you!")
        break


