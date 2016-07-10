#ch 11 Importing Modules

import math

print math.sqrt(16)

###
from math import sqrt

print sqrt(16)

###
from math import sqrt, exp

print sqrt(16)
print exp(2)

###

#saved module
#stored in Lib/idlelib (see help('modules'))

# Import our module
import smallmathsmodule

# multiplyBy5 function
print smallmathsmodule.multiplyBy5(3)

# add5 function
print smallmathsmodule.add5(9)

# randomAdd function
print smallmathsmodule.randomAdd(8)



