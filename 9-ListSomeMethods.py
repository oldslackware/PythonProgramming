#|/usr/bin/python
import math
mylist=["Slackware","Debian","Gentoo","Centos","Ubuntu"]
print (*mylist, sep="\n")
mylist.reverse()
print("\nReverse lis\nt")
print(*mylist, sep="\n")
"My list is the list reversed"
print("\nMy distro:",mylist[4])
print("\nCheck if there is Centos")
if("Centos" in mylist):
    print("There is Centos")
else:
    print("There is Not Centos")

"list of list"
print("\nThe best language is:")
nestedlist=["Java Python Perl", [9,3.6,5.6]]
print(nestedlist[0][5:11])
print("Version:")
print(nestedlist[1][1])
print("The language more used is ", nestedlist[0][:-12]," version:", nestedlist[1][:-2])
print("\nFactorial of some numbers\n")
"factorial of [6,8,10,12]"
listfactorial=[math.factorial(x) for x in range(13) if x>5 and x%2==0]
print(listfactorial)
print("Min:",min(listfactorial))
print("max",max(listfactorial))
print("Sum of all factorial number ",sum(listfactorial))
