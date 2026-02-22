# YEAR 10 COMPUTER SCIENCE PROJECT 2026
# BY ROYCE OMOTAYO-YOMES AND ANJOLA TAPERE 10.5 COMPUTER SCIENCE

# ==========================================================
#                FUTURELINK TECHNOLOGIES
#              Connecting You to Tomorrow
# ==========================================================
# Website: www.futurelinktech.com
# 24/7 Support Line: support@futurelinktech.com

# -------------------- USER INFORMATION --------------------
def get_user_info():
    print("==========================================================")
    print("             WELCOME TO FUTURELINK TECHNOLOGIES")
    print("Connecting You to Tomorrow")
    print("Website: www.futurelinktech.com")
    print("24/7 Support Line: support@futurelinktech.com")
    print("==========================================================")
    name = input("Enter your full name: ").strip()
    while name == "":
        print("ERROR: Name cannot be empty.")
        name = input("Enter your full name: ").strip()
    age = input("Enter your age: ").strip()
    while not age.isdigit() or int(age) <= 0:
        print("ERROR: Please enter a valid positive age.")
        age = input("Enter your age: ").strip()
    age = int(age)
    print("Gender options: M / F / P")
    gender = input("Enter your gender: ").strip().upper()
    while gender not in ["M", "F", "P"]:
        print("ERROR: Enter M for Male, F for Female, or P for Prefer not to say.")
        gender = input("Enter your gender: ").strip().upper()
    if gender == "M":
        title = "Mr."
    elif gender == "F":
        title = "Miss."
    else:
        title = ""
    print("----------------------------------------------------------")
    if title != "":
        print(f"Welcome {title} {name}, you are {age} years old.")
    else:
        print(f"Welcome {name}, you are {age} years old.")
    print("Please follow the prompts to complete your purchase.")
    print("----------------------------------------------------------")
    return name, title, age

# -------------------- PRODUCT DATA --------------------
phones = {
    "BPCM": {"Description": "Compact Phone", "price": 29.99},
    "BPSH": {"Description": "Clam Shell Phone", "price": 49.99},
    "RPSS": {"Description": "RoboPhone 5 inch 64GB", "price": 199.99},
    "RPLL": {"Description": "RoboPhone 6 inch 256GB", "price": 499.99}
}
tablets = {
    "RTMS": {"Description": "RoboTab 8 inch 64GB", "price": 149.99},
    "RTLM": {"Description": "RoboTab 10 inch 256GB", "price": 299.99}
}
sims = {
    "SMNO": {"Description": "SIM Free", "price": 0.00},
    "SMPG": {"Description": "Pay As You Go SIM", "price": 9.99}
}

# -------------------- DISPLAY FUNCTION --------------------
def display_items(items, title):
    print("==========================================================")
    print(f"                    {title}")
    print("==========================================================")
    for code, info in items.items():
        print(f"{code} | {info['Description']} | £{info['price']:.2f}")
    print("----------------------------------------------------------")

