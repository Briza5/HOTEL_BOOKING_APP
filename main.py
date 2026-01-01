import pandas as pd

# Load the CSV file into a DataFrame with specified data types
df = pd.read_csv('hotels.csv', dtype={
                 'id': str, 'name': str, 'available': str})
# Load the cards CSV file into a list of dictionaries with string data types
df_cards = pd.read_csv('cards.csv', dtype=str).to_dict(orient='records')


class Hotel:  # Hotel class to manage hotel bookings
    def __init__(self, hotel_id):  # Initialize with hotel ID
        self.hotel_id = hotel_id  # Store hotel ID
        # Get hotel name from DataFrame
        self.name = df.loc[df['id'] == hotel_id, "name"].squeeze()

    def book(self):
        '''Book the hotel by updating its availability in the DataFrame and saving it back to the CSV file.'''
        df.loc[df['id'] == self.hotel_id,
               "available"] = 'no'  # Update availability to 'no'
        df.to_csv('hotels.csv', index=False)

    def available(self):
        # Check if hotel is available
        availability = df.loc[df['id'] == self.hotel_id, "available"].squeeze()
        if availability == 'yes':
            return True
        else:
            return False


class ReservationTicket:  # Class to generate reservation tickets
    # Initialize with customer name and hotel object
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object  # Store hotel object

    def generate(self):  # Generate reservation ticket content
        content = f'''Thank you for your reservation, 
        Here are your booking data:
         Name : {self.customer_name}
         Hotel name: {self.hotel.name}'''
        return content


class CreditCard:  # Dummy CreditCard class for payment processing
    def __init__(self, number):  # Initialize with card details
        self.number = number

    def validate(self, expiration, cvc, holder):  # Dummy validation method
        card_data = {
            'number': self.number,
            'expiration': expiration,
            'cvc': cvc,
            'holder': holder}
        if card_data in df_cards:  # Check if card data exists in the loaded cards
            return True
        else:
            return False


# print list of hotels
print(df)
# User input for hotel ID
hotel_ID = input("Enter hotel id: ")
# Create Hotel instance object
hotel = Hotel(hotel_ID)
# Check availability and book if available
if hotel.available():
    # Create CreditCard instance (not used further in this example)
    credit_card = CreditCard(number="1234-5678-9876-5432")
    if credit_card.validate(expiration="12/26",
                            cvc="123", holder="JOHN SMITH"):
        # Call book method to book the hotel
        hotel.book()
        # User input for customer name
        name = input("Enter your name: ")
        # Create ReservationTicket instance and generate ticket
        reservation_ticket = ReservationTicket(
            customer_name=name, hotel_object=hotel)
        print(reservation_ticket.generate())
    else:
        print("There was an error with your payment")
else:
    print("Hotel not available")
