class Cal():
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def add(self):
        return self.number1 + self.number2

    def sub(self):
        return self.number1 - self.number2

    def mul5(self):
        return self.number1 * self.number2

    def div(self):
        return self.number1 / self.number2


number1 = int(input('enter first number:'))
number2 = int(input('enter second number:'))
ob = Cal(number1, number2)
while True:
    def menu():
        my_choice = ('1.Add\n 2.Sub\n 3.Mul\n 4.div')
        print(my_choice)


    menu()
    choice = int(input("select your choice"))
    if choice == 1:
        print("result:", ob.add())
    elif choice == 2:
        print("result:", ob.sub())
    elif choice == 3:
        print("result:", ob.mul5())
    elif choice == 4:
        print("result:", ob.div())
    elif choice == 0:
        print("Try Again Later")
        break
    else:
        print("Invalid")
        break
print()


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
