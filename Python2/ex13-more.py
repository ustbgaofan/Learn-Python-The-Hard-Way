# -*- coding: utf-8 -*-

# ex13: Parameters, Unpacking, Variables
# Write a script that has more arguments

from sys import argv

script, name, age, height, weight = argv

print "The script is called:", script
print "Your name is:", name
print "Your age is:", age
print "Your height is:", height
print "Your weight is:", weight
