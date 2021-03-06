def move_item(old_index, new_index):
    """Makes it possible to move items from one position to another"""
    item_to_move = shopping_list[old_index]
    shopping_list.insert(new_index, item_to_move)
    del shopping_list[old_index]


def clear_list():
    """Creates a CLEAR command that removes everything from the list"""
    shopping_list.clear()
    print("\nYou list is cleared.")


def remove_item(index):
    """Makes it possible to remove items from the list"""
    index_to_delete = index - 1
    item = shopping_list.pop(index_to_delete)
    print("Removed {}.".format(item))


def show_list():
    """Creates a SHOW command that shows the current list"""
    # print out the list
    print("Here's your list:")
    count = 1
    # Change the formatting of the list display
    for item in shopping_list:
        print("{}: {}".format(count, item))
        count += 1


def show_help():
    """Creates a HELP command that prints out the help messages"""
    # print out instructions on how to use the app
    print("Here's your current list:")
    start()
    print("What else should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
Enter 'SAVE' to save your list to a file.
Enter 'MOVE' to move items from one position to another.
Enter 'REMOVE' to remove an item from the list.
Enter 'CLEAR' to remove everything from the list.
""")


def add_to_list(new_item):
    """Add new items to our list"""
    shopping_list.append(new_item)
    print(
        "Added {}. List now has {} items."
        .format(new_item, len(shopping_list)))


def save_list():
    """Creates a SAVE method that saves the shopping list to a .txt file"""
    # Use the open function to open a file
    output = open("shopping_list.txt", 'w')
    # and save your shopping list to it
    count = 1
    for item in shopping_list:
        output.write('{}:{}\n'.format(count, item))
        count += 1
    output.close()


def start():
    """Starts each session by loading a previously saved list."""
    input = open('shopping_list.txt', 'r')
    # Then use a for loop on the file to read each line in the file.
    for line in input:
        line = line.rstrip('\n')
        old_item = line.split(":")[-1]
        # Add each line to your shopping_list when your file first runs.
        shopping_list.append(old_item)
    input.close()

# Make a list to hold onto our items
shopping_list = []

show_help()

while True:
    # ask for new items
    new_item = input("> ")

    # be able to quit the app
    if new_item == "DONE":
        break
    elif new_item == "HELP":
        show_help()
    elif new_item == "SHOW":
        show_list()
    elif new_item == "SAVE":
        save_list()
    elif new_item == "CLEAR":
        clear_list()
    elif new_item == "REMOVE":
        show_list()
        index = int(input(
                        """\nGive me the number of the item
                        you want to remove: """))
        remove_item(index)
    elif new_item == "MOVE":
        if len(shopping_list) == 0:
            print("\nThere are no items in your shopping list.")
            show_help()
        else:
            show_list()
            idx_old = input(
                        """\nGive me the number of the item
                        you want to move: """)
            old_index = int(idx_old) - 1
            idx_new = input(
                            "\nWhere do you want to place {}? "
                            .format(shopping_list[old_index]))
            new_index = int(idx_new)
            move_item(old_index, new_index)
            show_list()
    else:
        if new_item in shopping_list:
            print("You've already added that item.")
        else:
            add_to_list(new_item)

show_list()
