
# Homework 4: Heroes of Pymoli

### Imports and Data


```python
import pandas as pd 
import numpy as np
import json
data = pd.read_json('purchase_data.json')
```

### Player Count


```python
# Player Count
def unique_players():
    labels = "Total Players"
    values = len(data['SN'].value_counts())
    
    df = pd.DataFrame({labels: values}, index=[0])
    return(df)

unique_players()
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
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>573</td>
    </tr>
  </tbody>
</table>
</div>



### Purchasing Analysis


```python
# Total Purchases
def purchasing_totals():
    values = [len(data['Item Name'].value_counts()),
                        np.mean(data['Price']),
                        data.shape[0],
                        np.sum(data['Price'])]
    labels = ["Number of Unique Items", "Total Purchases", "Average Price", "Total Revenue"]
    
    df = pd.DataFrame({'Number of Unique Items': len(data['Item Name'].value_counts()),
                       'Average Price':np.mean(data['Price']),
                       'Total Purchases': data.shape[0],
                       'Total Revenue': np.sum(data['Price'])}, index=[0])
    df = df[labels]
    df.iloc[:,2:] = df.iloc[:,2:].applymap('${:,.2f}'.format)
    return(df)

purchasing_totals()
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
      <th>Number of Unique Items</th>
      <th>Total Purchases</th>
      <th>Average Price</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>179</td>
      <td>780</td>
      <td>$2.93</td>
      <td>$2,286.33</td>
    </tr>
  </tbody>
</table>
</div>



### Gender Analysis


```python
# Gender Demographics
def gender_demo():
    labels = ['Count']
    counts = data['Gender'].value_counts()
    
    df = pd.DataFrame({'Count': counts})
    return(df)

gender_demo()
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
      <th>Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>633</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>136</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Purchasing Analysis (Gender)
def purchasing_gender():
    col = ['Purchase Count', 'Purchasing Total', 'Purchase Average', 'Normalized Total']
    m = data.loc[data['Gender'] == 'Male']
    f = data.loc[data['Gender'] == 'Female']
    o = data.loc[data['Gender'] == 'Other \/ Non-Disclosed']
    mp = m['Price']
    fp = f['Price']
    op = o['Price']

    mfo = [m, f, o]
    mfop = [mp, fp, op]

    demo = [len(i['SN'].value_counts()) for i in mfo]
    ave = [np.mean(i) for i in mfop]
    total = [np.sum(i) for i in mfop]
    norm = [total[i]/demo[i] for i in range(3)]

    df = pd.DataFrame({'Purchase Count': demo, 'Purchasing Total': total, 'Purchase Average':ave, 
                       'Normalized Total': norm})
    df = df[col]
    df.iloc[:,2:] = df.iloc[:,2:].applymap('${:,.2f}'.format)
    df.index = ['Male', 'Female', 'Other/ Non-Disclosed']
    return(df)

purchasing_gender()
```

    /Users/mahn/anaconda3/lib/python3.6/site-packages/ipykernel_launcher.py:17: RuntimeWarning: invalid value encountered in double_scalars



    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-13-40042b18cd76> in <module>()
         23     return(df)
         24 
    ---> 25 purchasing_gender().demo
    

    ~/anaconda3/lib/python3.6/site-packages/pandas/core/generic.py in __getattr__(self, name)
       3612             if name in self._info_axis:
       3613                 return self[name]
    -> 3614             return object.__getattribute__(self, name)
       3615 
       3616     def __setattr__(self, name, value):


    AttributeError: 'DataFrame' object has no attribute 'demo'


### Age Analysis


```python
def age():
    labels = ['Purchase Count', 'Average Price', 'Total Purchase Value', 'Normalized Total Price']
    bins = [0, 10, 15, 20, 25, 30, 35, 40, 45]
    bin_names = range(8)
    data['Age Cat'] = pd.cut(data['Age'], bins, labels = bin_names)
    
    purchases = list(data['Age Cat'].value_counts().sort_index())
    ave_price = list(data.groupby('Age Cat')['Price'].mean())
    total_price = list(data.groupby('Age Cat')['Price'].sum())
    norm_tp = [total_price[i]/ purchases[i] for i in range(8)]
    
    df = pd.DataFrame()
    df['Purchase Count'] = purchases
    df['Average Price']=ave_price
    df['Total Purchase Value']=total_price
    df['Normalized Total Price'] = norm_tp
    
    df.iloc[:,1:4] = df.iloc[:, 1:4].applymap('${:.2f}'.format)

    df.index = ['<10', '10-14', '15-19', '20-24', '25-29', '30-34', '34-39', '40+']
    return(df)

age()
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
      <th>Purchase Count</th>
      <th>Average Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Total Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>32</td>
      <td>$3.02</td>
      <td>$96.62</td>
      <td>$3.02</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>78</td>
      <td>$2.87</td>
      <td>$224.15</td>
      <td>$2.87</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>184</td>
      <td>$2.87</td>
      <td>$528.74</td>
      <td>$2.87</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>305</td>
      <td>$2.96</td>
      <td>$902.61</td>
      <td>$2.96</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>76</td>
      <td>$2.89</td>
      <td>$219.82</td>
      <td>$2.89</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>58</td>
      <td>$3.07</td>
      <td>$178.26</td>
      <td>$3.07</td>
    </tr>
    <tr>
      <th>34-39</th>
      <td>44</td>
      <td>$2.90</td>
      <td>$127.49</td>
      <td>$2.90</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>3</td>
      <td>$2.88</td>
      <td>$8.64</td>
      <td>$2.88</td>
    </tr>
  </tbody>
</table>
</div>



### Top Spending


```python
def top_spending():    
    col = ['SN', 'Purchase Count', 'Average Purchase Price', 'Total Purchase Price']
    df = pd.DataFrame(np.sum(data.groupby('SN')['Price'])).reset_index()
    df = df.sort_values('Price', ascending=False)

    SN = list(df.head()['SN'])
    counts = [data[data['SN'] == SN[i]].shape[0] for i in range(len(SN))]
    total = list(df.head().loc[:,'Price'])

    counts = np.array(counts)
    total = np.array(total)
    average = total/counts


    df = pd.DataFrame({'SN': SN, 'Purchase Count': counts, 'Total Purchase Value': total,
                       'Average Purchase Price': average})
    df = df[['SN', 'Purchase Count', 'Total Purchase Value', 'Average Purchase Price']]
    
    df.iloc[:,2:] = df.iloc[:, 2:].applymap('${:.2f}'.format)
    return(df)

