INVENTORY_FILE = "inventory.txt"
failed_attempts = 0


def load_inventory():
    orders = []
    try:
        with open(INVENTORY_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                order_id, product_name, quantity = line.split(",")
                orders.append((int(order_id), product_name, int(quantity)))
    except FileNotFoundError:
        pass
    return orders


def save_inventory(orders):
    with open(INVENTORY_FILE, "w") as f:
        for order_id, product_name, quantity in orders:
            f.write(f"{order_id},{product_name},{quantity}\n")


def display_orders(orders):
    print("Current Orders:")
    for order_id, product_name, quantity in orders:
        print(f"{order_id}, {product_name}, {quantity}")
    print("-" * 34)


def get_valid_input():
    global failed_attempts
    while True:
        product_name = input("Enter Product Name (or 'quit to exit): ")
        if product_name.lower() == "quit":
            return None, None

        quantity = input("Enter Quantity: ")
        if quantity.lower() == "quit":
            return None, None

        try:
            quantity = int(quantity)
        except ValueError:
            print("Error! Please enter a valid number!")
            failed_attempts += 1
            continue

        if quantity < 0:
            print("Quantity cannot be a negative number!")
            failed_attempts += 1
            continue

        return product_name, quantity


def get_next_order_id(orders):
    if not orders:
        return 1001
    return max(order_id for order_id, _, _ in orders) + 1


def total_stock(orders):
    return sum(quantity for _, _, quantity in orders)


def generate_report(orders, failed_attempts):
    print()
    print("=== Audit Report ===")
    print(f"Total Transactions Recorded: {len(orders)}")
    print(f"Total Units Processed: {total_stock(orders)}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")


def main():
    orders = load_inventory()
    display_orders(orders)

    while True:
        product_name, quantity = get_valid_input()
        if product_name is None:
            save_inventory(orders)
            print(f"Order successfully saved to {INVENTORY_FILE}")
            break

        new_id = get_next_order_id(orders)
        orders.append((new_id, product_name, quantity))

        print("\nNew Order Added:")
        print(f"{new_id},{product_name},{quantity}\n")

        save_inventory(orders)
        print(f"Order successfully saved to {INVENTORY_FILE}")

        if total_stock(orders) > 500:
            print("Stock exceeded 500!")
            break

    generate_report(orders, failed_attempts)


if __name__ == "__main__":
    main()