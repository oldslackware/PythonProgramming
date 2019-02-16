#!/usr/bin/python
print("Stampa liste []")
list1=[12,"Luciano",3.6,"Demuru",35]
list2=["Perfect",28]
print(list1)
print(list1[1])
print(list1[1:3])
print(list1[3: ])
print(list2 *2)
print(list1 + list2)
print("Stampa tuple ()")
tupla1=(12,"Luciano",3.6,"Demuru",35)
tupla2=("Perfect",28)
print(tupla1)
print(tupla1[1])
print(tupla1[1:3])
print(tupla1[3: ])
print(tupla2 *2)
print(tupla1 + tupla2)

print("Le liste possono essere modificate")
list1[2]="The Boss"
print(list1)

print("le tuple no")
tupla1[2]="The Boss"
print(tupla1)