# initialize a class
class employee:
    # speacial method/ magic method/ dunder method - constructor
    def __init__(self):
        #print("Started executing the attributes/data")
        self.id = 123
        self.salary = 50000 
        self.designation = "SDE"
        #print("attributes/data initialized successfully")
        
    def travel(self, destination):
        print("This travel functio was called manually")
        print(f"Employee is now travelling to {destination}.")
        
        
# creating a object/instance of the class
sam = employee()


#print(sam.salary)  # accessing the attribute of the class
#print(sam.id) # accessing the attribute of the class
#print(sam.designation)  # accessing the attribute of the class

# calling the method of the class
#sam.travel("Rajsthan") 

#print(type(sam))  # checking the type of the object

# Outside attributes
sam.name = "Vikas Jangid"
print(sam.name)