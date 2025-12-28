import pandas as pd

df = pd.read_csv('hotels.csv',dtype={'id': str, 'name': str, 'available': str}) # Load the CSV file into a DataFrame


class Hotel: # Hotel class to manage hotel bookings
    def __init__(self, hotel_id): # Initialize with hotel ID
        self.hotel_id = hotel_id # Store hotel ID
        self.name = df.loc[df['id'] == hotel_id, "name"].squeeze() # Get hotel name from DataFrame
        

    def book(self):
        '''Book the hotel by updating its availability in the DataFrame and saving it back to the CSV file.'''
        df.loc[df['id'] == self.hotel_id, "available"] = 'no' # Update availability to 'no'
        df.to_csv('hotels.csv', index=False)

    def available(self):
        # Check if hotel is available
        availability = df.loc[df['id'] == self.hotel_id, "available"].squeeze()
        if availability == 'yes':
            return True
        else:
            return False

class ReservationTicket: # Class to generate reservation tickets
    def __init__(self, customer_name, hotel_object): # Initialize with customer name and hotel object
        self.customer_name = customer_name
        self.hotel = hotel_object # Store hotel object

    def generate(self): # Generate reservation ticket content
        content = f'''Thank you for your reservation, 
        Here are your booking data:
         Name : {self.customer_name}
         Hotel name: {self.hotel.name}'''
        return content
        


print(df)
hotel_ID = input("Enter hotel id: ")
hotel = Hotel(hotel_ID)

if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(customer_name=name,hotel_object=hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel not available")