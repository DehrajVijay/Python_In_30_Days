"""
Digital ID card - Day 1 project.
Collects details, converts types correctly, and prints a formatted card.
"""

print("let's build your ID card.\n")

full_name = input("Full name            :")
age = int(input("Age            :"))
height_m = float(input("Height in metres     :"))
city = input("city")
is_student = input("Are you a student ? (yes/no): ").strip().lower() =="yes"
nickname = input("Nickname (Enter to skip)    :") or None

birth_year = 2026 - age
height_cm = height_m * 100


print("\n" + "╔" + "═" * 38 + "╗")
print("‖" + "DIGITAL ID CARD".center(38)+ "‖")
print("╠" + "═" * 38 + "╣")
print(f"‖ Name      : {full_name:<25}‖")
print(f"‖ Nickname  : {str(nickname):<25}‖")
print(f"‖ Age       : {age:<25}‖")
print(f"‖ Born      : {birth_year:<25}‖")
print(f"‖ Height    : {height_cm:<25.0f} cm ‖")
print(f"‖ City      : {city:<25}‖")
print(f"‖ Student   : {str(is_student):<25}‖")
print("╚" + "═" * 38 + "╝")

print("\n--- What Python sees ---")
print(f"{type(full_name)=}")
print(f"{type(age)=}")
print(f"{type(height_m)=}")
print(f"{type(is_student)=}")
print(f"{type(nickname)}")



