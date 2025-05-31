# initialize a class
class employee:
    # speacial method/ magic method/ dunder method - constructor
    def __init__(self):
        self.id = 123
        self.salary = 50000 
        self.designation = "SDE"
        
    def travel(self, destination):
        print(f"Employee is now travelling to {destination}.")
        
        
# creating a object/instance of the class
sam = employee()


#print(sam.salary)  # accessing the attribute of the class
#print(sam.id) # accessing the attribute of the class
#print(sam.designation)  # accessing the attribute of the class
sam.travel("Rajsthan") # calling the method of the class