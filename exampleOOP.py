# Define a class called Person
class Person():

    # Define it's constructor
    def __init__(self,firstName:str,lastName:str):
        # first name is only visible inside of Person and is automatically has the first letter capitalized
        self.__firstName = firstName.title()
        # Same for last name. See above
        self.__lastName = lastName.title()
        
    # Because our variables are Private, we need some way to access them outside
    # of the Person class.
    # this can be done by defining methods called "getters" and "setters"
    # A getter returns the value. You can use it to control how the variable
    # Is accessed. I could force the programmer to only access the capitalized version
    # of lastName
    def readLastName(self):
        return self.__lastName.upper()
    
    def readFirstName(self):
        return self.__firstName
    
    # we can force the user to update a variable only following our set rules
    # Now they can update name but it has to be in title case
    def setLastName(self,newLastName:str):
        self.__lastName = newLastName.title()

# Create a person
myPerson:Person = Person("TiM","dRaKe")
# Update the last name
myPerson.setLastName("DrakE")
# Read the name using the getter we built
print(myPerson.readLastName())


# Define a class called pet. this will be the base/parent/super class
class Pet():

    # Define it's attributes
    def __init__(self,name,age,adoptionDate):
        self.name = name.title()
        self.age = age
        self.adoption_date = adoptionDate
    
    # Give it a method
    def makeHumanHappy(self):
        return "The pet's owner is now happy"
    
    # Give it another method
    def move(self):
        return f"{self.name} has moved from point A to point B"


# Create a class called Dog that inherits from pet
class Dog(Pet):

    # We need to get all the information to create a pet because a 
    # dog IS a pet. We also need to get the extra information associated with dogs
    # that is not associated with pets
    def __init__(self,name,age,adoptionDate,breed,furColor):
        # Because dog IS a pet we need to send that information to the pet constructor
        # This allows us to reuse the code from before without having to copy and paste
        super().__init__(name,age,adoptionDate)
        # Now we can create the extra information
        self.breed = breed
        self.fur_color = furColor

    # We automatically get all the methods associated with pets. We actually want
    # the move to behave differently because we are a dog not just a generic pet
    
    def move(self):
        return f"{self.name} walked from point A to point B"
    

# A Fish IS a Pet so we can use inheritance again so we don't have to duplicate code.
class Fish(Pet):

    
    def __init__(self, name, age, adoptionDate,scaleColor,waterType):
        # Pass name, age, and adoptionDate to the Pet class so that we take
        # advantage of the code we already wrote
        super().__init__(name, age, adoptionDate)
        # Create two new attributes
        self.scale_color = scaleColor
        self.waterType = waterType

    def move(self):
        # Override move to that it says "swam" instead of moved
        return f"{self.name} swam from point A to point B"


# Here is a default pokemon class. This is the base/parent/super class
class Pokemon():

    # Here we define it's base attributes
    def __init__(self,name,hp) -> None:
        self.name = name
        self.hp = hp
        self.attackList = []

    # Here we define an attack method that chooses a random attack from the 
    # pokemon's attackList
    def attack(self):
        import random
        return f"{self.name} used the attack " + random.choice(self.attackList)
    
    # Here we define a method that chooses a pokemon's moveset based on an available list
    def chooseMoveset(self):
        import random
        possibleMoves = ["Quick Attack","Tackle"]
        self.attackList.append(random.choice(possibleMoves))
        self.attackList.append(random.choice(possibleMoves))

# a Firetype Pokemon IS a Pokemon so we can use inheritance
class FirePokemon(Pokemon):

    # FirePokemon have the exact same attributes as other Pokemon
    def __init__(self, name, hp) -> None:
        super().__init__(name, hp)
    
    # We like almost everything about Pokemon. We just want the chooseMoveset 
    # to work slightly differently.
    def chooseMoveset(self):
        import random
        # Override chooseMoveset so that we can have Flame Thrower on FirePokemon
        possibleMoves = ["Quick Attack","Tackle","Flame Thrower"]
        self.attackList.append(random.choice(possibleMoves))
        self.attackList.append(random.choice(possibleMoves))
    

# Here is a Pokemon object
evee = Pokemon("Eevee",100)
# Here is a FirePokemon Object
charmander = FirePokemon("Charmander",150)

# Here is the result of overriding. Charmander has the chance of getting Flame Thrower
charmander.chooseMoveset()
# Here is the original. Evee can only get Quick Attack or Tackle
evee.chooseMoveset()

# Print out a chosen attack for each pokemon (Fire and regular)
print(evee.attack())
print(charmander.attack())

# This is how the Dog class would look if we didn't take advantage of Inheritance
class Dog():

    def __init__(self,name,age,adoptionDate,breed,furColor):
        # These three are all duplicated from the Pet Class
        self.name = name
        self.age = age
        self.adoption_date = adoptionDate

        # These two are new
        self.breed = breed
        self.fur_color = furColor
    
    # Because we didn't inherit, we had to recreate the makeHumanHappy method
    def makeHumanHappy(self):
        print("The pet's owner is now happy")

# Create a Dog Object
myDog = Dog("Dallas",3,"12/25/2023","Lab","White")

# Create a Pet Object
myPet = Pet("Fluffy",4,"12/25/2021")

# Call the makeHumanHappy method for each one
print(myPet.makeHumanHappy())
print(myDog.makeHumanHappy())


# Here we talk about Encapsulation. We are breaking down a complex 
# object into smaller parts. Each part becomes it's own object

# Here is one way of making an object with an object inside of it.
# If you follow this method, deleting a car will delete the associated Engine
class Car():

    def __init__(self,color,model,make,cost,cylinders,fuel_type,engine_cost):
        self.color = color
        self.model = model
        self.make = make
        self.cost = cost
        self.engine = Engine(cylinders,fuel_type,engine_cost)
        

class Engine():
    def __init__(self,cylinders,fuel_type,cost) -> None:
        self.cylinders = cylinders
        self.fuel_type = fuel_type
        self.cost = cost

myCar = Car("Green","Honda","Accord",12000,6,"Gas",230)

# Here is the other way to have an object as an attribute. This is when you pass
# the other object in as a parameter. When you delete the car, the engine will still exist
class Car():

    def __init__(self,color,model,make,cost,engine):
        self.color = color
        self.model = model
        self.make = make
        self.cost = cost
        self.engine = engine
        

class Engine():
    def __init__(self,cylinders,fuel_type,cost) -> None:
        self.cylinders = cylinders
        self.fuel_type = fuel_type
        self.cost = cost

# Create the engine
v6 = Engine(6,"Gas",240)
# Create the car using the engine as a parameter
myCar = Car("Blue","Honda","Accord",12000,v6)

# Regardless of how you set an attribute to be an object, this is how you print attributes
# of an object inside of another object
print(myCar.engine.fuel_type)

        