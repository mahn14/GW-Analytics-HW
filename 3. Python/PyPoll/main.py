import csv
import os
os.system("clear")

file1 = 'election_data_1.csv'
file2 = 'election_data_2.csv'

# analysis as assigned in the homework instructions for election data
def pypoll(filepath):
	'''
	params:
		@filepath: path of csv file to be worked with
	returns:
		@print:
			Total Votes
			Unique Candidate Name: # of votes (% of total votes)
			Winner: Candidate Name
	'''

	# declaring variables
	counter = 0
	nameList = []
	voteList = []
	percentList = []
	name = "" 

	# reading through csv for (1)row count, (2)unique names, (3)corresponding votes
	with open(filepath, newline = "", encoding = 'latin-1') as file:
		reader = csv.reader(file, delimiter = ",")
		next(reader) #skips the header

		for row in reader:
			# (1)
			counter += 1

			# (2)
			name = row[2]
			if name in nameList:
				pass
			else:
				nameList.append(name)
				voteList.append(0)

			# (3)
			index = nameList.index(name)
			voteList[index] = voteList[index] + 1

	# calculating percent of votes per unique candidate
	for i in voteList:
		percentList.append(str(round(i/counter * 100, 2)) + "%")
	# calculating winner
	winner = nameList[voteList.index(max(voteList))]

	# @print
	print("Total Votes: " + str(counter))
	for i in nameList:
		print(i + ": " + str(voteList[nameList.index(i)]) + " (" +
		 str(percentList[nameList.index(i)]) + ")")
	print("Winner: " + winner)


# testing output
pypoll(file1)
print(" " )
pypoll(file2)


