Project Description:

This code demonstrates the concepts of abstraction, encapsulation, inheritance, polymorphism in object-oriented programming. Abstraction and encapsulation are achieved through the Person class. It serves as a base class for other classes and provides common functionality and abstraction. The constructor initializes the _name and _age attributes for encapsulation. The display_info method is an abstract method that must be implemented by subclasses. Inheritance and polymorphism are demonstrated through the Student and Teacher classes. The Student class inherits from the Person class and adds a student_id attribute. The Teacher class also inherits from the Person class and adds an employee_id attribute. Both classes override the display_info method to provide class-specific information. The display_person_info function accepts a Person object or its subclasses and calls the display_info method. This showcases polymorphism, where the same function can operate on different types of objects. In the usage section, a Student object and a Teacher object are created with specified attributes. The display_person_info function is called with both objects, demonstrating polymorphism in action.

