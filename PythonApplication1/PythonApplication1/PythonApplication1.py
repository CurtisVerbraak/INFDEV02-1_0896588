import sys
for x in range(0,5,1):
	for y in range(1,5-x,1):

		sys.stdout.write(' ')

	for y in range(1,(2*x),1):

		sys.stdout.write('*')

	sys.stdout.write('\n')