'''
Introduction to Classes and Object Oriented Programming (OOP) in Python:

Define a class, so we can reuse it by creating an instances. The self parameter, refer to instance being created, and it uses the attributes and method of
the class within the class definition.
'''

class Pet:
  def __init__(self, name, species):
    self.name = name
    self.species = species

  def introduce(self):
      print(f"Hello, my name is {self.name} and I am a {self.species}.")
    
# --------------------------------
# Create an instance of the class
# --------------------------------

cat = Pet("Baby", "British Short Hair")

# --------------------------------
# Access the attributes of the instance
# --------------------------------

cat.name
>> Baby
cat.species
>> British Short Hair

# --------------------------------
# Call the method of the instance
# --------------------------------

cat.introduce() # Output : Hello, my name is Baby and I am a British Short Hair.

# --------------------------------
# Update the attribute of the instances
# --------------------------------

cat.name = "Tom"
cat.species = "American Curl"

cat.name # Output: Tom
cat.species # Output: American Curl


