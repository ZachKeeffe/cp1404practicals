"""
CP1404/CP5632 Practical
UnreliableCar class tests

Unreliable cars are exactly that - unreliable. The point of this class is to see whether the car will manage
to complete it's drive each time.
"""

from prac_08.unreliable_car import UnreliableCar


def main():
    """Test some UnreliableCars."""

    # create cars with different reliabilities
    good_car = UnreliableCar("Mostly Good", 100, 95)
    average_car = UnreliableCar("Average", 100, 50)
    bad_car = UnreliableCar("Dodgy", 100, 9)

    # attempt to drive the cars many times
    # output what distance they drove
    for i in range(1, 12):
        print("Attempting to drive {}km:".format(i))
        print("{:12} drove {:2}km".format(good_car.name, good_car.drive(i)))
        print("{:12} drove {:2}km".format(average_car.name, average_car.drive(i)))
        print("{:12} drove {:2}km".format(bad_car.name, bad_car.drive(i)))

    # print the final states of the cars
    print(good_car)
    print(average_car)
    print(bad_car)
main()