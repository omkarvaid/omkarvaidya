def om(): #omkar
    class student:
        def __init__(self,name,rollno):
            self.name=name
            self.rollno=rollno


    s1=student('omkar',2)
    s2=student('ram',6)
    print(s1.name,s1.rollno)
    print(s2.name,s2.rollno)






def om1():
    class student:
        def __init__(self, name, rollno):
            self.name = name
            self.rollno = rollno
        def show(self):
            print(self.name,self.rollno)

    s1 = student('omkar', 2)
    s2 = student('ram', 6)
    s1.show()
    s2.show()






def om2():
    class student:
        def __init__(self, name, rollno):
            self.name = name
            self.rollno = rollno
            self.lap=self.laptop()
        def show(self):
            print(self.name,self.rollno)
            self.lap.show()
        class laptop:
            def __init__(self):
                self.brand="hp"
                self.cpu="i5"
                self.ram="8"

            def show(self):
                print(self.brand, self.cpu,self.ram)


    s1 = student('omkar', 2)
    s2 = student('ram', 6)
    s1.show()
    s2.show()
    lap1=s1.lap
    lap2 =s2.lap
    print(id(lap1))
    print(id(lap2))




def om3():
    class A:
        def feature1(self):
            print("omkar1")
        def feature2 (self):
            print("omkar2")
    class B(A):
        def feature3(self):
            print("omkar3")
        def feature4 (self):
            print("omkar4")
    a1=A()
    a1.feature1()
    a1.feature2()
    b1=B()
    b1.feature3()
    b1.feature4()
    b1.feature1()
    b1.feature2()



def om4():
    class A:
        def __init__(self):
            print("in A Init")
        def feature1(self):
            print("omkar1")
        def feature2 (self):
            print("omkar2")
    class B(A):
        def feature3(self):
            print("omkar3")
        def feature4 (self):
            print("omkar4")
    a1 = B()




def om5():
    class A:
        def __init__(self):
            print("omkar1")
    class B:
        def __init__(self):
            print("omkar2")
    class C(A,B):
        def __init__(self):
            print("omkar3")
    a=C()




def om6():
    class pycham:
        def execute (self):
            print("compiling")
            print("running")
    class laptop:
        def code(self,ide):
            ide.execute()
    ide=pycham()
    lap1=laptop()
    lap1.code(ide)




def om7():
    class pycham:
        def execute (self):
            print("compiling")
            print("running")
    class myeidtor:
        def execute (self):
            print("compiling")
            print("running")
            print("style")
            print("rdx")
    class laptop:
        def code(self,ide):
            ide.execute()
    ide=myeidtor()
    lap1=laptop()
    lap1.code(ide)




def om8():
    a=5
    b=6
    print(a+b)
    print(int.__add__(a,b))

    a = 'omk'
    b = 'ar'
    print(a + b)
    print(str.__add__(a, b))




def om9():
    class student:
        def __init__(self,m1,m2):
            self.m1=m1
            self.m2=m2
        def __add__(self, other):
            m1=self.m1+other.m1
            m2 = self.m2 + other.m2
            s3=student(m1,m2)
            return (s3)
    s1=student(58,69)
    s2=student(60,65)
    s3=s1+s2
    print(s3.m1)
    print(s3.m2)



def om9():
    class student:
        def __init__(self,m1,m2):
            self.m1=m1
            self.m2=m2
        def __add__(self, other):
            m1=self.m1+other.m1
            m2 = self.m2 + other.m2
            s3=student(m1,m2)
            return (s3)
        def __gt__(self, other):
            r1=self.m1+self.m2
            r2=other.m1+other.m2
            if r1>r2:
                return True
            else:
                return False
    s1=student(58,69)
    s2=student(60,65)
    s3=s1+s2

    if s1>s2:
        print("s1 win")
    else:
        print("s2 win")





def om9():
    class student:
        def __init__(self,m1,m2):
            self.m1=m1
            self.m2=m2
        def sum(self,a,b):
            s=a+b
            return s
    s1=student(58,56)
    print(s1.sum(5,6))






def om9():
    class student:
        def __init__(self,m1,m2):
            self.m1=m1
            self.m2=m2
        def sum(self,a,b,c):
            s=a+b+c
            return s
    s1=student(58,56)
    print(s1.sum(5,6,9))




def om9():
    class student:
        def __init__(self,m1,m2):
            self.m1=m1
            self.m2=m2
        def sum(self,a=None,b=None,c=None):
            if a!=None and b!=None and c!=None:
                s=a+b+c
            elif a != None and b != None:
                s = a + b
            else:
                s = a
            return s
    s1=student(58,56)
    print(s1.sum(5))
#om9()




def om9():
    from abc import ABC, abstractmethod
    class computer(ABC):
        @abstractmethod
        def omkar(self):
            pass
    class loptop(computer):
        def omkar(self):
            print('omkar')
    com=loptop()
    com.omkar()
#om9()






def om9():
    num=[1,2,3,4,5]
    print(num)
    for a in num :
        print(a)
#om9()




def om9():
    num=[1,23,4,5,6]
    it=iter(num)
    print(next(it))
    print(next(it))
    print(next(it))
#om9()


def om9():
    num=[1,2,3,4,5]
    it=iter(num)
    print(it.__next__())
    print(it.__next__())
#om9()


def om9():
    num=[1,2,3,4,5]
    it=iter(num)
    print(it.__next__())
    print(it.__next__())
    for i in num:
        print(i)
#om9()





def om9():
    class topten:
        def __init__(self):
            self.num=1
        def __iter__(self):
            return self
        def __next__(self):
            val =self.num
            self.num+=1
            return val
    value=topten()
    for i in value:
        print(i)
