# ATM Simulator

# Account details
balance = 10000.00
correct_pin = "1234"
attempts = 0
max_attempts = 3

# PIN verification
while attempts < max_attempts:
    entered_pin = input("Enter your ATM PIN: ")

    if entered_pin == correct_pin:
        print("PIN verified successfully. Welcome!")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts

        if remaining > 0:
            print("Incorrect PIN. You have", remaining, "attempt(s) left.")
        else:
            print("Too many incorrect attempts. Your ATM access is blocked.")

# Show the ATM menu only after successful PIN verification
if attempts < max_attempts:
    while True:
        print("\nATM Menu")
        print("1. Check Account Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        try:
            option = int(input("Enter your choice number: "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 4.")
            continue

        if option < 1 or option > 4:
            print("Invalid option. Please choose a number from 1 to 4.")

        elif option == 1:
            print("Your Account Balance is: ₦", format(balance, ".2f"))

        elif option == 2:
            try:
                deposit = float(input("Enter your deposit amount: "))
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue

            if deposit <= 0:
                print("Invalid deposit amount. Please enter an amount greater than zero.")
            else:
                balance += deposit
                print("Deposit successful!")
                print("Your new account balance is: ₦", format(balance, ".2f"))

        elif option == 3:
            try:
                withdraw = float(input("Enter your withdrawal amount: "))
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue

            if withdraw <= 0:
                print("Invalid withdrawal amount. Please enter an amount greater than zero.")
            elif withdraw > balance:
                print("Insufficient funds.")
            else:
                balance -= withdraw
                print("Withdrawal successful!")
                print("Your new account balance is: ₦", format(balance, ".2f"))

        elif option == 4:
            print("Thank you for using this application!")
            print("Your final account balance is: ₦", format(balance, ".2f"))
            break