"""
Expense Tracker CLI — version 1 (Day 3).
Every expense is a tuple: (date, category, amount, note).
All expenses live in one list. This file demonstrates add, list,
sort, filter and total, and prints a formatted report.
Day 5 adds the menu loop. Day 6 turns these blocks into functions.
Day 7 saves it to a file.


"""

# - The data: a list of tuples------------------------------

expenses = [
    ("2026-08-01", "Food", 450.00, "Swiggy - office launch"),
    ("2026-08-01", "Travel", 120.00, "Auto to Andheri"),
    ("2026-08-03", "Groceries", 2340.50, "DMart monthly"),
    ("2026-08-05", "Food", 180.00, "Chai and samosa"),
    ("2026-08-07", "Bills", 1499.00, "Broadband"),
    ("2026-08-09", "Travel", 3200.00, "IRCTC Mumbai-Pune"),
    ("2026-08-12", "Food", 920.00, "Dinner with team"),
]

# Add : append a new tupple ---------

expenses.append(("2026-08-15", "Shopping", 2799.00, "Running shoes"))

WIDTH = 60
BAR = "─" * WIDTH

# LIST:the full table----

print("=" * WIDTH)
print("EXPENSE TRACKER . August 2026".center(WIDTH))
print("=" * WIDTH)
print(f"{'DATE':<12}{'CATEGORY':<12}{'AMOUNT':<12}  {'NOTE'}")
print(BAR)

for date, category, amount, note in expenses:
    print(f"{date:<12}{category:<12}{amount:>12,.2f}    {note}")

print(BAR)

total = sum(row[2] for row in expenses)
print(f"{'TOTAL':<24}{total:>12,.2f}")
print(f"{'ENTRIES':<24}{len(expenses):>12}")
print(f"{'AVERAGE':<24}{total / len(expenses):>12,.2f}")


# SORT: biggest spends first---
print("\n" + "=" * WIDTH)
print("TOP 3 SINGLE EXPENSES".center(WIDTH))
print("=" * WIDTH)


by_amount = sorted(expenses, key=lambda row: row[2], reverse=True)

for rank, (date, category, amount, note) in enumerate(by_amount[:3], start=1):
    print(f"{rank}. {category:<11}{amount:>10,.2f} {note}")

# --FILTER: only the big ones ---
print("\n" + "=" * WIDTH)
print("OVER ₹1,000".center(WIDTH))
print("=" * WIDTH)

big = [row for row in expenses if row[2] > 1000]

for date, category, amount, note in big:
    print(f"{date:<12}{category:<12}{amount:>12,.2f}")

print(BAR)
print(f"{'SUBTOTAL':<24}{sum(row[2] for row in big):>12,.2f}")
print(f"{'COUNT':<24}{len(big):>12}")


# GROUP: totals per category, without dictionaries---
# Tomorrow this becomes three lines with a dict. Today, hones work.
categories = []
for row in expenses:
    if row[1] not in categories:
        categories.append(row[1])

    categories.sort()

print("\n" + "=" * WIDTH)
print("BY CATEGORY".center(WIDTH))
print("=" * WIDTH)

for category in categories:
    cat_total = sum(row[2] for row in expenses if row[1] == category)
    percent = cat_total / total * 100
    bar = "█" * int(percent // 2)
    print(f"{category:<14}{cat_total:>12,.2f}{percent:>8.1f}% {bar}")


print(BAR)
print(
    f"Biggest category  : {max(categories, key=lambda c: sum(r[2] for r in expenses if r[1]==c))}"
)
print(f"Highest expense   : ₹{max(row[2] for row in expenses):,.2f}")
print(f"Lowest expense    : ₹{min(row[2] for row in expenses):,.2f}")
print(f"Any lower ₹5000   : {any(row[2] >5000 for row in expenses)}")
print(f"All have a note   : {all(row[3] for row in expenses)}")
