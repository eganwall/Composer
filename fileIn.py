from midiutil.MidiFile import MIDIFile

input = open('music3.in', 'r').read()
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

	print("Adding pitch: %d, duration: %.1f to the file" % (pitch, duration))
	myMIDI.addNote(track, channel, pitch, time, duration, volume)

	time += duration

print("The piece is %.1f beats long" % time) # make sure the length is correct

# and then we write it to our output MIDI file	
outFile = open("output.mid", 'wb')
myMIDI.writeFile(outFile)

# bitches ain't shit
outFile.close()