inventory = 0
failed_attempts = 0
def get_valid_input():
    global failed_attempts
    while True:
        stock = input("Enter Stock Quantity (or 'quit'): ")

        if stock.lower() == "quit":
            return None

        try:
            stock = int(stock)
        except ValueError:
            print("Error! Please enter a valid number!")
            failed_attempts += 1
            continue

        if stock < 0:
            print("Stock cannot be a negative number!")
            failed_attempts += 1
            continue

        return stock

def process_delivery(current_total, new_value): 
    return current_total + new_value

def calculate_tax(amount):
    tax_rate = 0.10
    return amount * tax_rate


def generate_report(total_units, failed_attempts): 
    print(f"Total Inventory: {total_units}")
    print(f"Failed entries: {failed_attempts}")

while True:
    stock = get_valid_input()
    if stock is None:
        break
    inventory = process_delivery(inventory, stock)
    print(f"Current Total Inventory: {inventory}")
    print(f"Tax $: {calculate_tax(stock):.2f}")

   

    if inventory > 500:
        print("Stock exceeded 500!!!!!")
        break

generate_report(inventory, failed_attempts) 






























