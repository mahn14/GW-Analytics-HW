import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

# Preprocessing Data

data = pd.read_csv("StarterBook.csv", sep = ",", encoding = "latin-1")
data.name = "All Data"

data = data.loc[:,['id', 'name', 'blurb', 'state', 'country',
       'currency', 'deadline', 'launched_at', 'staff_pick', 'backers_count',
       'spotlight', 'Category and Sub-Category', 'Percent Funded',
       'Average Donation', 'Category', 'Sub-category',
       'Date Created Conversion', 'Date Ended Creation', 'Year', 'convert',
       'goal.1', 'pledge']]

data.columns = ['id', 'name', 'blurb', 'state', 'country',
       'currency', 'deadline', 'launched_at', 'staff_pick', 'backers_count',
       'spotlight', 'Category and Sub-Category', 'Percent Funded',
       'Average Donation', 'Category', 'Sub-category',
       'Date Created Conversion', 'Date Ended Creation', 'Year', 'convert',
       'goal', 'pledge']

us = data[data.loc[:,"currency"] == "USD"]
us.name = "USD Data"

data_sample = data[data.loc[:,"state"] != "live"]
success = data_sample[data_sample.loc[:, "state"] == "successful"]
fail = data_sample[data_sample.loc[:, "state"] != "successful"]

fail = fail[fail["backers_count"] != 0]


# Exploring Backers and Pledges ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# calculates averages to be displayed in Terminal
def show_means(df, *args):
	print("Means from " + df.name[1])
	for i in args:
		print(str(i) + ": " + str(np.mean(df[i])))

# calculates average of goals and pledges made in USD only
def show_means_usd():
	show_means(us, "goal", "pledge")

# Average Pledge for success vs fail
def pledge_success_fail():

	print("Average Pledge")
	print(str(np.sum(success.pledge)/np.sum(success.backers_count)))
	print(str(np.sum(fail.pledge)/np.sum(fail.backers_count)))

# Mean and Median of Backers Count
def backers_summary():
	print("Mean: Backers Count")
	print(np.mean(success.backers_count))
	print(np.mean(fail.backers_count))

	print("Median: Backers Count")
	print(np.median(success.backers_count))
	print(np.median(fail.backers_count))

# Distribution of Backers Count for successful and failing 
def backers_distr():

	x = success.backers_count
	y = fail.backers_count
	bins = np.linspace(0, 250, 50)
	plt.hist(x, bins, label = "success")
	plt.hist(y, bins, label = "fail")
	plt.legend()
	plt.title("Backers_Count")
	plt.show()

def pledge_goal_difference():
	x = success.pledge - success.goal
	y = fail.pledge - fail.goal

	print(np.mean(x))
	print(np.mean(y))


# Exploring Staff Picks nad Success ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
yes = data_sample[data.loc[:,"staff_pick"] == True] #556
no = data_sample[data.loc[:,"staff_pick"] == False] #3508

yes_success = yes[yes.loc[:,"state"] == "successful"] #486
no_success = no[no.loc[:,"state"] == "successful"] #1699

print(486/556)
print(1699/3508)






