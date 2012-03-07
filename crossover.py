'''''''''''''''''''''''''''''''''''''''''''''

	crossover.py
	
	This module will be responsible for 
	creating generation x by combining the 
	DNA of two members of generation x-1.

'''''''''''''''''''''''''''''''''''''''''''''

# this is going to help us choose our crossover point
import random

# first we'll bring in the two parents of the new generation
parent1 = open('parent1.dna', 'r').read()
parent2 = open('parent2.dna', 'r').read()

# go ahead and initialize our output DNA file
outFile = file('newGen.dna', 'w+')

# initialize our duration counter
totalDuration = 0

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
	maxCrossover = len(parent1) - 2 # we subtract 2 to ensure that at least 2 genes will always be passed from each parent
else:
	maxCrossover = len(parent2) - 2
	
# the crossover point will be a random point inside the bounds 
# of the DNA of the shorter parent
crossoverPoint = random.randrange(2, maxCrossover)

# random debugging shit
print parent1
print parent2
print len(parent1)
print len(parent2)
print("The crossover point is %d." % crossoverPoint)

# now we can go ahead and start the real work

newGen = list()
newGen.extend(parent1[0:crossoverPoint])
print("After parent 1:")
print newGen

newGen.extend(parent2[crossoverPoint:len(parent2)])
print("After parent 2:")
print newGen

# we need to add up the total duration of the crossed-over piece
for gene in newGen:
	totalDuration += int(gene[2:3]) # this will get the 3rd and 4th chromosomes and cast to an int
	
print("The total duration of the piece is: %d." % totalDuration)	

# now we write our Adam into our new DNA file to start the new generation
for gene in newGen:
	outFile.write(gene + "|")