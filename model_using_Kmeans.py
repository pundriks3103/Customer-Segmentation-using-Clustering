#Elbow Method Explained to find the number of Clusters

"""
1. WCSS is defined as the Within Cluster Sum of Squares. It is the measure of sum of distances of observations from their cluster centroids. 
2. The elbow method runs k-means clustering on the dataset for a range of values for k (say from 1-10) and then for each value of k computes a WCSS for all clusters.
3. The lesser the WCSS, the better is the model.
4. WCSS will eventually tend to 0 as no. of clusters tend to no. of observations. So, for an optimal number of clusters, **the point upto which the Decrement in WCSS is large is taken as the optimal number of Cluster.** 
"""

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

#Important Note
"""
First define n as the number of clusters you want to take based on Above Elbow Graph.
"""

n = 

# Applying K-means to the Mall datasheet
kmeans = KMeans(n_clusters = n, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
y_kmeans = kmeans.fit_predict(X)
