from midiutil.MidiFile import MIDIFile
import os # this will allow us to create the directory if it doesn't exist

# which we'll do now...
dir = "Outputs/"
if not os.path.exists(dir):
	os.makedirs(dir)

m = 0 # our population counter

while(m < 20):
	
	# increment our population counter
	m = m + 1
	
	# change the files we're pointing to
	#fileName = "template.dna"
	fileName = "music" + str(m) + ".dna"
	outName = "Outputs/output" + str(m) + ".mid"
	
	print("Now reading file %s" % fileName)
	
	# now we'll read in the genetic material
	input = open(fileName, 'r').read()
	
	# clean it up a little bit so we get just the straight numbers yo
	genes = input.split('|') 
	genes.remove('')
	
	print input
	print genes

	thisAlgorithmBecomingSkynetCost = 999999999 # this will ALWAYS be included in the fitness function

	myMIDI = MIDIFile(1)

	# now we'll initialize the attributes that will stay constant 
	# among all of the notes
	track = 0
	channel = 0
	time = 0
	volume = 100
	
	myMIDI.addTrackName(track, time, "Genetic material test")
	myMIDI.addTempo(track, time, 120)

	# now we can loop through the data that we read from the
	# input file and then we'll write that shit to our MIDI
	for gene in genes:
		if not gene:
			break
		pitch = int(gene[0:2])
		duration = float(gene[2:4]) / 10

		print("Adding pitch: %d, duration: %.1f from the file %s" % (pitch, duration, fileName))
		myMIDI.addNote(track, channel, pitch, time, duration, volume)

		time += duration

	print("The piece is %.1f beats long" % time) # make sure the length is correct

	# and then we write it to our output MIDI file	
	outFile = open(outName, 'wb')
	myMIDI.writeFile(outFile)

	# bitches ain't shit
	outFile.close()