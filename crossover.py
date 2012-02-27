'''''''''''''''''''''''''''''''''''''''''''''

	crossover.py
	
	This module will be responsible for 
	creating generation x by combining the 
	DNA of two members of generation x-1.
	It will also handle mutation of the 
	new generation.

'''''''''''''''''''''''''''''''''''''''''''''

# this is going to help us choose our crossover point
import random

# first we'll bring in the two parents of the new generation
parent1 = open('parent1.in', 'r').read()
parent2 = open('parent2.in', 'r').read()

# clean them up a little bit so we can use them as lists
parent1 = parent1.split('|')
parent2 = parent2.split('|')

# strip out the last element so the lengths are accurate
parent1.remove('')
parent2.remove('')

# now we have to determine the parameter for the crossover
# point. the latest crossover gene in the DNA will be the 
# second-to-last one.
if(len(parent1) < len(parent2)):
	maxCrossover = len(parent1) - 1
else:
	maxCrossover = len(parent2)
	
# the crossover point will be a random point inside the bounds 
# of the DNA of the shorter parent
crossoverPoint = random.randrange(1,maxCrossover)

print parent1
print parent2
print len(parent1)
print len(parent2)
print("The crossover point is %d." % crossoverPoint)