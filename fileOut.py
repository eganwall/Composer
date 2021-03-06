# This will write a random string of notes
# in the key of C major, convert it to genes,
# and write it to a text file
import random

m = 0 # this is our population counter
cMajorKey = [60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81, 83, 84] # 2 octave C major
timeDict = {'eighth' : .5, 'quarter' : 1, 'half' : 2, 'whole' : 4}
maxBeats = 480.0 # we'll generate an excerpt that's 8 measures of 4 beats each

# now we'll loop through and generate a population
while(m < 20):
	
	m = m + 1 # increment our counter
	
	# this will tell us which file to write to
	fileName = "music" + str(m) + ".dna"
	outFile = file(fileName, "w+")

	currBeats = 0.0 # and this will keep track of how many beats we've currently written
	prevPitch = 0 # this will keep track of the previous pitch so we can resolve 7ths

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
			noteTime = int(timeDict['quarter'] * 10)
		elif rand > 0.6 and rand <=0.85:
			noteTime = int(timeDict['eighth'] * 10)
		elif rand > 0.85 and rand <= .95:
			noteTime = int(timeDict['half'] * 10)
		else:
			noteTime = int(timeDict['whole'] * 10)

		# now we'll check to see if the last pitch was a major 7th
		if prevPitch == "71":
			# if it is, we'll resolve it up to the root note
			pitch = "72"
		elif prevPitch == "83":
			pitch = "84"
		else:
			# if it's not, we'll give it a random pitch from our key list
			pitchNum = random.randrange(0, 15)
			pitch = str(cMajorKey[pitchNum])

		prevPitch = pitch
		noteTime = str(noteTime)
		# this checks to see if the piece is finished and makes 
		# sure we don't put too many beats in it
		if (currBeats + float(noteTime)) >= maxBeats:
			noteTime = str(int(maxBeats - currBeats))
			currBeats = maxBeats
			pitch = "60"

	
		# we have to make sure it writes the chromosome for the 
		# eighth note correctly
		if noteTime == "5":
			noteTime = "05"
		
		currBeats += float(noteTime)

		gene = pitch + noteTime

		outFile.write(gene + "|")
		print("Current time: %.2f    Current pitch: %s     File: %s" % (currBeats, pitch, fileName))

print("There we go, done!")