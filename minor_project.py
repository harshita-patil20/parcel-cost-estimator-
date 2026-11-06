# Shared Bill Splitter
# A simple console program that splits a bill between friends.

print("=====================================")
print("        SHARED BILL SPLITTER         ")
print("=====================================")

split_again = "yes"

while split_again == "yes" or split_again == "y":

    while True:
        try:
            bill_amount = float(input("\nEnter the total bill amount: "))
            if bill_amount <= 0:
                print("The bill must be greater than 0. Please try again.")
            else:
                break  # valid value, leave this loop
        except ValueError:
            print("Invalid input! Please enter a number (for example 450 or 99.50).")

    while True:
        try:
            extra_percent = float(input("Enter tip/tax percentage (enter 0 if none): "))
            if extra_percent < 0:
                print("The percentage cannot be negative. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a number (for example 10 or 0).")

    while True:
        try:
            number_of_people = int(input("Enter the number of people splitting the bill: "))
            if number_of_people < 1:
                print("There must be at least 1 person. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a whole number (for example 4).")

    # Step 4: Do the calculations
    extra_charges = bill_amount * extra_percent / 100
    final_total = bill_amount + extra_charges
    amount_per_person = final_total / number_of_people

    # Step 5: Show the summary (:.2f means 2 decimal places)
    print("\n------------- SUMMARY -------------")
    print(f"Original bill    : {bill_amount:.2f}")
    print(f"Extra charges    : {extra_charges:.2f}")
    print(f"Final total      : {final_total:.2f}")
    print(f"Number of people : {number_of_people}")
    print(f"Each person pays : {amount_per_person:.2f}")
    print("-----------------------------------")

    split_again = input("\nDo you want to split another bill? (yes/no): ").strip().lower()

print("\nThank you for using Shared Bill Splitter. Goodbye!")
