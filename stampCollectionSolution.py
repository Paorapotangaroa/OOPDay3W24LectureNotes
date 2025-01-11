# Name: Toa Pita
# Section: 002
# Description: This project tracks stamps that 
# various collectors have as well as the dollar ammount of the stamps

# Import the required libraries
import random

# Create the stamp class
class Stamp():
    # constructor, name, and dollar_value
    def __init__(self,name,dollar_value) -> None:
        self.name = name
        self.dollar_value = dollar_value

# Stamp Collector class
class StampCollector():
    def __init__(self,name):
        # set name
        self.name = name
        # set collection to an empty list
        self.collection = []

    # Displays the stamp collection
    def show_collection(self):
        # Print the collector's name
        print(f"{self.name}'s Stamp Collection:")
        # Keep a running total
        runningTotal = 0

        # Loop through each stamp. Update the running total based on the dollar_value of each stamp
        for stamp in self.collection:
            runningTotal += stamp.dollar_value
            # Display each stamp
            print(f"Stamp:{stamp.name}, Value:${stamp.dollar_value}")
        # Display the final collection total
        print(f"Total Collection Value: {round(runningTotal,2)}")
            
            
    # Show the most valuable stamp and it's dollar value
    def show_most_valuable_stamp(self):
        # If they only have one stamp it will be the most valuable
        topValueStamp = self.collection[0]
        # Loop through each stamp and check if it has a higher dollar value than the first stamp
        for stamp in self.collection:
            # If it does, update which stamp is the stamp with the highest value
            if stamp.dollar_value > topValueStamp.dollar_value:
                topValueStamp = stamp
        # Print the variable topValueStamp because it will be updated to be the highest value
        print(f"Highest value stamp: {topValueStamp.name}: ${round(topValueStamp.dollar_value,2)}")

# Stamp Seller inherits from stamp collector
class StampSeller(StampCollector):

    def __init__(self, name):
        # Pass the values up the chain to StampCollector
        super().__init__(name)
        # default is_certified to False
        self.is_certified = False

    def show_collection(self):
        # Print the collector's name
        print(f"{self.name}'s Stamp Collection:")
        # Track running total:
        runningTotal = 0

        # Loop through each stamp, update total value, print each stamp. Multiply each dollar_value by 1.1 to
        # increase the cost by 10%
        for stamp in self.collection:
            runningTotal += (stamp.dollar_value*1.1)
            print(f"Stamp:{stamp.name}, Value:${round(stamp.dollar_value*1.1,2)}")

        # Print total collection value
        print(f"Total Collection Value: {round(runningTotal,2)}")

    def show_most_valuable_stamp(self):
        # sort the collection based on it's price using my custom function below
        self.collection.sort(key=sortByPrice)
        # Once it is sorted the first position is the highest dollar ammount
        mostValue = self.collection[0]
        # Print it
        print(f"Highest value stamp: {mostValue.name}: ${round(mostValue.dollar_value*1.1,2)}")

# Define a sorting function
def sortByPrice(object):
    # Return the price multiplied by 1.1. This will be used to sort the objects in the self.collection list
    return round(object.dollar_value*1.1,2)

# Create a global list of sellars and collectors
collectorsAndSellers = []

# Gather input:
numStampCollectors = int(input("How many stamp collectors/sellers do you want to enter? "))

for counter in range(0,numStampCollectors):
    # Adding a blank line in the output:
    print()
    
    # Check if they are a seller or a collector
    collectorOrSeller = input(f"Is person #{counter+1} a regular collector or a seller? Enter \"s\" if they are a seller: ")

    # Build the correct object based on input
    if collectorOrSeller == "s":
        name = input("What is the seller's name? ")
        person = StampSeller(name)
    else:
        name = input("Enter the collector's name: ")
        person = StampCollector(name)

    # List of possible stamps
    stamp_names = ["Penny Black", "Treskilling Yellow", "Blue Mauritius", 
                    "Red Mauritius","Inverted Jenny","British Guiana 1-cent Magenta", 
                    "Hawaiian Missionaries", "Swedish Treskilling Yellow", 
                    "Perot Provisional", "Canada's 12d Black"]
    
    # Pick a random number of stamps 1-5 inclusive 
    randNumStamps = random.randint(1,5)

    # Pick that many stamps
    for stampNum in range(0,randNumStamps):
        # Create a stamp object using a random stamp name and stamp price
        stamp = Stamp(random.choice(stamp_names),random.randint(1,2000000))
        # Add the stamp object to the person object
        person.collection.append(stamp)
    
    # Add the completed person (either Seller or Collector) to the global list
    collectorsAndSellers.append(person)

# Loop through each person
for person in collectorsAndSellers:
    # Print their collections
    print()
    person.show_collection()
    # Print their top stamp
    print()
    person.show_most_valuable_stamp()



