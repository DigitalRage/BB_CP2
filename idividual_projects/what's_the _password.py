import random

# Returns a random lowercase letter for the password
def random_lower():
    return random.choice("abcdefghijklmnopqrstuvwxyz")

# Returns a random uppercase letter for the password
def random_upper():
    return random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

# Returns a random number character for the password
def random_number():
    return random.choice("0123456789")

# Returns a random special character for the password
def random_special():
    return random.choice("!@#$%^&*()-_=+[]{}|;:',.<>?/`~")


# Asks the user for a number and keeps asking until they enter a valid positive integer.
# This prevents the program from crashing if the user types something invalid.
def get_int(prompt):
    while True:
        value = input(prompt)
        if value.isdigit() and int(value) > 0:
            return int(value)
        print("Please enter a valid positive number.")


# Asks the user a yes/no question and keeps asking until they enter Y or N.
# Converts the answer into True or False so the rest of the program is easier to write.
def get_yes_no(prompt):
    while True:
        value = input(prompt).strip().lower()
        if value in ("y", "n"):
            return value == "y"
        print("Please type Y or N.")


# Builds a password that guarantees at least one of each selected character type.
# First adds one required character from each chosen type, then fills the rest randomly,
# and finally shuffles the characters so the password looks natural.
def make_password(length, use_lower, use_upper, use_numbers, use_special):
    char_functions = []
    required_chars = []

    # Add one required character for each selected type
    if use_lower:
        char_functions.append(random_lower)
        required_chars.append(random_lower())
    if use_upper:
        char_functions.append(random_upper)
        required_chars.append(random_upper())
    if use_numbers:
        char_functions.append(random_number)
        required_chars.append(random_number())
    if use_special:
        char_functions.append(random_special)
        required_chars.append(random_special())

    # Start the password with the required characters
    password_chars = required_chars.copy()

    # Fill the remaining characters randomly from the allowed types
    while len(password_chars) < length:
        func = random.choice(char_functions)
        password_chars.append(func())

    # Shuffle so required characters aren't always at the front
    random.shuffle(password_chars)

    # Convert list of characters into a string
    return "".join(password_chars)


# Collects all password requirements from the user.
# Forces the user to choose at least one character type before continuing.
def get_settings():
    length = get_int("How long does the password need to be: ")

    while True:
        use_lower = get_yes_no("Does it need lowercase letters (Y/N): ")
        use_upper = get_yes_no("Does it need uppercase letters (Y/N): ")
        use_numbers = get_yes_no("Does it need numbers (Y/N): ")
        use_special = get_yes_no("Does it need special characters (Y/N): ")

        # If at least one type is selected, continue
        if use_lower or use_upper or use_numbers or use_special:
            return length, use_lower, use_upper, use_numbers, use_special

        # Otherwise, force the user to try again
        print("\nYou must select at least ONE type of character. Please try again.\n")


# Displays the main menu, handles user choices, and generates four passwords.
# This function controls the entire program flow.
def main():
    print("Welcome to the Random Password Generator!")
    print("This program will create four passwords based on your choices.\n")

    while True:
        print("1. Generate Passwords")
        print("2. Exit")

        choice = input("> ").strip()

        # If the user chooses to generate passwords, gather settings and create four results
        if choice == "1":
            length, lo, up, num, sp = get_settings()

            print("\nPossible Passwords:\n")
            for _ in range(4):
                print(make_password(length, lo, up, num, sp))
            print()

        # Ends the program
        elif choice == "2":
            print("Goodbye!")
            break

        # Handles invalid menu input
        else:
            print("Invalid choice. Please type 1 or 2.\n")


# Starts the program
main()
