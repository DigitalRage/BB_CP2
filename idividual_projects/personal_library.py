# BB 1st Personal Library Project

# A list to store all book items
library = []

# A set used to validate menu choices
valid = {"1", "2", "3", "4", "5"}


# display all books in the library
def view_library():
    print("\n--- YOUR LIBRARY ---")
    
    # If the library is empty, tell the user
    if len(library) == 0:
        print("Your library is currently empty.\n")
        return
    
    # Loop through the list and print each book
    for book in library:
        print(f"{book['title']} by {book['author']}")
    print()


# add a new book to the library
def add_book():
    print("\n--- ADD A NEW BOOK ---")
    
    # Ask user for book details
    title = input("Title: ").strip()
    author = input("By: ").strip()
    
    # Create a dictionary to store the book
    new_book = {"title": title, "author": author}
    
    # Add the book to the library list
    library.append(new_book)
    
    print(f"\nYou have added\n{title} by {author}\n")


# remove a book from the library
def remove_book():
    print("\n--- REMOVE A BOOK ---")
    
    # If library is empty, nothing to remove
    if len(library) == 0:
        print("Your library is empty. Nothing to remove.\n")
        return
    
    # Display numbered list of books
    for index, book in enumerate(library, start=1):
        print(f"{index}. {book['title']} by {book['author']}")
    
    # Ask user which book to remove
    try:
        choice = int(input("\nEnter the number of the item you would like to remove: "))
        
        # Validate the number
        if 1 <= choice <= len(library):
            removed_book = library.pop(choice - 1)
            print(f"\nYou have removed {removed_book['title']} by {removed_book['author']}\n")
        else:
            print("\nInvalid number. No book removed.\n")
    
    except ValueError:
        print("\nInvalid input. Please enter a number.\n")


# search for books by title or author
def search_library():
    print("\n--- SEARCH LIBRARY ---")
    print("What would you like to search by")
    print("1. Title")
    print("2. Author")
    
    search_choice = input("Enter choice: ").strip()
    
    # Search by title
    if search_choice == "1":
        keyword = input("Enter the title keyword: ").strip().lower()
        print()
        
        # Loop through library and print matches
        for book in library:
            if keyword in book["title"].lower():
                print(f"{book['title']} by {book['author']}")
        print()
    
    # Search by author
    elif search_choice == "2":
        keyword = input("Enter the author's name: ").strip().lower()
        print()
        
        for book in library:
            if keyword in book["author"].lower():
                print(f"{book['title']} by {book['author']}")
        print()
    
    else:
        print("\nInvalid search option.\n")


# MAIN PROGRAM LOOP
# Displays menu and calls functions
def run_library_program():
    print("Welcome to your Personal Library Catalog!")
    print("You can view, add, remove, and search your books.\n")
    
    while True:
        print("MAIN MENU:")
        print("1. View")
        print("2. Add")
        print("3. Remove")
        print("4. Search")
        print("5. Exit")
        
        choice = input("\nType the number for the action you would like to perform: ").strip()
        
        # Validate menu choice using the set
        if choice not in valid:
            print("\nInvalid choice. Please try again.\n")
            continue
        
        # Call the correct function
        if choice == "1":
            view_library()
        elif choice == "2":
            add_book()
        elif choice == "3":
            remove_book()
        elif choice == "4":
            search_library()
        elif choice == "5":
            print("\nGoodbye! Thanks for using the library catalog.\n")
            break


# Start the program
run_library_program()