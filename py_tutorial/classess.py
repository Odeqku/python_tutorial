import sys

class Flight:
    def __init__(self, capacity: int) -> str:
        self.capacity = capacity
        self.passengers = []
        self.open_seats = 0
        self.passengers_exc = []

    def __str__(self) -> str:

        if len(self.passengers) <= self.capacity:
            return f"{self.__class__.__name__} capacity is {self.capacity} and number of passengers is {len(self.passengers)}"
        else:
            return f"{self.__class__.__name__} is at capacity now"

    def add_passengers(self):

        for name in sys.argv[1:]:
            self.passengers.append(name)


    def open_seat(self) -> str:
        return f"Numbber of open_seats is {self.capacity - len(self.passengers)}"

def main():
    
    flight = Flight(3)
    flight.add_passengers()
    print(flight)
    print(flight.open_seat())
    
    """
    if len(flight.passengers) > flight.capacity:
        print(f"An excess of {flight.open_seat()}")
    """

if __name__ == "__main__":
    main()
