# BB 1st Update Personal Library Project
# Import libraries
import csv
import os

# Read library csv file
# import list from csv file
def load_library(file_path):
    library = []

    if not os.path.exists(file_path):
        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=[
                    "Title",
                    "Director",
                    "Genre",
                    "Rating",
                    "Length (min)",
                    "Notable Actors"
                ]
            )
            writer.writeheader()
        return library

    with open(file_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                if not row["Title"] or not row["Director"] or not row["Genre"]:
                    raise ValueError("Missing required field")

                try:
                    row["Length (min)"] = int(row["Length (min)"])
                except ValueError:
                    pass

                library.append(row)
            except Exception as e:
                print(f"Skipping bad row: {row} ({e})")

    return library


# add an option that allows the user to save the library back to the csv file
def save_library(file_path, library):
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "Title",
                "Director",
                "Genre",
                "Rating",
                "Length (min)",
                "Notable Actors"
            ]
        )
        writer.writeheader()
        for item in library:
            writer.writerow(item)
    print("Library saved.")


# make a function that properly formats and displays the list of books
def show_simple_list(library):
    print("\nSimple List:")
    for i, item in enumerate(library):
        print(f"{i}: {item['Title']} — {item['Director']}")
    print()


# make a function that neatly displays all details of the books
def show_detailed_list(library):
    print("\nDetailed List:")
    for i, item in enumerate(library):
        print(f"\nItem {i}:")
        for key, value in item.items():
            print(f"  {key}: {value}")
    print()


# make a function that allows the user to add a book to the library
def add_item(library):
    print("\nAdd New Item")
    title = input("Title: ").strip()
    director = input("Director: ").strip()
    genre = input("Genre: ").strip()
    rating = input("Rating: ").strip()
    length = input("Length (min): ").strip()
    actors = input("Notable Actors: ").strip()

    try:
        length = int(length)
    except ValueError:
        print("Length must be a number. Keeping as text.")

    item = {
        "Title": title,
        "Director": director,
        "Genre": genre,
        "Rating": rating,
        "Length (min)": length,
        "Notable Actors": actors
    }

    library.append(item)
    print("Item added.")


# make a function that allows the user to update the details of a book in the library
def update_item(library):
    show_simple_list(library)
    try:
        index = int(input("Enter index to update: "))
        if index < 0 or index >= len(library):
            print("Invalid index.")
            return
    except ValueError:
        print("Invalid number.")
        return

    item = library[index]
    print("Press Enter to keep current value.")

    for key in item:
        new_value = input(f"{key} [{item[key]}]: ").strip()
        if new_value:
            if key == "Length (min)":
                try:
                    new_value = int(new_value)
                except ValueError:
                    print("Length must be a number. Keeping old value.")
                    continue
            item[key] = new_value

    print("Item updated.")


# make a function that allows the user to remove a book from the library
def delete_item(library):
    show_simple_list(library)
    try:
        index = int(input("Enter index to delete: "))
        if index < 0 or index >= len(library):
            print("Invalid index.")
            return
        library.pop(index)
        print("Item deleted.")
    except ValueError:
        print("Invalid number.")


# make a while loop that allows the user to choose which function they want to use until they choose to exit the program
# make a conditional statement that allows the user to choose which function they want to use
# allow the user to reload the library from the csv file
# allow the user to exit the program
def main():
    file_path = input("Enter CSV file path (or press Enter for default 'library.csv'): ").strip()
    if file_path == "":
        file_path = "library.csv"

    library = load_library(file_path)
    unsaved_changes = False

    while True:
        print("""
Choose an option:
1. Show simple list
2. Show detailed list
3. Add item
4. Update item
5. Delete item
6. Save library
7. Reload library
8. Exit
""")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            show_simple_list(library)

        elif choice == "2":
            show_detailed_list(library)

        elif choice == "3":
            add_item(library)
            unsaved_changes = True

        elif choice == "4":
            update_item(library)
            unsaved_changes = True

        elif choice == "5":
            delete_item(library)
            unsaved_changes = True

        elif choice == "6":
            save_library(file_path, library)
            unsaved_changes = False

        elif choice == "7":
            confirm = input("Reloading will discard unsaved changes. Continue (Y/N): ").lower()
            if confirm == "y":
                library = load_library(file_path)
                unsaved_changes = False

        elif choice == "8":
            if unsaved_changes:
                save = input("You have unsaved changes. Save before exiting (Y/N): ").lower()
                if save == "y":
                    save_library(file_path, library)
            print("Goodbye.")
            break

        else:
            print("Invalid choice.")


main()