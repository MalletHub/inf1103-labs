inventory = 0
failed = 0
deliveries = 0


def get_valid_input():
    """Prompt for stock quantity, validate it, and return an int or None for 'quit'."""
    global failed
    while True:
        user_input = input("Enter Stock Quantity (or 'quit'): ")

        if user_input.lower() == "quit":
            return None

        if user_input.startswith("-") and user_input[1:].isdigit():
            print("Stock cannot be a negative number!")
            failed += 1
            continue

        if not user_input.isdigit():
            print("Error! Please enter a valid number!")
            failed += 1
            continue

        return int(user_input)


def process_delivery(current_total, new_value):
    """Add the delivery amount to the running total and return the new total."""
    return current_total + new_value


def calculate_tax(amount):
    """Return 10% tax on a single delivery amount."""
    tax_rate = 0.10
    return amount * tax_rate


def generate_report(total_deliveries, failed_attempts):
    """Print the final summary."""
    print("\n--- Audit Report ---")
    print(f"Total Deliveries Processed: {total_deliveries}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")


def main():
    global inventory, deliveries

    while True:
        stock = get_valid_input()
        if stock is None:
            break

        inventory = process_delivery(inventory, stock)
        deliveries += 1
        tax = calculate_tax(stock)

        print(f"Current Total Inventory: {inventory}")
        print(f"Tax on this delivery: ${tax:.2f}")

        if inventory > 500:
            print("Stock exceeded 500! Please follow up!")
            break

    generate_report(deliveries, failed)


if __name__ == "__main__":
    main()