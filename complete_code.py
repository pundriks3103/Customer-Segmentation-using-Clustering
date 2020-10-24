#Importing the Libraries
import numpy as np
import pandas as pd
import seaborn as sns
import plotly as py
import matplotlib.pyplot as plt
import plotly.graph_objs as go
from sklearn.preprocessing import LabelEncoder # For Label Encoding
from sklearn.cluster import KMeans # For K-means Algorithm
from sklearn.cluster import AgglomerativeClustering # For Hierarchical Clustering
import scipy.cluster.hierarchy as sch # For Dendogram Method to find Cluster number

#Step 2** Loading and Exploration of the Dataset
df = pd.read_csv('Mall_Customers.csv')
df = df.drop('CustomerID', axis = 1)

#Label Encoding
labelencoder = LabelEncoder()
df['Gender']= labelencoder.fit_transform(df['Gender'])

X = df[['Age' , 'Annual Income (k$)', 'Spending Score (1-100)']].iloc[: , :].values

# Using the elbow method to find the optimal number of clusters
wcss = []
for i in range(1, 11):
        kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)
plt.figure(1 , figsize = (10 , 5))
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xticks(ticks = [1,2,3,4,5,6,7,8,9,10])
plt.xlabel('The Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# Applying K-means to the Mall datasheet
kmeans = KMeans(n_clusters = 6, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
y_kmeans = kmeans.fit_predict(X)

#Visualizing Clusters
labels = kmeans.labels_
centroids3 = kmeans.cluster_centers_
df['label'] =  labels
trace1 = go.Scatter3d(x= df['Age'], z= df['Annual Income (k$)'], y= df['Spending Score (1-100)'], mode='markers', marker=dict(color = df['label'], size= 10, line=dict(color= df['label'], width= 12), opacity=0.8))
data = [trace1]
layout = go.Layout(title= 'Clusters',scene = dict(xaxis = dict(title  = 'Age'), zaxis = dict(title  = 'Annual Income'), yaxis = dict(title  = 'Spending Score')))
fig = go.Figure(data=data, layout=layout)
py.offline.iplot(fig)

