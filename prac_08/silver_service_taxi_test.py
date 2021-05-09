from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Test a Silver Service Taxi."""

    fancy_taxi = SilverServiceTaxi("Fancy Taxi", 100, 2)
    fancy_taxi.drive(18)
    print(fancy_taxi)
    print(fancy_taxi.get_fare())


main()
