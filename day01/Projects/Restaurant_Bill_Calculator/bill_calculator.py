"""
Restaurant bill calculator — Day 1 project.
Asks for the food total and a tip percentage,
then prints a clean itemised bill.
"""

GST_RATE = 0.05

print("=" * 40)
print("     THE SPICE ROUTE - BILL")
print("=" * 40)

table_number = input("Table number:")
food_total = float(input("Food total (₹):"))
tip_percent = float(input("Tip % (0 if none): "))

gst = food_total * GST_RATE
tip = food_total * (tip_percent / 100)
grand_total = food_total + gst + tip

print("-" * 40)
print(f"Table               : {table_number}")
print(f"Food                : ₹{food_total:>10,.2f}")
print(f"GST (5%)            : ₹{gst:>10,.2f}")
print(f"Tip ({tip_percent:.0f}%)            : ₹{tip:>10,.2f}")
print(f"TOTAL               : ₹{grand_total:>10,.2f}")
print("=" * 40)
print("Thank you, come again!")
