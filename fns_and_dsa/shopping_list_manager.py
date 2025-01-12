def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            item_to_be_added = input("Enter the item to add: ")
            shopping_list.append(item_to_be_added)
        elif choice == "2":
            item_to_be_removed = input("please provide the item you want to remove: ")
            if item_to_be_removed in shopping_list:
                shopping_list.remove[item_to_be_removed]
            else:
                print(
                    "the item you provided is not in the shopping list please check it once more. "
                )
        elif choice == "3":
            if len(shopping_list) > 0:
                for item in shopping_list:
                    print(item)
            else:
                print("shopping list is empty")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
