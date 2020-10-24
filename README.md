# Customer Segmentation using Clustering
---
![](https://github.com/pundriks3103/Customer-Segmentation-using-Clustering/blob/main/img.png?raw=true)

Customer Segmentation is the process of division of customer base into several groups of individuals that share a similarity in different ways that are relevant to marketing such as gender, age, interests, and miscellaneous spending habits.

Companies that deploy customer segmentation are under the notion that every customer has different requirements and require a specific marketing effort to address them appropriately. Companies aim to gain a deeper approach of the customer they are targeting. Therefore, their aim has to be specific and should be tailored to address the requirements of each and every individual customer. Furthermore, through the data collected, companies can gain a deeper understanding of customer preferences as well as the requirements for discovering valuable segments that would reap them maximum profit. This way, they can strategize their marketing techniques more efficiently and minimize the possibility of risk to their investment.

# Usage 

1. For implementing the model directly on [Mall Customers Dataset](https://www.kaggle.com/vjchoudhary7/customer-segmentation-tutorial-in-python),
    *   Download the file [complete_code.py](https://github.com/pundriks3103/Customer-Segmentation-using-Clustering/blob/main/complete_code.py) and keep it in the same folder as your project notebook/script.
    *   Make sure your dataset (downloaded in same folder as project noteboob) has same name as used for loading the Data in the python file, i.e, **Mall_Customers**
    *   Execute the complete code to get a Visualisation of the Clusters/Groups formed.

2. For implementing the model on any other dataset,
     *   First do the Complete analysis and Pre-processing of the data to reduce the number of variables. (Take reference of the 2 solved examples)
     *   Define the input matrix with the variable **X** before applying the Model.
     *   Apply the [model_using_Kmeans.py](https://github.com/pundriks3103/Customer-Segmentation-using-Clustering/blob/main/model_using_Kmeans.py).
     *   If your Input matrix has more than 3 variables, see the output in **y_pred** with each number representing a cluster. ( i.e., y_pred = 1 represents one cluster and y_pred = 2 represents another cluster and so on)
     *   If your Input marix has 3 variables, Visualize the Output using [Visualize_using_Kmeans.py](https://github.com/pundriks3103/Customer-Segmentation-using-Clustering/blob/main/Visualize_using_Kmeans.py)
     *   If your Input matrix has only 2 variables, Visualize the Output using [Visualize_using_Kmeans1.py](https://github.com/pundriks3103/Customer-Segmentation-using-Clustering/blob/main/Visualize_using_Kmeans1.py)
    


# Example on Dataset

Go through the [Example](https://github.com/pundriks3103/Customer-Segmentation-using-Clustering/blob/main/FinalCustomer_Segmentation.ipynb) notebook to see an example where this model is used on the [dataset](https://www.kaggle.com/vjchoudhary7/customer-segmentation-tutorial-in-python) provided by Kaggle.
