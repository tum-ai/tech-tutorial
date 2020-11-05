# Some function
def greet(name):
    print("Hello {}".format(name))


# A class
class Person:
    # Constructor
    def __init__(self, name):
        self.name = name
        self.age = 25

    # Some method
    def print_data(self):
        print("{} is {} years old".format(self.name, self.age))

# This is the main entry point for the program.
if __name__=='__main__':
    # Input
    print('Hello, world!')

    # Output
    name = input('What is your name?\n')
    print('Hi, %s.' % name)

    # Arrays
    friends = ['john', 'pat', 'gary', 'michael']
    for i, name in enumerate(friends):
        print("iteration {iteration} is {name}".format(iteration=i, name=name))
    print(friends[-1])

    # Function call
    greet("Horst")

    # Dictionaries
    prices = {'apple': 0.40, 'banana': 0.50}
    print("An apple costs: {}".format(prices['apple']))

    # Classes
    person = Person("Horst")
    person.print_data()