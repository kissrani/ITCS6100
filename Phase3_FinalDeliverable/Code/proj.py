
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#import boto3
import os
#get_ipython().system('pip install wordcloud')
from wordcloud import WordCloud, STOPWORDS 
from collections import Counter
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')
import random
#get_ipython().system('pip install streamlit')
import streamlit as st
data_key = 'rating.tsv'
#data_location = 's3://{}/{}'.format(bucketname, data_key)
title_ratings = pd.read_csv(data_key,sep='\t')

data_key = 'basics_movie.tsv'
#data_location = 's3://{}/{}'.format(bucketname, data_key)
title_basics = pd.read_csv(data_key,sep='\t')

model_data = pd.merge(title_ratings,title_basics, on = 'tconst')

model_data.to_csv('projectdata.csv')

# In[3]:
type_wise_counting = model_data.titleType.value_counts().reset_index(name='counts')
type_wise_counting = type_wise_counting.rename(columns = {'index':'types'})
#type_wise_counting
movies_type_ratings_avg = pd.DataFrame(model_data.groupby(['titleType'])['averageRating'].sum().reset_index(name='rating'))
movies_type_ratings_avg = movies_type_ratings_avg.sort_values(by=['titleType'], ascending = False)
movies_type_ratings_avg = movies_type_ratings_avg.rename( columns = {'titleType':'types'})

all_type_ratings = pd.merge(movies_type_ratings_avg,type_wise_counting, on = 'types')
all_type_ratings['avg_rating_type_wise'] = round(all_type_ratings.rating / all_type_ratings.counts,2)
#all_type_ratings

fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(111)
bar1 = plt.bar(all_type_ratings.types,all_type_ratings.avg_rating_type_wise)
plt.xticks(all_type_ratings.types)
plt.xlabel('types')
plt.ylabel('rating')
plt.title('Type ratings')
for rect in bar1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.2f' % float(height), ha='center', va='bottom')

st.pyplot(plt)


word_cloud_list = list(model_data.genres)
word_cloud_list = ','.join(word_cloud_list)
word_cloud_list = word_cloud_list.split(',')

word_could_dict = Counter(word_cloud_list)
wordcloud = WordCloud(width = 1000, height = 500).generate_from_frequencies(word_could_dict)


plt.figure(figsize=(15,6))
plt.bar(list(word_could_dict.keys())[:15],list(word_could_dict.values())[:15])
plt.tight_layout()
st.pyplot(plt)

plt.figure(figsize=(15,6))
plt.bar(list(word_could_dict.keys())[15:],list(word_could_dict.values())[15:])
plt.tight_layout()
st.pyplot(plt)











votes = model_data['numVotes']
m = votes.quantile(0.95)
C = model_data.averageRating.mean()


# In[4]:


def weighted_ratings(model_data):
    v = model_data['numVotes']
    R = model_data['averageRating']
    return (v/(v+m) * R) + (m/(m+v) * C)
  
model_data['wr'] = model_data.apply(weighted_ratings, axis=1)
model_data = model_data.sort_values(by = ['wr'], ascending = False)

word_cloud_list = list(set(word_cloud_list))
for i in word_cloud_list:
    model_data[i] = 0
    
for i in model_data.index:
    x = model_data['genres'][i].split(',')
    for k in x:
        model_data[k][i] = 1

cluster_data = model_data[['primaryTitle'] + word_cloud_list]

scaler = StandardScaler()
data_scaled = scaler.fit_transform(cluster_data.iloc[:,1:])


# In[5]:



A = []
for cluster in range(1,50):
    kmeans = KMeans(n_jobs = -1, n_clusters = cluster, init='k-means++')
    kmeans.fit(data_scaled)
    A.append(kmeans.inertia_)

frame = pd.DataFrame({'Cluster':range(1,50), 'SSE':SSE})
plt.figure(figsize=(12,6))
plt.plot(frame['Cluster'], frame['A'], marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
#fig = plt.show()
st.pyplot(plt)


data_scaled = data_scaled.astype('float32')
kmeans = KMeans(n_clusters=23, init='k-means++')
kmeans.fit(data_scaled)
pred = kmeans.predict(data_scaled)
final = pd.DataFrame(data_scaled)
final['cluster'] = pred
final


# In[6]:


def get_recommendations(title=None,types = None,ratings=None,year=None,genres=None):
    x = model_data
    if title != None:
        cluster_no = list(x[x['primaryTitle'].str.lower() == title.lower()]['cluster'])
        x = x[x['cluster'] == random.choice(cluster_no)]
    if types != None:
        x = x[x['titleType'].str.lower() == types.lower()]
    if year != None:
        x = x[x['startYear'] == year]
    if genres != None:
        list_of_genres = genres.split(',')
        x = x[x[genres.capitalize()] == 1]
    if ratings != None:
        x = x[x['wr'] >= ratings]
    
    return x[:15]


# In[7]:


get_recommendations(types='short', genres='comedy')


# In[8]:


text_input=st.text_input("Enter type")
text_input1=st.text_input("Enter genres")
#text_input2=st.text_input("Enter rating")
#text_input3=st.text_input("Enter title")


a = get_recommendations(types=text_input, genres=text_input1)
a


# In[ ]:
