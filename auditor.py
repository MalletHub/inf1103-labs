inventory = 0;

while True:
    stock = input("Enter Stock Quantity(or 'quit'): ")

    if stock.lower() == "quit":
        break


    if stock.startswith("-") and stock[1:].isdigit():
        print("Stock cannot be a negative number!")
        continue


    if not stock.isdigit():
        print("Error! Please enter a valid number! ")
        continue

    stock = int(stock)




