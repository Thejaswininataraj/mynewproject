# person.py

class Person:
    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

# Main function to create and use the class
def main():
    person1 = Person("Alice", 25)
    person2 = Person("Bob", 30)

    person1.greet()
    person2.greet()

if __name__ == "__main__":
    main()
