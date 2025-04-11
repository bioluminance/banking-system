import os

# Ensure the data files exist
if not os.path.exists("accounts.txt"):
    open("accounts.txt", "w").close()

if not os.path.exists("transactions.txt"):
    open("transactions.txt", "w").close()

def display_menu():
    print("\n--- Banking System Menu ---")
    print("1. Create Account")
    print("2. View Accounts")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. View Transactions")
    print("6. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter account holder's name: ")
            balance = input("Enter initial deposit amount: ")

            with open("accounts.txt", "a") as file:
                file.write(f"{name},{balance}\n")

            print("✅ Account created successfully!")

        elif choice == '2':
            try:
                with open("accounts.txt", "r") as file:
                    accounts = file.readlines()
                    if not accounts:
                        print("⚠️ No accounts found.")
                    else:
                        print("\n--- Account List ---")
                        for acc in accounts:
                            name, balance = acc.strip().split(",")
                            print(f"Name: {name}, Balance: ₹{balance}")
            except FileNotFoundError:
                print("❌ accounts.txt not found.")
        elif choice == '3':
            name_to_deposit = input("Enter account holder's name: ")
            amount = float(input("Enter amount to deposit: "))
            updated = False

            lines = []
            with open("accounts.txt", "r") as file:
                for line in file:
                    name, balance = line.strip().split(",")
                    if name == name_to_deposit:
                       new_balance = float(balance) + amount
                       lines.append(f"{name},{new_balance}\n")
                       updated = True
                    else:
                       lines.append(line)

            if updated:
               with open("accounts.txt", "w") as file:
                    file.writelines(lines)
               with open("transactions.txt", "a") as tfile:
                    from datetime import datetime
                    date = datetime.now().strftime("%Y-%m-%d")
                    tfile.write(f"{name_to_deposit},Deposit,{amount},{date}\n")
               print(f"💰 Deposit successful! ₹{amount} added.")
            else:
               print("❌ Account not found.")

        elif choice == '4':
                name_to_withdraw = input("Enter account holder's name: ")
                amount = float(input("Enter amount to withdraw: "))
                updated = False

                lines = []
                with open("accounts.txt", "r") as file:
                   for line in file:
                       name, balance = line.strip().split(",")
                       if name == name_to_withdraw:
                          if float(balance) >= amount:
                             new_balance = float(balance) - amount
                             lines.append(f"{name},{new_balance}\n")
                             updated = True
                          else:
                             print("❌ Insufficient balance.")
                             lines.append(line)
                             updated = True  # Still mark as found to avoid 'not found' message
                       else:
                           lines.append(line)

                if updated:
                   with open("accounts.txt", "w") as file:
                        file.writelines(lines)
                   if float(balance) >= amount:
                      from datetime import datetime
                      date = datetime.now().strftime("%Y-%m-%d")
                      with open("transactions.txt", "a") as tfile:
                           tfile.write(f"{name_to_withdraw},Withdrawal,{amount},{date}\n")
                      print(f"💸 Withdrawal of ₹{amount} successful!")
                else:
                    print("❌ Account not found.")

        elif choice == '5':
         try:
            with open("transactions.txt", "r") as file:
                 transactions = file.readlines()
                 if not transactions:
                     print("📂 No transactions recorded yet.")
                 else:
                     print("\n--- Transaction History ---")
                 for t in transactions:
                     acc_no, trans_type, amount, date = t.strip().split(",")
                     print(f"{date} | {acc_no} | {trans_type} | ₹{amount}")
         except FileNotFoundError:
             print("❌ transactions.txt not found.")

        elif choice == '6':
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
