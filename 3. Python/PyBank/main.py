import csv
import os
os.system("clear")

file1 = "budget_data_1.csv"
file2 = "budget_data_2.csv"

def pybank(filepath):

	counter = 0
	total = 0
	revenues = []
	revChange = []
	
	# Opens csv file, skipping the header line
	with open(filepath, newline="", encoding="latin-1") as file:
		reader = csv.reader(file, delimiter = ",")
		next(reader)

		# Loop through rows of the data set
		for row in reader:
			row = int(row[1])
			counter += 1 			#number of rows/months
			total = total + row		#total revenue
			revenues.append(row)	#list of revenues
			
			# Creating list of changes in the revenue each month
			if counter > 0:
				change = (revenues[counter-1] - revenues[counter - 2])
				revChange.append(change)
			maxInc = max(revChange)
			maxDec = min(revChange)


	aveChange = sum(revChange)/counter

	# Output
	print("Financial Analysis of Revenue")
	print("-------------------------")
	print("Total: $" + str(total))
	print("Average Change: $" + str(aveChange))
	print("Greatest Increase: " + str(maxInc))
	print("Greatest Decrease: " + str(maxDec))

pybank(file1)
