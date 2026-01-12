# BB 1st Financial Calculator Project

def savings_time_calculator():
    # Calculates how long it will take to reach a savings goal
    print("\n--- Savings Time Calculator ---")
    goal = float(input("What amount are you saving to: "))

    print("\nHow often are you contributing?")
    print("1. Weekly")
    print("2. Monthly")
    frequency = int(input("> "))

    deposit = float(input("How much are you contributing each time: "))

    # Time required depends on whether the user contributes weekly or monthly
    if frequency == 1:
        weeks = goal / deposit
        print(f"\nIt will take {round(weeks)} weeks to save ${goal:.2f}")
    else:
        months = goal / deposit
        print(f"\nIt will take {round(months)} months to save ${goal:.2f}")


def compound_interest_calculator():
    # Calculates compound interest over a number of years
    print("\n--- Compound Interest Calculator ---")
    principal = float(input("Starting Amount: "))
    rate = float(input("Interest Rate Percent: ")) / 100
    years = int(input("Years Spent Compounding: "))

    # Inner function: applies one year of interest
    # This demonstrates scope because it uses the 'rate' variable
    def apply_interest(amount):
        return amount * (1 + rate)

    total = principal

    # Apply interest once per year
    for _ in range(years):
        total = apply_interest(total)

    print(f"\nAt the end of {years} years you will have ${total:.2f}")


def budget_allocator():
    # Divides a user's income into categories based on percentages
    print("\n--- Budget Allocator ---")
    num_categories = int(input("How many budget categories do you have: "))

    categories = []
    for i in range(num_categories):
        name = input(f"Category {i+1}: ")
        categories.append(name)

    income = float(input("What is your monthly income: "))

    percentages = []
    for name in categories:
        percent = float(input(f"What percent is your {name}: "))
        percentages.append(percent)

    print()
    # Calculate and display the dollar amount for each category
    for name, percent in zip(categories, percentages):
        amount = income * (percent / 100)
        print(f"{name} is ${amount:.2f}")


def sale_price_calculator():
    # Calculates the final price after a discount
    print("\n--- Sale Price Calculator ---")
    original = float(input("How much does the item originally cost: "))
    discount = float(input("What percent is the discount: ")) / 100

    final_price = original * (1 - discount)
    print(f"\nThe item now costs ${final_price:.2f}")


def tip_calculator():
    # Calculates a tip amount and total bill
    print("\n--- Tip Calculator ---")
    bill = float(input("How much is the bill: "))
    tip_percent = float(input("What percent of a tip are you giving: ")) / 100

    tip_amount = bill * tip_percent
    total = bill + tip_amount

    print(f"\nThe tip amount is ${tip_amount:.2f} and your total is ${total:.2f}")


def main():
    # Main menu loop — keeps running until the user chooses to exit
    while True:
        print("\n==============================")
        print("   Financial Calculator Menu")
        print("==============================")
        print("Enter the number to select an option:")
        print("1. Savings Time Calculator")
        print("2. Compound Interest Calculator")
        print("3. Budget Allocator")
        print("4. Sale Price Calculator")
        print("5. Tip Calculator")
        print("6. Exit")

        choice = input("> ")

        # Call the correct function based on user choice
        if choice == "1":
            savings_time_calculator()
        elif choice == "2":
            compound_interest_calculator()
        elif choice == "3":
            budget_allocator()
        elif choice == "4":
            sale_price_calculator()
        elif choice == "5":
            tip_calculator()
        elif choice == "6":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid option. Try again.")


# Start the program
main()
