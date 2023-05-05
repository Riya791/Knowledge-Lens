class cal():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        return self.x+self.y
    def sub(self):
        return self.x-self.y
    def mul5(self):
        return self.x*self.y
    def div(self):
        return self.x/self.y
x=int(input('enter first number:'))
y=int(input('enter second number:'))
ob=cal(x,y)
while True:
    def menu():
        My_choice=('1.Add\n 2.Sub\n 3.Mul\n 4.div')
        print(My_choice)
    menu()
    Choice=int(input("select your choice"))
    if Choice==1:
        print("result:",ob.add())
    elif Choice==2:
        print("result:",ob.sub())
    elif Choice==3:
        print("result:",ob.mul())
    elif Choice==4:
        print("result:",ob.div())
    elif Choice==0:
        print("Try Again Later")
        break
    else:
        print("Invalid")
        break
print()