#om9()





def om9():
    class topten:
        def __init__(self):
            self.num=1
        def __iter__(self):
            return self
        def __next__(self):
            if self.num<=10:
                val =self.num
                self.num+=1
                return val
            else:
                raise StopIteration
    value=topten()
    for i in value:
        print(i)
#om9()





def om9():
    def topten () :
        return 5

    value = topten()
    print(value)
    def topten():
        yield 1

    value=topten()
    print(value.__next__())
#om9()

def om9():
    def topten():
        yield 1
        yield 2
        yield 3
        yield 4
    value=topten()
    print(value.__next__())
    print(value.__next__())
    print(value.__next__())
#om9()



def om9():
    def topten():
        yield 1
        yield 2
        yield 3
        yield 4
    value=topten()
    for i in value:
        print(i)
#om9()


def om9():
    def topten():
        n=1
        while n<=10:
            s=n*n
            yield s
            n+=1
    value=topten()
    for a in value:
        print(a)
#om9()






def om9():
    a=5
    b=0
    try:
        print(a/b)
    except Exception :
        print("not possible")

    print("bye")
#om9()




def om9():
    a=5
    b=0
    try:
        print(a/b)
    except Exception as e:
        print("not possible",e)

    print("bye")
#om9()



def om9():
    a=int(input("1:"))
    b=int(input("2:"))
    try:
        print("resource open")
        print(a/b)
    except Exception as e:
        print("not possible",e)
    finally:
        print("resource close")

    print("bye")
#om9()





def om9():
    class hello:
        def way(self):
            for i in range(5):
                print("hello")
    class hi:
        def way(self):
            for i in range(5):
                print("hi")
    i=hello()
    i1=hi()
    i.way()
    i1.way()
#om9()


from time import sleep
from threading import *
class hello(Thread):
    def run(self):
        for i in range(5):
                print("hello")
                sleep(1)
class hi(Thread):
    def run(self):
         for i in range(5):
                print("hi")
                sleep(1)
i=hello()
i1=hi()
#i.start()
#i1.start()



from time import sleep
from threading import *
class hello(Thread):
    def run(self):
        for i in range(5):
                print("hello")
                sleep(1)
class hi(Thread):
    def run(self):
         for i in range(5):
                print("hi")
                sleep(1)
i=hello()
i1=hi()
#i.start()
sleep(0.3)
#i1.start()




from time import sleep
from threading import *
class hello(Thread):
    def run(self):
        for i in range(5):
                print("hello")
                sleep(1)
class hi(Thread):
    def run(self):
         for i in range(5):
                print("hi")
                sleep(1)
i=hello()
i1=hi()
#i.start()
sleep(0.3)
#i1.start()
#i.join()
#i1.join()

#print("bye")





def om9():
    f= open("omkar","r")
    print(f.read())
#om9()



def om9():
    f= open("joy","w")
    f.write("Name= Joy Bhandare")
    f.write("Roll no= 33")
#om9()


def om9():
    f= open("joy","a")
    f.write("Name= Joy Bhandare")
    f.write("Roll no= 33")
#om9()


def om9():
    f= open("joy","a")
    f.write("Name= ram ")
    f.write("Roll no= 3")
#om9()

def om9():
    f= open("omkar","r")
    f1=open("joy","w")
    for data in f:
        f1.write(data)
#om9()



#searching the element from list
def om9():
    def search (list,n):
        i=0
        while i<len(list):
            if list [i]==n:
                return True
            i=i+1
        return  False
    list=[1,2,3,4,5,6]
    n=8
    if search (list,n):
        print("Found")
    else:
        print("Not Found")
#om9()



#searching the element and it's position from list

#pos= -1
#def search (list,n):
    #i=0
    #while i<len(list):
        #if list [i]==n:
            #globals()['pos']= i
            #return True
        #i=i+1
    #return False
#list=[1,2,3,4,5,6]
#n=6
#if search (list,n):
    #print("Found at",pos+1)
#else:
   # print("Not Found")




#searching the element and it's position from list


def om9():

    pos= -1
    def search (list,n):
        l=0
        u=len(list)-1

        while l<=u:
            mid=(l+u)//2
            if list [mid]==n:
                globals()['pos']= mid
                return True
            else:
                if list[mid]<n:
                    l=mid;
                else:
                    u=mid;
        return  False
    list=[0,1,2,3,4,5,99,475,145]
    n=747
    if search (list,n):
        print("Found at",pos+1)
    else:
        print("Not Found")




def om9():
# swapping of value
    x=5
    y=6
    t=x
    x=y
    y=t
    print('x:',x)
    print('y:',y)





# bubble sort
def om9():
    def sort(nums):
        for i in range(len(nums)-1,0,-1):
            for j in range(i):
                if nums[j]>nums[j+1]:
                    t=nums[j]
                    nums[j]=nums[j+1]
                    nums[j+1]=t
    nums=[5,6,7,8,4,1]
    sort(nums)
    print(nums)




# selection sort
# easy method
def om9():
    def sort(nums):
        for i in range(5):
            minpos=i
            for j in range(i,6):
                if nums[j]<nums[minpos]:
                    minpos=j
            t = nums[i]
            nums[i] = nums[minpos]
            nums[minpos] = t
    nums=[5,6,7,8,4,1]
    sort(nums)
    print(nums)








# mysql
def om9():
    import mysql.connector

    mybd= mysql.connector.connect(host="localhost", user="root", passwd="omkar@0504")

    mycursor=mybd.cursor()
    mycursor.execute("shoe")
    for i in mycursor:
        print(i)

r="omkar"
print(r)





