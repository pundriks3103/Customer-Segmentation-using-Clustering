#Important Note
""" In the following code,
V1 = Name of 1st variable
V2 = Name of 2nd variable
V3 = Name of 3rd variable"""

#Visualizing Clusters using K_means
labels = kmeans.labels_
centroids3 = kmeans.cluster_centers_
df['label'] =  labels
trace1 = go.Scatter3d(x= df['V1'], z= df['V3'], y= df['V2'], mode='markers', marker=dict(color = df['label'], size= 10, line=dict(color= df['label'], width= 12), opacity=0.8))
data = [trace1]
layout = go.Layout(title= 'Clusters',scene = dict(xaxis = dict(title  = 'V1'), zaxis = dict(title  = 'V3'), yaxis = dict(title  = 'V2')))
fig = go.Figure(data=data, layout=layout)
py.offline.iplot(fig)