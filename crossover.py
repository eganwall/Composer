'''''''''''''''''''''''''''''''''''''''''''''

	crossover.py
	
	This module will be responsible for 
	creating generation x by combining the 
	DNA of two members of generation x-1.

'''''''''''''''''''''''''''''''''''''''''''''

# this is going to help us choose our crossover point
import random

# our C major key for use in our mutation function
cMajorKey = [60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81, 83, 84]

# first we'll pass it the two parents
p1 = raw_input("Parent 1: ")
p2 = raw_input("Parent 2: ")

# this is our target length for the piece
LENGTH = 48.0

# we'll bring in the two parents of the new generation
parent1 = open('music' + p1 + '.dna', 'r').read()
parent2 = open('music' + p2 + '.dna', 'r').read()

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

# random debugging shit
print parent1
print parent2
print len(parent1)
print len(parent2)

# initialize our population counter
m = 0

while(m < 20):

	m = m + 1
	
	# initialize our duration counter
	totalDuration = 0.0
	
	#initialize our output file
	outFile = file('music' + str(m) + '.dna', 'w+')
	
	# the crossover point will be a random point inside the bounds 
	# of the DNA of the shorter parent
	crossoverPoint = random.randrange(2, maxCrossover)
	
	print("The crossover point for piece %d is %d." % (m, crossoverPoint))

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
		totalDuration += float(gene[2:4]) # this will get the 3rd and 4th chromosomes and cast to an int
	
	totalDuration = totalDuration / 10
	print("The total duration of piece %d is %.1f before cleanup." % (m, totalDuration))

	noteDurations = list()
	notePitches = list()
	
	# now we loop through and populate our lists
	for index, gene in enumerate(newGen):
		currGene = newGen[index]
			
		notePitches.append(currGene[0:2]) # this will copy the pitch value into our first list
		
		# this little block copies our time value into the second list
		if currGene[2:4] == "05":
			noteDurations.append(5)
		else:
			noteDurations.append(int(currGene[2:4]))
		print(currGene[2:4])
	print noteDurations
	print notePitches
	
	''' Here we'll add a small mutation function. The mutation rate
	will be experimented with, but for now we'll simply make it alter 
	a single pitch '''
	mutationRoll = random.random()
	
	if mutationRoll <= .5: # lol
		# and so we find a random index
		rand = random.randrange(0, len(notePitches))
		
		# debugging code
		x = notePitches[rand]
		
		# here we actually swap the index for a new pitch
		notePitches[rand] = cMajorKey[random.randrange(0, len(cMajorKey))]
		
		print("******* Note at index %d changed from %s to %s *******" % (rand, x, notePitches[rand]))
	else:
		print("No mutation occurred.")
	
	if noteDurations is not None: # lol
		'''
		Here is where we're going to assess how far off the mark
		our piece is in terms of timing. Once we know how much 
		editing we have to do, we'll loop through our time
		list and add/subtract an eighth note from a random
		index in the list.
		'''
		# this block determines whether we're going to add
		# or subtract time from the piece
		if(totalDuration < LENGTH):
			direction = 1
		elif(totalDuration > LENGTH):
			direction = -1
			
		# we'll loop through until the piece is the correct length
		while totalDuration != LENGTH:
			index = random.randrange(0, len(noteDurations)) # this is the note we'll modify
			
			# if it's already a whole note, we don't want to add anything
			if(noteDurations[index] == 40 and direction == 1):
				continue
			# conversely, we can't subtract an eighth note from an eighth note
			if(noteDurations[index] == 5 and direction == -1):
				continue
		
			noteDurations[index] += direction * 5 # this will add or subtract an eighth note from the selected note
			totalDuration += direction * .5 # and this allows us to keep track of it
		
			print("The note in index %d has been modified." % index)
			print("The piece is now %.1f beats long." % totalDuration)
		
		print noteDurations

		# the final step is to splice our arrays together to make the genetic material
		for index in range(0, len(noteDurations)):
			gene = str(notePitches[index])
		
			if(noteDurations[index] == 5):
				gene += "05"
			else:
				gene += str(noteDurations[index])
		
			newGen[index] = gene
		print newGen

	# now we write our Adam into our new DNA file to start the new generation
	for gene in newGen:
		outFile.write(gene + "|")
		print("Writing gene " + gene + " into piece " + str(m))
		
print("All done!")