"""
Text Report formatter - Day 02 project.
Take ONE messy raw line of customer data, cleans every field, validates it,
 masks the phone number, and prints and aligned card.
 Uses only Day 1 + Day 2 concepts: operators, strings, f-strings.
"""

# The kind of line a real system actually emails you:
# extra spaces, random capitals, inconsistent padding.

RAW = "  priya   sharma ,PRIYA.SHARMA@Example.COM , 9876543210 ,  48250.5 , mumbai  "

WIDTH = 46
BAR = "─" * WIDTH
# - Step 1 . cut the line into filds ------------------

name_raw, email_raw, phone_raw, amount_raw, city_raw = RAW.split(",")

# - Step 2 email: normalise, then validate---------------

name = " ".join(name_raw.split()).title()


# ── Step 3 · email: normalise, then validate ───────────────────
email = email_raw.strip().casefold()
local, at, domain = email.partition("@")
email_ok = bool(at) and bool(local) and "." in domain


# - Step 4 phone: keep digits only, then mask-----------------
digits = phone_raw.strip().replace(" ", "").replace("-", "")

phone_ok = digits.isdigit() and len(digits) == 10
phone_shown = ("X" * 6 + digits[-4:]) if phone_ok else "INVALID NUMBER"

# - Step 5 money: text -> float -> formatted currency-------
amount = float(amount_raw.strip())
amount_shown = f"₹{amount:,.2f}"

# - Step 6 city---

city = city_raw.strip().upper()

# Step 7 overall verdict

status = "OK" if (email_ok and phone_ok) else "NEEDS REVIEW"

# - Step 8 drwa the card
print("┌" + BAR + "┐")
print("│" + "CUSTOMER RECORD".center(WIDTH) + "│")
print("├" + BAR + "┤")
print(f"| {'Name':<12}{name:<32} |")
print(f"| {'Email':<12}{email:<32} |")
print(f"| {'Phone':<12}{phone_shown:<32} |")
print(f"| {'Amount':<12}{amount_shown:<32} |")
print(f"| {'City':<12}{city:<32} |")
print("├" + BAR + "┤")
print(f"| {'Status':<12}{status:<32} |")
print("└" + BAR + "┘")

# ── Step 9 · the cleaning log, so you can see the work ──────────
print("\n--- cleaning log ---")
print(f"raw lenght                  :{len(RAW)}")
print(f"spaces in the raw line      :{RAW.count(' ')}")
print(f"'@' found at index          :{email.find('@')}")
print(f"domain ends with .com       :{domain.endswith('.com')}")
print(f"local part is alphanumeric  :{local.replace('.', '').isalnum()}")
print(f"record id                   :INV-{'7'.zfill(4)}")
print(f"initials                    :{name[0]}.{name.split()[1][0]}.")
print(f"city, display case          :{city.capitalize()}")
print(f"'priya' appears in raw      :{'priya' in RAW.lower()}")
print(f"name right-aligned to 20    :[{name.rjust(20)}]")
print(f"name reversed               :{name[::-1]}")
