item_count = int(input("Number of Items: "))
total_price = 0
while item_count < 0:
    print("Invalid number of items.")
    item_count = int(input("Number of Items: "))
for i in range(item_count):
    price = float(input("Please enter the price of item " + str(i + 1) + ": "))
    total_price += price
if total_price > 100:
    total_price *= 0.9
print("Total Price for {} items is ${:.2f}".format(item_count, total_price))
