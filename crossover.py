# first we'll bring in the two parents of the new generation
parent1 = open('parent1.in', 'r').read()
parent2 = open('parent2.in', 'r').read()

# clean them up a little bit so we can use them as lists
parent1 = parent1.split('|')
parent2 = parent2.split('|')

# strip out the last element so the lengths are accurate
parent1.remove('')
parent2.remove('')

print parent1
print parent2
print len(parent1)
print len(parent2)