def main():
    item_count = int(input("Number of Items: "))
    total_price = 0
    while item_count < 0:
        print("Invalid number of items.")
        item_count = int(input("Number of Items: "))
    for i in range(item_count):
        price = int(input("Please enter the price of item " + str(i + 1) + ": "))
        total_price += price
    final_price = calc_final_cost(total_price)
    print("Total Price: $" + str(final_price))


def calc_final_cost(total_price):
    if total_price >= 100:
        total_price = total_price * 0.9
    return total_price


main()
