inventory = 0
failed = 0

while True:
    stock = input("Enter Stock Quantity(or 'quit'): ")

    if stock.lower() == "quit":
        break


    if stock.startswith("-") and stock[1:].isdigit():
        print("Stock cannot be a negative number!")
        failed += 1
        continue


    if not stock.isdigit():
        print("Error! Please enter a valid number! ")
        failed += 1
        continue

    stock = int(stock)


    inventory += stock
    print(f"Current Total Inventory: {inventory}")

    if inventory > 500:
        print("Stock exceeded 500! Please follow up! ")
        break



print(f"Total Inventory: {inventory}")
print(f"Failed entries: {failed}")




