'''
#standard library
import math
print("the value of sqrt is",math.sqrt(49))

#type of import
import math as m
print(m.pi)

#from
from math import pi
print (pi)

#all
from math import *
print("the value is",sqrt(81))

'''
#user define Modules
import Modules
print(Modules.add(4,9))


import Modules as m
print(m.add(45,12))


from Modules import add
print(add(78,45))

from Modules import *
print(add(45,78))
greeting("hiiii")











