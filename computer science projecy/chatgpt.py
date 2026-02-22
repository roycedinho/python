# Shop Program for Mobile Devices, SIM Cards, and Accessories

# Function to display welcome message and get user info
def get_user_info():
    name = input("Please enter your name: ").strip()
    while name == "":
        print("Error: Name cannot be empty.")
        name = input("Please enter your name: ").strip()
    gender = input("Please enter your gender (M/F): ").strip().upper()
    while gender not in ["M", "F"]:
        print("Error: Gender must be 'M' or 'F'.")
        gender = input("Please enter your gender (M/F): ").strip().upper()
    print(f"\nWelcome {name}! Enjoy shopping at our store.\n")
    return name, gender

# Data structure for items: dictionary with item code as key
products = {
    "BPCM": {"category": "phone", "description": "compact", "price": 29.99},
    "BPSH": {"category": "phone", "description": "clam shell", "price": 49.99},
    "RPSS": {"category": "phone", "description": "RoboPhone - 5-inch screen and 64 GB memory", "price": 199.99},
    "RPLL": {"category": "phone", "description": "RoboPhone - 6-inch screen and 256 GB memory", "price": 499.99},
    "YPLS": {"category": "phone", "description": "Y-Phone Standard - 6-inch screen and 64 GB memory", "price": 549.99},
    "YPLL": {"category": "phone", "description": "Y-Phone Deluxe - 6-inch screen and 256 GB memory", "price": 649.99},
    "RTMS": {"category": "tablet", "description": "RoboTab - 8-inch screen and 64 GB memory", "price": 149.99},
    "RTLM": {"category": "tablet", "description": "RoboTab - 10-inch screen and 256 GB memory", "price": 299.99},
    "YTLM": {"category": "tablet", "description": "Y-Tab Standard - 10-inch screen and 128 GB memory", "price": 499.99},
    "YTLL": {"category": "tablet", "description": "Y-Tab Standard - 10-inch screen and 256 GB memory", "price": 599.99},
    "SMNO": {"category": "sim card", "description": "SIM Free (no SIM card purchased)", "price": 0},
    "SMPG": {"category": "sim card", "description": "Pay As You Go (SIM card purchased)", "price": 9.99}
}

# Function to display products by category
def display_products(category):
    print(f"\nAvailable {category}s:")
    for code, info in products.items():
        if info["category"] == category:
            print(f"{code}: {info['description']} - ${info['price']:.2f}")

# Function to get a valid item code
def get_item_choice(category):
    display_products(category)
    choice = input(f"Enter the item code for the {category} you want: ").strip().upper()
    while choice not in products or products[choice]["category"] != category:
        print("Error: Invalid choice. Please enter a valid item code.")
        choice = input(f"Enter the item code for the {category} you want: ").strip().upper()
    return choice

# Function to ask SIM preference for phones
def get_sim_choice():
    print("\nSIM options for phones:")
    print("1: SIM Free (SMNO) - $0")
    print("2: Pay As You Go (SMPG) - $9.99")
    choice = input("Enter 1 for SIM Free or 2 for Pay As You Go: ").strip()
    while choice not in ["1", "2"]:
        print("Error: Please enter 1 or 2.")
        choice = input("Enter 1 for SIM Free or 2 for Pay As You Go: ").strip()
    return "SMNO" if choice == "1" else "SMPG"

# Function to get quantity
def get_quantity():
    quantity = input("Enter the quantity you want to purchase: ").strip()
    while not quantity.isdigit() or int(quantity) <= 0:
        print("Error: Quantity must be a positive number.")
        quantity = input("Enter the quantity you want to purchase: ").strip()
    return int(quantity)

# Main program
def main():
    name, gender = get_user_info()
    purchased_items = []

    while True:
        print("\nCategories: phone, tablet, sim card")
        category = input("Enter the category you want to shop (or 'exit' to finish): ").strip().lower()
        if category == "exit":
            print("\nThank you for shopping with us. Have a great day!")
            break
        if category not in ["phone", "tablet", "sim card"]:
            print("Error: Invalid category. Choose 'phone', 'tablet', or 'sim card'.")
            continue

        item_code = get_item_choice(category)
        # If phone, ask for SIM option
        if category == "phone":
            sim_code = get_sim_choice()
            purchased_items.append({"code": sim_code, "quantity": 1})
        quantity = get_quantity()
        purchased_items.append({"code": item_code, "quantity": quantity})

        # Display current purchase
        print("\nCurrent items in your cart:")
        total_price = 0
        for item in purchased_items:
            info = products[item["code"]]
            item_total = info["price"] * item["quantity"]
            total_price += item_total
            print(f"{info['description']} (Code: {item['code']}), Quantity: {item['quantity']}, Unit Price: ${info['price']:.2f}, Total: ${item_total:.2f}")
        print(f"Current total price: ${total_price:.2f}")

    # Final receipt
    if purchased_items:
        print("\n--- Final Receipt ---")
        total_price = 0
        for item in purchased_items:
            info = products[item["code"]]
            item_total = info["price"] * item["quantity"]
            total_price += item_total
            print(f"{info['description']} (Code: {item['code']}), Quantity: {item['quantity']}, Unit Price: ${info['price']:.2f}, Total: ${item_total:.2f}")
        print(f"Total amount to pay: ${total_price:.2f}")

# Run program
if __name__ == "__main__":
    main()