top_spending()
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
      <th>SN</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
      <th>Average Purchase Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Undirrala66</td>
      <td>5</td>
      <td>$17.06</td>
      <td>$3.41</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Saedue76</td>
      <td>4</td>
      <td>$13.56</td>
      <td>$3.39</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Mindimnya67</td>
      <td>4</td>
      <td>$12.74</td>
      <td>$3.18</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Haellysu29</td>
      <td>3</td>
      <td>$12.73</td>
      <td>$4.24</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Eoda93</td>
      <td>3</td>
      <td>$11.58</td>
      <td>$3.86</td>
    </tr>
  </tbody>
</table>
</div>



### Popular Items


```python
def pop_items():
    # Returns DataFrame containing column headers:
    col = ['Item ID', 'Item Name', 'Purchase Count', 'Item Price', 'Total Purchase Value']

    # Calculating values for df
    series = data['Item ID'].value_counts().head()
    items = list(series.index)

    temp = data[data['Item ID'].isin(items)]
    counts = np.array(temp['Item ID'].value_counts())
    names = list(temp['Item Name'].value_counts().index)

    total = [np.sum(temp[temp['Item ID'] == items[i]]['Price']) for i in range(len(items))]
    price = [temp[temp['Item ID'] == items[i]].reset_index().loc[0,'Price'] for i in range(len(items))]

    # Formatting DataFrame
    df = pd.DataFrame({'Item ID':items, 'Item Name': names, 'Purchase Count': counts, 'Item Price':price,
                 'Total Purchase Value': total})
    df = df[col]
    df.iloc[:,3:] = df.iloc[:, 3:].applymap('${:.2f}'.format)
    
    return(df)

pop_items()
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
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>84</td>
      <td>Arcane Gem</td>
      <td>11</td>
      <td>$2.23</td>
      <td>$24.53</td>
    </tr>
    <tr>
      <th>1</th>
      <td>39</td>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>11</td>
      <td>$2.35</td>
      <td>$25.85</td>
    </tr>
    <tr>
      <th>2</th>
      <td>31</td>
      <td>Woeful Adamantite Claymore</td>
      <td>9</td>
      <td>$2.07</td>
      <td>$18.63</td>
    </tr>
    <tr>
      <th>3</th>
      <td>34</td>
      <td>Retribution Axe</td>
      <td>9</td>
      <td>$4.14</td>
      <td>$37.26</td>
    </tr>
    <tr>
      <th>4</th>
      <td>175</td>
      <td>Trickster</td>
      <td>9</td>
      <td>$1.24</td>
      <td>$11.16</td>
    </tr>
  </tbody>
</table>
</div>



### Profitable Items


```python
def prof_items():
    col = ['Item ID', 'Item Name', 'Purchase Count', 'Item Price', 'Total Purchase Value']

    df = pd.DataFrame(np.sum(data.groupby('Item ID')['Price'])).reset_index()
    df = df.sort_values('Price', ascending = False)

    items = list(df.head()['Item ID'])
    counts = [data[data['Item ID'] == items[i]].shape[0] for i in range(len(items))]

    temp = data[data['Item ID'].isin(items)]
    names = list(temp['Item Name'].value_counts().index)

    total = list(df.head().loc[:,'Price'])
    price = [temp[temp['Item ID'] == items[i]].reset_index().loc[0, 'Price'] for i in range(len(items))]

    df = pd.DataFrame({'Item ID': items, 'Item Name': names, 'Purchase Count':counts, 'Item Price':price,
                     'Total Purchase Value':total})
    df = df[col]
    df.iloc[:,3:] = df.iloc[:,3:].applymap('${:.2f}'.format)
    return(df)

prof_items()
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
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>34</td>
      <td>Retribution Axe</td>
      <td>9</td>
      <td>$4.14</td>
      <td>$37.26</td>
    </tr>
    <tr>
      <th>1</th>
      <td>115</td>
      <td>Splitter, Foe Of Subtlety</td>
      <td>7</td>
      <td>$4.25</td>
      <td>$29.75</td>
    </tr>
    <tr>
      <th>2</th>
      <td>32</td>
      <td>Spectral Diamond Doomblade</td>
      <td>6</td>
      <td>$4.95</td>
      <td>$29.70</td>
    </tr>
    <tr>
      <th>3</th>
      <td>103</td>
      <td>Singed Scalpel</td>
      <td>6</td>
      <td>$4.87</td>
      <td>$29.22</td>
    </tr>
    <tr>
      <th>4</th>
      <td>107</td>
      <td>Orenmir</td>
      <td>8</td>
      <td>$3.61</td>
      <td>$28.88</td>
    </tr>
  </tbody>
</table>
</div>


