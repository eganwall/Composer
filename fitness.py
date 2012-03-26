'''
	This module will evaluate the 
	fitnesses of a population of organisms
	in order to optimize them to evolve into
	"Twinkle, Twinkle Little Star." Yep, 
	it's just as badass as it sounds.
'''
import random

# our population counter
m = 0

# our target length (we'll make it a magic constant, rather than a magic number
TARGET_LENGTH = 42 # this is how many notes are in "Twinkle, Twinkle, Little Star

# this is our target pitch total
TARGET_TOTAL = 2710 # confirmed multiple times

# our list of fitnesses
fitnesses = list()

# here's the loop where we read in all of the organisms and evaluate them
while(m < 20):
	
	# first we'll initialize our fitness to 0 for this organism
	fitnesses.append(0)
	
	# then we increment our counter
	m = m + 1
	
	# our filename
	fileName = 'music' + str(m) + '.dna'
	
	# now we'll read in the genetic material
	input = open(fileName, 'r').read()
	
	# do all the basic cleanup shit, you know homey
	genes = input.split('|') 
	genes.remove('')
	
	''' So now that we have a straight list of numbers, we can start 
	tallying up all the fitness stuff'''
	
	# first, we'll assign a few fitness points based on 
	# the number of notes in the organism vs. the number in the goal
	if(len(genes) != TARGET_LENGTH):
		fitnesses[m - 1] += abs(len(genes) - TARGET_LENGTH)
	print("Length of piece %d is %d, fitness is %d." % (m, len(genes), fitnesses[m - 1]))

	# our second step is to tally up the total sum of the 
	# pitches in the piece and compare it against the target
	totalPitches = 0
	
	for index, gene in enumerate(genes):
		currGene = genes[index]
		# increment our counter by the current note's pitch value
		totalPitches += int(currGene[0:2])
	
	if(totalPitches != TARGET_TOTAL):
		fitnesses[m - 1] += abs(totalPitches - TARGET_TOTAL)
	print("The pitch total of piece %d is %d, fitness is %d." % (m, totalPitches, fitnesses[m - 1]))
	
	''' INSERT MORE FITNESS CALCULATIONS HERE WHEN YOU THINK OF THEM '''
	
# now that we've analyzed the fitnesses of our population, we can
# choose two pairings for our tournament selection
finalistPieces = list()
finalistFits = list()
i = 0

while(i < 4):
	i += 1
	finalist = random.randrange(0, len(fitnesses))
	
	# we'll add the fitness and number of our finalist piece to the arrays
	finalistFits.append(fitnesses[finalist])
	finalistPieces.append(finalist)
	
print("The four finalists are:")
print finalistPieces
print finalistFits

# select the two winners
if(finalistFits[0] <= finalistFits[1]):
	finalist1Fit = finalistFits[0]
	finalist1 = finalistPieces[0]
else:
	finalist1Fit = finalistFits[1]
	finalist1 = finalistPieces[1]
if(finalistFits[2] <= finalistFits[3]):
	finalist2Fit = finalistFits[2]
	finalist2 = finalistPieces[2]
else:
	finalist2Fit = finalistFits[3]
	finalist2 = finalistPieces[3]

print("Parent 1 is piece number %d, with fitness %d." % (finalist1, finalist1Fit))
print("Parent 2 is piece number %d, with fitness %d." % (finalist2, finalist2Fit))