# Week 3 assignment.  create a program taht 
# takes user input for a car and outputs it
# using classes.

#parent class
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

#next class, calling back to the parent
#using the super function
class Automobile(Vehicle):
    def __init__(self, vehicle_type):
        super().__init__(vehicle_type)
        self.year = None
        self.make = None
        self.model = None
        self.doors = None
        self.roof = None
    
#setting the details of it.
    def set_details(self, year, make, model, doors, roof):
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    
#returning the info
    def __str__(self):
        return f"Vehicle type: {self.vehicle_type}\n" \
               f"Year: {self.year}\n" \
               f"Make: {self.make}\n" \
               f"Model: {self.model}\n" \
               f"Number of doors: {self.doors}\n" \
               f"Type of roof: {self.roof}"

def main():
    # Accept user input for car detailz
    vehicle_type = "car"
    year = input("Enter the year of the car: ")
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sun roof): ")
    
    # Create an instance of Automobile and set details
    car = Automobile(vehicle_type)
    car.set_details(year, make, model, doors, roof)
    
    # Output the car details
    print("\nHere are the details of the car:")
    print(car)

if __name__ == "__main__":
    main()
