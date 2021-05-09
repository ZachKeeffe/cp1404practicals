from prac_08.car import Car
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "Press 'C' to Choose Taxi\nPress 'D' to take a Taxi for a Drive\nPress 'Q' to Quit"


def main():
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    print("Let's Drive!")
    print(MENU)
    menu_input = input(">>> ").upper()
    while menu_input != "Q":
        if menu_input == "C":
            # Choose taxi from 'Taxis' list
            print("Choose Your Taxi:")
            display_taxis(taxis)
            correct_input = False
            while not correct_input:
                try:
                    taxi_choice = int(input("Choose taxi: "))
                    try:
                        current_taxi = taxis[taxi_choice]
                        correct_input = True
                    except IndexError:
                        print("Invalid taxi choice; select between 0 - {}".format(len(taxis) - 1))
                except ValueError:
                    print("Entry must be a number between 0 - {}".format(len(taxis) - 1))
            print("Bill to Date {:.2f}".format(total_bill))
        elif menu_input == "D":
            if current_taxi:
                current_taxi.start_fare()
                correct_input = False
                while not correct_input:
                    try:
                        distance_to_drive = float(input("Drive how far? "))
                        current_taxi.drive(distance_to_drive)
                        correct_input = True
                    except ValueError:
                        print("Entry must be numeric")

                trip_cost = current_taxi.get_fare()
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name,
                                                             trip_cost))
                total_bill += trip_cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid Menu Option")
        print(MENU)
        menu_input = input(">>> ").upper()
    print("Thanks for using Taxi Simulator\nTotal trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display numbered list of taxis."""
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()
