#!/usr/bin/python
import FirstModules

print("I call the modules created to know my os")
tmp=FirstModules.myoperatingsystem()
print("My operating system is "+tmp)
print("\nAll methods of platform")
FirstModules.platformmethod()
print("Those infos are relative on the date:")
FirstModules.todaydate()
print("Number lucky: ", FirstModules.luckynumber())