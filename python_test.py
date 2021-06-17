x = [100,110,120,130,140,150] #question1
y=[]
for a in x:
    b=a*5
    y.append(b)
print(y)

def divisible_by_three(n):#question2
    m=range(1,n)
    for i in m:
        if i % 3==0:
          print(f"{i} is divisible by three")

divisible_by_three(10)

x = [[1,2],[3,4],[5,6]] #question3
y=[]
for sublist in x:
    for items in sublist:
        y.append(items)
print(y)

def smallest(a): #question4, find smallest num in the list.
    a.sort()
    print(f"The smallest number in the list is {min(a)}")
smallest([5,2,3,4,1,10,9,7,8,6])

x = ['a','b','a','e','d','b','c','e','f','g','h'] #question5, use a set to remove duplicate values.
y=set(x)
print(y)

def divisible_by_seven(): #question6
    a=range(100,200)
    b=[] #this is my empty list that will store the numbers divisible by 7.
    for i in a:
        if i%7==0:
            b.append(i)
    print(b)
divisible_by_seven()

def greet(): #question7
     students = [{"age": 19, "name": "Eunice"},{"age": 21, "name": "Agnes"},{"age": 18, "name": "Teresa"},{"age": 22, "name": "Asha"}]
     for student in students:
         print(f"The student's name is {student['name']} and they are {student['age']} years old.")
greet()      

class Rectangle: #question8
    def __init__(self,width,length):   #I will give the parameters values when I instantiate the class.
        self.width=width
        self.length=length
    def area(self):
        a=self.width*self.length
        print(f"the area of the rectangle is {a}")
    def perimeter(self):
        p=self.length+self.width
        print(f"The perimeter of the rectangle is {p}")



