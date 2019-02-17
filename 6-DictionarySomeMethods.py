#!/usr/bin/python
travelBestEurope={"Italy":"Florence","England":"Liverpool","Swisse":"Geneve","Norway":"Drammen","Belgie":"Bruges"}
print(travelBestEurope)
print("A better way to print")
print(str(travelBestEurope))
"print(travelBestEurope[1]) ERROR:->You can't access like array"
print("My favourite city in Norway is: "+travelBestEurope["Norway"])
"Add an element"
travelBestEurope["Sweden"]="Umea"
print("After an ADD")
print(travelBestEurope)
"Duplicates are not permitted"
travelBestEurope["Norway"]="Drammen"
print("Duplicates are not permitted")
print(travelBestEurope)
del travelBestEurope["Belgie"]
print("After Belgie deleted")
print(travelBestEurope)
print("Copy a dictionary")
travelBestEuropetmp=travelBestEurope.copy()
print(travelBestEuropetmp)
travelBestEuropetmp.clear()
print("After all items deleted")
print(travelBestEuropetmp)
print("Dict removed")
del travelBestEuropetmp
"print(travelBestEuropetmp) Error the dict doesn't exist"
print("We return at the original dict.")
print(travelBestEurope)
print("Dictionary has ",len(travelBestEurope)," elements")
print("We order it by items")
travelSorted=sorted(travelBestEurope.items())
print(travelSorted)
print("We order it by keys")
travelSorted=sorted(travelBestEurope.keys())
print(travelSorted)
print("We order it by values")
travelSorted=sorted(travelBestEurope.values())
print(travelSorted)
del travelSorted
print("Original dict")
print(travelBestEurope)
print("Reverse")
print(sorted(travelBestEurope.items(),reverse=True))
print("We come back at the original dic")
print(travelBestEurope)
print("Second dict with capital visited")
travelCapitalVisited={"Rome":"VISITED","London":"VISITED","Bern":"NO VISITED","Oslo":"VISITED"}
print(travelCapitalVisited)
print("Show me the Nation with Status Capital")
for (i,j),(i2,j2) in zip(travelBestEurope.items(),travelCapitalVisited.items()):
     print(i,j2)
print("Nested dictionaries")
"The number is the key and all inside {} is the value"
car={
     1:{"brand":"Renault","model":"Megane","price":"25000"},
     2:{"brand":"Fiat","model":"Cinquecento","price":"15000"}
}
print(car)
print("We try to add this dictionary(Note the color)")
car[3]={"brand":"Nissan","model":"Micra","price":"9000","color":"red"}
print(car[3])
print("The new dictionary after the add")
print(car)
print("WE Remove the color from key 3")
del car[3]["color"]
print(car)
print("Remove the dictionary Nissan")
del car[3]
print(car)
print("The iterator power")
for c_id, c_info in car.items():
     print("\nAuto ID:", c_id)
     for key in c_info:
          print(key + ":", c_info[key])




