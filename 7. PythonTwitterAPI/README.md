
# NewsMood  
This assignment focuses on parsing through Tweets from large news organizations and using Vader to analyze individuals sentiments

### Setup


```python
# Dependencies
import tweepy
import numpy as np
import pandas as pd
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

# Import and Initialize Sentiment Analyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# Dependencies
import tweepy

# Twitter API Keys
import sys
sys.path.append('/Users/mahn/Desktop/GW/API')
from keys import (twitter_consumer_key, 
                    twitter_consumer_secret, 
                    twitter_access_token, 
                    twitter_access_secret)

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
auth.set_access_token(twitter_access_token, twitter_access_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
```

### Gathering Data

1. Loop through each target_user 
2. Collect sentiment scores for 100 tweets per user
3. Append each dataframe to a list  


```python
# Separate Twitter handles from actual names
target_users = ['@bbcthesocial', '@CBSNews', '@CNN', '@FoxNews', '@nytimes']
news_channels = ['BBC', 'CBS', 'CNN', 'Fox', 'NYTimes']
```


```python
# Initialize list of dataframes
df_list = []

# 1. Loop through each target_user
for target_user in target_users:  
    counter = 1 
    sentiments = []
    oldest_tweet = None 
    
# 2. Loop through 5 pages of 20 tweets to collect sentiment scores
    for x in range(5):
        public_tweets = api.user_timeline(target_user, max_id = oldest_tweet)

        # Analyzing sentiment scores
        for tweet in public_tweets:
            results = analyzer.polarity_scores(tweet["text"])
            compound = results["compound"]
            pos = results["pos"]
            neu = results["neu"]
            neg = results["neg"]
            tweets_ago = counter

            oldest_tweet = tweet['id'] - 1

            sentiments.append({"Date": tweet["created_at"], 
                               "Compound": compound,
                               "Positive": pos,
                               "Negative": neu,
                               "Neutral": neg,
                               "Tweets Ago": counter}) 
            counter += 1

# 3. Create DataFrame and append each to df_list
    sentiments_pd = pd.DataFrame.from_dict(sentiments)
    df_list.append(sentiments_pd)
```


```python
# Create column containing News Source
x = 0
for i in news_channels:
    df_list[x]['News Source'] = i
    x += 1

# Use df_list to create total DataFrame
df_list_concat = [df_list[i] for i in range(len(df_list))]
df = pd.concat(df_list_concat)

df.to_csv('News_Mood_04102018')
```

### Visualizing

1. Scatter plot of ordered, compound sentiment scores  
2. Bar plot of mean, compound sentiment score  


```python
# Setup
col = ['skyblue', 'green', 'orange', 'blue', 'yellow']
f = plt.figure(figsize=(10,5))
ax = f.add_subplot(111)

# Plotting Compound Scores by News Source
for i in range(len(df_list)):
    ax.scatter(df_list[i]['Tweets Ago'], df_list[i]['Compound'],
               color = col[i],
               edgecolor='black',
               alpha= 0.9,
               s=100)

# Formatting Plot
plt.title('Sentiment Analysis of Media Tweets (04/10/2018)')
plt.xlabel('Tweets Ago')
plt.ylabel('Tweet Polarity')
plt.yticks([-1, -0.5, 0, 0.5, 1])

plt.legend(labels = news_channels,
          bbox_to_anchor=(1, 1),
          title='Media Sources',
          frameon=False)

plt.savefig('100Sentiments04102018.png')
plt.show()
```


![png](output_10_0.png)



```python
# Mean Compound Scores
aggregate = [np.mean(df_list[i]['Compound']) for i in range(len(df_list))]
aggregate = [round(aggregate[i], 3) for i in range(len(aggregate))]

# In-Plot Label
agg_value = [str(aggregate[i]) if aggregate[i]<0 else "+"+str(aggregate[i]) 
             for i in range(len(aggregate))]

y_pos = [aggregate[i] - 0.015 if aggregate[i]<=0 else aggregate[i] + 0.002
         for i in range(len(aggregate))]
```


