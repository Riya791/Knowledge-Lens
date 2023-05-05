def add(a,b):
    return a + b    #This is a sample Python script.

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a/b

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    My_choice= input("Select your choice(1/2/3/4)")

    if My_choice in('1','2','3','4'):
        try:
            n1=float(input("first number"))
            n2=float(input("second number"))
        except ValueError:
            print("Invalid input")
            continue
        if My_choice == '1':
            print(n1, "+", n2, "=", add(n1, n2))

        elif My_choice == '2':
            print(n1, "-", n2, "=", subtract(n1, n2))

        elif My_choice == '3':
            print(n1, "*", n2, "=", multiply(n1, n2))

        elif My_choice == '4':
            print(n1, "/", n2, "=", divide(n1, n2))

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid Input")


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
