# Abstraction and encapsulation
class Person:
    # The `Person` class serves as a base class for other classes, providing common functionality and abstraction.
    def __init__(self, name, age):
        # The constructor initializes the `_name` and `_age` attributes for encapsulation.
        self._name = name
        self._age = age

    def display_info(self):
        # This is an abstract method, indicating that subclasses must implement their own version of it.
        raise NotImplementedError("Subclasses must implement abstract method")

    def get_name(self):
        # Getter method to access the `name` attribute in an encapsulated manner.
        return self._name
    
    def get_age(self):
        # Getter method to access the `age` attribute in an encapsulated manner.
        return self._age

# Inheritance and polymorphism
class Student(Person):
    # `Student` class inherits from the `Person` class, utilizing inheritance to gain the `Person`'s functionality.
    def __init__(self, name, age, student_id):
        # The constructor initializes the attributes specific to `Student`, using `super()` to call the `Person` constructor.
        super().__init__(name, age)
        self._student_id = student_id

    def display_info(self):
        # This method implements the abstract method from the base `Person` class.
        # It returns a formatted string containing `Student`-specific information.
        return f"Student: {self._name}, Age: {self._age}, Student ID: {self._student_id}"

class Teacher(Person):
    # `Teacher` class also inherits from `Person`, demonstrating inheritance and polymorphism.
    def __init__(self, name, age, employee_id):
        # The constructor initializes `Teacher`-specific attributes and calls the base class constructor.
        super().__init__(name, age)
        self._employee_id = employee_id

    def display_info(self):
        # This method implements the abstract method, returning a formatted string with `Teacher`-specific information.
        return f"Teacher: {self._name}, Age: {self._age}, Employee ID: {self._employee_id}"

# Polymorphism
def display_person_info(person):
    # This function accepts a `Person` object or its subclasses and calls `display_info`.
    # This is an example of polymorphism, where the same function can operate on different types of objects.
    print(person.display_info())

# Usage
student1 = Student("Alyn", 21, "S001")
# Create a `Student` object with specified name, age, and student ID.

teacher1 = Teacher("Mr. Smith", 40, "T001")
# Create a `Teacher` object with specified name, age, and employee ID.

display_person_info(student1)
# Calls `display_person_info` with a `Student` object, demonstrating polymorphism.

display_person_info(teacher1)
# Calls `display_person_info` with a `Teacher` object, also demonstrating polymorphism.
