class Shape:
    def __init__(self,type):
        self.type=type

    def calc_area(self):
        pass
    def calc_peri(self):
        pass

class Rectangle(Shape):
    def __init__(self):
        super().__init__("Rectangle")
        self.length=float(input("enter the length of the rectangle"))
        self.width=float(input("enter the width of the rectangle"))

    def calc_area(self):
        return self.length*self.width
    def calc_peri(self):
        return 2*(self.length+self.width)

class Circle(Shape):
    def __init__(self):
        super().__init__("Circle")
        self.radius=float(input("enter the radius of the circle"))
    def calc_area(self):
        return 3.14 * self.radius ** 2
    def calc_peri(self):
        return 2 * 3.14 * self.radius

class Square(Rectangle):
    def __init__(self):
        super().__init__()
        self.type="Square"
    def calc_peri(self):
        return 4 * self.width

class Triangle(Shape):
    def __init__(self):
        super().__init__("Triangle")
        self.base=float(input("enter the base: "))
        self.height=float(input("enter the height: "))
        self.s1=float(input("enter the value of side one: "))
        self.s2= float(input("enter the value of 2nd side: "))
        self.s3= float(input("enter the value of 3rd side: "))

    def calc_area(self):
        return 0.5 * self.base * self.height

    def calc_peri(self):
        return self.s1 + self.s2 + self.s3

def main():

        # Prompt user to select a shape
    print("Select a shape:")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Square")
    print("4. Triangle")
    shape_MyChoice = int(input())

        # Create a new object based on the selected shape
    if shape_MyChoice == 1:
        shape = Rectangle()
    elif shape_MyChoice == 2:
        shape = Circle()
    elif shape_MyChoice == 3:
        shape = Square()
    elif shape_MyChoice == 4:
        shape = Triangle()
    else:
        print("Invalid choice")
        return

    print("Shape type:",shape.type)
    print("Area:", shape.calc_area())
    print("Perimeter:",shape.calc_peri())

if __name__ == '__main__':
    main()

    # This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
   # print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
