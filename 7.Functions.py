#!/usr/bin/python

def hola():
    "A function without args"
    print("Hola in Python's function")

def holaFromDev(name,msg):
    "A function with 2 args"
    print("Hola from "+name+".\nThis is for you:"+msg)

def holafromLuciano(name, msg = "I can do all!"):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Msg ", msg)
   return

def holafromCrew(*names):
    "Arbitrary values"
    for n in names:
     print("Hello from "+n+ "\n")


def isoven(num):
    if(num%2 == 0):
        print(str(num)+ " is even")
    else:
        print(str(num)+" is odd")

def changeEuroDollar(num):
    "Change eruo dollars"
    if num >0:
        return num*1.13
    else:
        return 0

def sum(num):
    "Sum function"
    sum=0
    i=1
    while(i<num):
        sum=sum+i
        i=i+1
    return(sum)


def functionList(list):
    "Change all value in the list"
    list=[1,2,3,4]
    return list


print("Before the function")
"Print the documentation"
print(hola.__doc__)
hola()
print(holaFromDev.__doc__)
holaFromDev("Luciano","Never give up")
print(holafromCrew.__doc__)
holafromLuciano("Luciano")
print()
holafromCrew("Mike","Steve","Luciano","Jim")
isoven(512)
money=changeEuroDollar(10)
print("I have "+str(money)+ " dollars")
values=1000
print('The sum of ' + str(values) + " values is " + str(sum(values)))
list=[100,200,300,400]
print ("List value before the function's call", list)
list=functionList(list)
print("List's value after the function:", list)