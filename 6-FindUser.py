#!/usr/bin/python
print("Find user con code")
mydata = [
    ["Luciano", "1010"],
    ["Pablo", "1298"],
    ["Mario", "3097"]
]

username = input("Username to find: ")
pin = input("Code: ")
if [username, pin] in mydata:
    print ("User found")
else:
    print ("User not found")
