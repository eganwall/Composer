# This will write a random string of notes
# in the key of C major, convert it to genes,
# and write it to a text file
import random

cMajorKey = [60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81, 83, 84] # 2 octave C major
timeDict = {'eighth' : .5, 'quarter' : 1, 'half' : 2, 'whole' : 4}
outFile = file("music3.in", "w+")

maxBeats = 320.0 # we'll generate an excerpt that's 8 measures of 4 beats each
currBeats = 0.0 # and this will keep track of how many beats we've currently written

# for now, the loop will go until the number of beats
# in the entire excerpt is reached. The loop will
# break when the condition has been satisfied
while currBeats < maxBeats: 

	# the time value for a given note will be weighted random:
	# there will be a 60% chance for a quarter note, a 25% chance
	# for an eighth note, a 10% chance for a half note and a 5%
	# chance for a whole note. I'm lazy right now and I'm just 
	# going to hardcode this shit. FUCK WHAT YA HERD
	
	rand = random.random()

	if rand <= 0.6:
		noteTime = str(int(timeDict['quarter'] * 10))
	elif rand > 0.6 and rand <=0.85:
		noteTime = "0" + str(int(timeDict['eighth'] * 10))
	elif rand > 0.85 and rand <= .95:
		noteTime = str(int(timeDict['half'] * 10))
	else:
		noteTime = str(int(timeDict['whole'] * 10))

	# now we'll select a random pitch from our key list
	pitchNum = random.randrange(0, 15)
	pitch = str(cMajorKey[pitchNum])
	
	# this checks to see if the piece is finished and makes 
	# sure we don't put too many beats in it
	if (currBeats + float(noteTime)) > maxBeats:
	
		noteTime = str(int(maxBeats - currBeats))
		pitch = "60" # we'll also make the last note resolve
		
	currBeats += float(noteTime)
	
	gene = pitch + noteTime
	
	outFile.write(gene + "|")

print("There we go, done!")