# -------------------- MAIN PROGRAM --------------------
def main():
    name, title, age = get_user_info()
    cart = []
    shopping = True
    while shopping:
        print("\nSelect a category to purchase from:")
        print("1 - Phone")
        print("2 - Tablet")
        print("3 - SIM Card")
        category_choice = input("Enter option number (1/2/3): ").strip()

        # ---------------- PHONE ----------------
        if category_choice == "1":
            display_items(phones, "AVAILABLE PHONES")
            phone_code = input("Enter the phone code you wish to buy: ").strip().upper()
            while phone_code not in phones:
                print("ERROR: Invalid phone code.")
                phone_code = input("Enter a valid phone code: ").strip().upper()
            quantity = input("Enter phone quantity: ").strip()
            while not quantity.isdigit() or int(quantity) <= 0:
                print("ERROR: Quantity must be a positive number.")
                quantity = input("Enter phone quantity: ").strip()
            quantity = int(quantity)
            cart.append({
                "description": phones[phone_code]["Description"],
                "price": phones[phone_code]["price"],
                "quantity": quantity
            })
            print("\nChoose SIM option for this phone:")
            display_items(sims, "SIM OPTIONS")
            sim_choice = input("Enter SIM code (SMNO or SMPG): ").strip().upper()
            while sim_choice not in sims:
                print("ERROR: Invalid SIM choice.")
                sim_choice = input("Enter SIM code (SMNO or SMPG): ").strip().upper()
            sim_quantity = input("Enter SIM quantity: ").strip()
            while not sim_quantity.isdigit() or int(sim_quantity) <= 0:
                print("ERROR: Quantity must be a positive number.")
                sim_quantity = input("Enter SIM quantity: ").strip()
            sim_quantity = int(sim_quantity)
            cart.append({
                "description": sims[sim_choice]["Description"],
                "price": sims[sim_choice]["price"],
                "quantity": sim_quantity
            })

        # ---------------- TABLET ----------------
        elif category_choice == "2":
            display_items(tablets, "AVAILABLE TABLETS")
            tablet_code = input("Enter the tablet code you wish to buy: ").strip().upper()
            while tablet_code not in tablets:
                print("ERROR: Invalid tablet code.")
                tablet_code = input("Enter a valid tablet code: ").strip().upper()
            quantity = input("Enter quantity: ").strip()
            while not quantity.isdigit() or int(quantity) <= 0:
                print("ERROR: Quantity must be a positive number.")
                quantity = input("Enter quantity: ").strip()
            quantity = int(quantity)
            cart.append({
                "description": tablets[tablet_code]["Description"],
                "price": tablets[tablet_code]["price"],
                "quantity": quantity
            })

        # ---------------- SIM ONLY ----------------
        elif category_choice == "3":
            display_items(sims, "AVAILABLE SIM CARDS")
            sim_code = input("Enter the SIM code you wish to buy: ").strip().upper()
            while sim_code not in sims:
                print("ERROR: Invalid SIM code.")
                sim_code = input("Enter a valid SIM code: ").strip().upper()
            quantity = input("Enter quantity: ").strip()
            while not quantity.isdigit() or int(quantity) <= 0:
                print("ERROR: Quantity must be a positive number.")
                quantity = input("Enter quantity: ").strip()
            quantity = int(quantity)
            cart.append({
                "description": sims[sim_code]["Description"],
                "price": sims[sim_code]["price"],
                "quantity": quantity
            })
        else:
            print("ERROR: Invalid menu option.")
            continue
        continue_choice = input("\nDo you want to buy anything else? (Yes/No): ").strip().lower()
        while continue_choice not in ["yes", "no"]:
            print("ERROR: Please enter Yes or No.")
            continue_choice = input("Do you want to buy anything else? (Yes/No): ").strip().lower()
        if continue_choice == "no":
            shopping = False

    # -------------------- RECEIPT --------------------
    if cart:
        print("\n==========================================================")
        print("                     FINAL RECEIPT")
        print("==========================================================")
        if title != "":
            print(f"Customer: {title} {name}")
        else:
            print(f"Customer: {name}")
        print(f"Age: {age}")
        print("----------------------------------------------------------")
        total_cost = 0
        for item in cart:
            item_total = item["price"] * item["quantity"]
            total_cost += item_total
            print(f"Item: {item['description']}")
            print(f"Unit Price: £{item['price']:.2f}")
            print(f"Quantity: {item['quantity']}")
            print(f"Total: £{item_total:.2f}")
            print("----------------------------------------------------------")
        print(f"GRAND TOTAL: £{total_cost:.2f}")
        print("==========================================================")
        print("Thank you for choosing FutureLink Technologies")
        print("==========================================================")
    else:
        print("No items purchased.")
# -------------------- RUN PROGRAM --------------------
if __name__ == "__main__":
    main()