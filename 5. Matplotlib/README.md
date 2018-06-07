
# Pyber
Michael Ahn  
GWU: Data Analytics Certification Homework 5

#### Initial Setup


```python
# Dependencies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_city = 'city_data.csv'
file_ride = 'ride_data.csv'
```


```python
# Reading in CSVs
city = pd.read_csv(file_city)
city = city.drop([84]) #contains a repeat row
city.columns = ['City', 'Driver Count', 'Type']

ride = pd.read_csv(file_ride)
ride.columns = ['City', 'Date', 'Fare', 'Ride ID']
```

## Preparing DataFrames for Plotting

#### Per City DataFrames


```python
# Average Fare
fare = pd.DataFrame(ride.groupby('City')['Fare'].mean()).reset_index()
fare.columns = ['City', 'Average Fare']

# Total Fare
city_fare = pd.DataFrame(ride.groupby('City')['Fare'].sum())
city_fare = city_fare.reset_index()
city_fare.columns = ['City', 'Total Fare']

# Total Rides
count = pd.DataFrame(ride['City'].value_counts()).reset_index()
count.columns = ['City', 'Ride Count']
```

#### Combine DataFrames


```python
# Consolidate Subsetted DataFrames
df = city.merge(fare, how='outer')
df = df.merge(count, how='outer')
df = df.merge(city_fare)

# Format Final DataFrame
df = df.sort_values('Type')
df = df[['City', 'Type', 'Driver Count','Ride Count', 'Average Fare','Total Fare']]
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City</th>
      <th>Type</th>
      <th>Driver Count</th>
      <th>Ride Count</th>
      <th>Average Fare</th>
      <th>Total Fare</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>124</th>
      <td>West Kevintown</td>
      <td>Rural</td>
      <td>5</td>
      <td>7</td>
      <td>21.528571</td>
      <td>150.70</td>
    </tr>
    <tr>
      <th>107</th>
      <td>South Elizabethmouth</td>
      <td>Rural</td>
      <td>3</td>
      <td>5</td>
      <td>28.698000</td>
      <td>143.49</td>
    </tr>
    <tr>
      <th>108</th>
      <td>East Troybury</td>
      <td>Rural</td>
      <td>3</td>
      <td>7</td>
      <td>33.244286</td>
      <td>232.71</td>
    </tr>
    <tr>
      <th>109</th>
      <td>Kinghaven</td>
      <td>Rural</td>
      <td>3</td>
      <td>6</td>
      <td>34.980000</td>
      <td>209.88</td>
    </tr>
    <tr>
      <th>110</th>
      <td>New Johnbury</td>
      <td>Rural</td>
      <td>6</td>
      <td>4</td>
      <td>35.042500</td>
      <td>140.17</td>
    </tr>
  </tbody>
</table>
</div>



#### Per City Type DataFrames


```python
rural = df[df['Type'] == 'Rural']
urban = df[df['Type'] == 'Urban']
sub = df[df['Type'] == 'Suburban']
```

## Plotting

#### Bubble Plot


```python
# Plot Setup
types = [rural, urban, sub]
colors = ['yellow', 'orange', 'teal' ]
x = 0

# Plotting by City Type
for i in types:
    plt.scatter(x = i['Ride Count'], y = i['Average Fare'],
               edgecolor = 'black', color = colors[x],
               s = i['Driver Count']*2)
    x+=1

# Formatting
plt.title('Pyber Ride Sharing Data (2016)')
plt.xlabel('Total Number of Rides (per City)')
plt.ylabel('Average Fare ($)')

legend = plt.legend(title='City Type', 
                    labels = ['rural', 'urban', 'suburban'])
legend.legendHandles[0]._sizes = [20]
legend.legendHandles[1]._sizes = [20]
legend.legendHandles[2]._sizes = [20]

plt.text(38, 40, 'Note: \nCircle size correlates with count per city')

plt.show()
```


![png](output_13_0.png)


#### Pie Charts


```python
# Plot Setup
pie_titles = ['Total Fare', 'Driver Count', 'Ride Count']
X = [df.groupby('Type')[i].sum() for i in pie_titles]

f = plt.figure(figsize=(10,3))
pos = 131
counter = 0

# Plotting by Statistic
for x in X:
    ax = f.add_subplot(pos + counter)
    plt.pie(x,autopct="%1.1f%%")
    plt.title(pie_titles[counter])
    counter += 1

# Formatting
f.suptitle('Comparison of City Types (%)')
plt.subplots_adjust(top=0.8)
ax.legend(labels=X[0].index, loc='lower right')
plt.show()
```


![png](output_15_0.png)

