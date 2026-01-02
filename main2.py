import pandas
from abc import ABC, abstractmethod  # Abstract Base Class and abstractmethod

df = pandas.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    water_mark = "The Real Estate Company"  # class variable

    def __init__(self, hotel_id):
        self.hotel_id = hotel_id  # instance variable
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

    @classmethod
    def get_hotel_count(cls, data):    # class method
        return len(data)

    def __eq__(self, other):  # magic method for equality comparison
        if self.hotel_id == other.hotel_id:
            return True
        else:
            return False


class Ticket(ABC):

    @abstractmethod
    def generate(self):
        pass


class ReservationTicket(Ticket):
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are you booking data:
        Name: {self.the_customer_name}
        Hotel name: {self.hotel.name}
        """
        return content

    @property  # property decorator to define a getter method
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name

    @staticmethod
    def convert(amount):  # static method
        return amount * 1.2  # Example conversion logic


class DigitalTicket(Ticket):
    def generate(self):
        content = f"""
        This is your digital ticket!
        Name: {self.the_customer_name}
        Hotel name: {self.hotel.name}
        Enjoy your stay!
        """
        return content


hotel1 = Hotel(hotel_id="188")
hotel2 = Hotel(hotel_id="188")
