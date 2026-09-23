# NOTE: I Typed the entire code, It could have tying errors so please ignore.

"""
Bank Account ATM Menu -Day 5 project.
A menu-driven ATM till with PIN entry, deposits, withdrawals,
balance enquiry and a mini statement.
Uses only Days 1-5: no functions yet (Day 6), no files yet (Day 7),
no exception handling yet (Day 8).

"""

MIN_BALANCE = 500.0
MAX_WITHDRAWL = 20_000.0
NOTE_SIZE = 100

balance = 12_500.0
history = []  # list of (kind, amount, balance_after)

# SECURITY-REVIEW : a hardcoded PIN is acceptable only in a teaching scropt.
# A real system never stores a PIN in source code and never compares it in plain text. It stores a salted hash (bcrypt or argon2) loaded
# from an environment variable or a secrets manager, and compares hashes.
# You build the correct version on Day 25.

CORRECT_PIN = "1234"

MENU = """
+========================================+
|   MUMBAI CENTRAL BANK  ·  ATM  #4471   |
+========================================+
|  1  Deposit                            |
|  2  Withdraw                           |
|  3  Balance                            |
|  4  Mini statement                     |
|  5  Exit                               |
+========================================+"""

# 1. Authentication : a while  loop with a hard attempt limit -
# The 'else' on the while fires only if we never hit 'break'.

attempts = 0
while attempts < 3:
    pin = input("Enter 4-digit PIN: ").strip()
    attempts += 1

    if not pin.isdigit() or len(pin) != 4:
        print(f"  ! A PIN is exactly 4 digits. {3 - attempts} attempt(s) left.")
        continue
    if pin == CORRECT_PIN:
        print("\nPIN accepted. Welcome, Vijay")
        break

    print(f" ! Wrong PIN. {3-attempts} attempts(s) left.")

else:
    print("\nCard retained. Please contact your branch.")
    raise SystemExit  # stops the program cleanly (Day 8 explains raise)

# 2. The main menu loop --
while True:
    print(MENU)
    choice = input("Choose 1-5  ").strip()

    match choice:

        case "1":
            raw = input("  Amount to deposit ₹: ").strip()
            # allow one decimal point, nothing else
            if not raw.replace(".", "", 1).isdigit():
                print(" ! Digits only. Nothing was deposited.")
                continue
            amount = float(raw)
            if amount <= 0:
                print(" ! A deposit must be more than zero.")
                continue
            balance += amount
            history.append(("DEPOSIT", amount, balance))
            print(f" Deposited ₹{amount:,.2f}. Balance ₹{balance:,.2f}")

        case "2":
            raw = input(" Amount  to withdraw ₹: ").strip()
            if not raw.isdigit():
                print(" ! Whole ruees only, digits only.")
                continue
            amount = float(raw)
            if amount % NOTE_SIZE != 0:
                print("f ! This  ATM dispenses multiples of ₹{NOTE_SIZE} only.")
                continue
            if amount > MAX_WITHDRAWL:
                print(f" !Per-transaction limit is ₹{MAX_WITHDRAWL:,.0f}.")
                continue
            if balance - amount < MIN_BALANCE:
                shortfall = MIN_BALANCE - (balance - amount)
                print(f" ! Insufficient funds. You must leave ₹{MIN_BALANCE:,.0f}.")
                print(f"   You are ₹{shortfall:,.2f} short.")
                continue
            balance -= amount
            history.append(("WITHDRAW", amount, balance))
            print(f" Dispensed ₹{amount:,.2f}. Balance ₹{balance:,.2f}")

        case "3":
            print(f" Available balance: ₹{balance:,.2f}")
            print(f" withdrawable now: ₹{balance - MIN_BALANCE:,.2f}")

        case "4":
            if not history:
                print("  No transactions this session.")
                continue
            print(f"\n  {'#':<3} {'TYPE':<10} {'AMOUNT':>15} {'BALANCE':>15}")
            print("  " + "-" * 46)
            for i, (kind, amount, after) in enumerate(history, start=1):
                sign = "+" if kind == "DEPOSIT" else "-"
                print(f"  {i:<3} {kind:<10} {sign}{amount:>14,.2f} {after:>15,.2f}")
            deposits = sum(a for k, a, _ in history if k == "DEPOSIT")
            withdrawals = sum(a for k, a, _ in history if k == "WITHDRAW")
            print("  " + "-" * 46)
            print(
                f"  {len(history)} transaction(s) · in ₹{deposits:,.2f} · out ₹{withdrawals:,.2f}"
            )

        case "5":
            print("\n Please collect your card. Thank you.")
            break

        case _:
            print("  ! Choose a number from 1-5.")