```python
# Setup
plt.figure(figsize=(10,5))

# Plotting Mean Compound Scores
ax = sns.barplot(news_channels, aggregate)
ax.set(title='Overall Twitter Sentiment (04/10/2018)',
        xlabel='News Channel', ylabel='Mean Polarity Score',
        yticks=[-0.2, -0.1, 0, 0.1])

# Labels
for i, v in enumerate(aggregate):
    ax.text(i, y_pos[i], 
            agg_value[i], 
            color='black')
    
plt.savefig('OverallSentiment04102018.png')
plt.show()
```


![png](output_12_0.png)


### Analysis

An initial note is of Fox and BBCs central tendency towards more positive tweets that CBS, CNN, and NYTimes. But can we examine this further?


```python
# Import libraries and set plt style to default
import matplotlib.lines as mlines
plt.rcParams.update(plt.rcParamsDefault)
```


```python
# Extract distribution summary of compound sentiment scores
compound_all = df['Compound'].describe()[3:]
compound_each = [df_list[i]['Compound'].describe()[3:] for i in range(len(df_list))]
index = range(len(compound_all))

# Put summaries into DataFrame
ex = {'Total':compound_all}
for i in range(len(compound_each)):
    ex[news_channels[i]] = compound_each[i]
pd.DataFrame(ex)
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
      <th>BBC</th>
      <th>CBS</th>
      <th>CNN</th>
      <th>Fox</th>
      <th>NYTimes</th>
      <th>Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>min</th>
      <td>-0.703400</td>
      <td>-0.8591</td>
      <td>-0.822500</td>
      <td>-0.8658</td>
      <td>-0.796400</td>
      <td>-0.8658</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>0.000000</td>
      <td>-0.2732</td>
      <td>-0.340000</td>
      <td>-0.2263</td>
      <td>-0.301550</td>
      <td>-0.2263</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.000000</td>
      <td>0.0000</td>
      <td>0.000000</td>
      <td>0.0000</td>
      <td>0.000000</td>
      <td>0.0000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.164625</td>
      <td>0.1531</td>
      <td>0.109025</td>
      <td>0.3403</td>
      <td>0.146575</td>
      <td>0.1779</td>
    </tr>
    <tr>
      <th>max</th>
      <td>0.888500</td>
      <td>0.6908</td>
      <td>0.822500</td>
      <td>0.8360</td>
      <td>0.718400</td>
      <td>0.8885</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Plotting individual summaries compared to total summary
f = plt.figure()
ax = f.add_subplot(111)

for each in compound_each:
    plt.scatter(index, each)
plt.legend(news_channels, bbox_to_anchor=(1,1))

for i in compound_all:
    plt.axhline(i, linewidth=0.5)
plt.text(4.3, 0.2,'*Blue line represents percentiles \n for all channels ')

plt.title('Comparing Sentiment Distributions')
plt.ylabel('Polarity Score')
plt.xlabel('Percentiles')

ax.set_xticks(index)
ax.set_xticklabels(compound_all.index)
plt.show()
```


![png](output_17_0.png)


Whereas our Bar Plot showed that Fox and BBC had more positive tweets based on mean score, we can also see that they have more positive tweets when looking at the distribution, too. This essentially means that their average scores are not just due to several outliers in the data. Instead, this supports the strength of our intial conclusion.

Next, let's look at the number of neutral vs not-neutral tweets.


```python
not_zero = df[df['Compound'] != 0]
not_zero['News Source'].value_counts()
```




    Fox        69
    CNN        64
    NYTimes    63
    CBS        63
    BBC        55
    Name: News Source, dtype: int64



Let's compare Fox and BBC to the others, to see if the proportion of neutral vs not-neutral tweets is significant with a 0.05 significance level.


```python
from statsmodels.stats import proportion as prop
prop.proportions_ztest([64, 55], [100, 100]),prop.proportions_ztest([69, 63], [100, 100])
```




    ((1.2964074471043283, 0.19483514774305044),
     (0.89562215103979737, 0.37045460103859473))



Apparently not. We can conclude that Fox and BBC create roughly the same number of neutral vs non-neutral tweets as the other sources.  
This is important to our earlier examination of the sentiment summaries because we can still reach the same conclusion from before, but with more detail. Fox and BBC do not simply tweet more positive messages, but overall are more positive in the tweets themselves.  
This may seem somewhat of a circle from looking at the mean, but now we have even stronger evidence of conclusions.
