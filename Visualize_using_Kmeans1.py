# Visualising the Clusters
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Cluster 3')

"""

plt.scatter(X[y_kmeans == N, 0], X[y_kmeans == N, 1], s = 100, c = 'cyan', label = 'Cluster N')

Repeat the above line with modifications of color and label and N acccording to your number of Clusters."""


plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of clients')
plt.xlabel('Variable 1')
plt.ylabel('Variable 2')
plt.legend()
plt.show()