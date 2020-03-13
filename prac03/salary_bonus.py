"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""


def main():
    acceptable_input = False
    sales = 0
    while not acceptable_input:
        try:
            sales = float(input("Enter sales: $"))
            acceptable_input = True
        except ValueError:
            print("Sorry, I didn't understand that. Remember, only numbers are accepted.")
    if sales >= 0:
        bonus = calc_bonus(sales)
        print("Total Sales:" + str(sales) + "\nTotal Bonus:" + str(bonus))


def calc_bonus(sales):
    if sales >= 1000:
        bonus_amount = sales * 0.15
    else:
        bonus_amount = sales * 0.10
    return bonus_amount


main()
