'''
	This module will evaluate the 
	fitnesses of a population of organisms
	in order to optimize them to evolve into
	"Twinkle, Twinkle Little Star." Yep, 
	it's just as badass as it sounds.
'''

# our population counter
m = 0

# our target length (we'll make it a magic constant, rather than a magic number
TARGET_LENGTH = 42 # this is how many notes are in "Twinkle, Twinkle, Little Star

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
