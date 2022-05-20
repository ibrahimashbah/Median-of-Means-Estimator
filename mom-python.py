#!/usr/bin/env python
# coding: utf-8


import numpy as np
import pandas as pd
from time import time


# Loading Dataset
df = pd.read_csv('question-custom-takehome-project-zpnxbh3x9d-sales.csv')


# Computing Median of Means 

start_time = time()  # start time of execution


# returns the median of means of given array
def median_of_means_estimator(arr, n_chunks):
    if n_chunks <= 0:
        raise Exception("Sorry, number of chunks must me bigger than zero")
    if not type(arr) is np.ndarray:
        raise TypeError("Only numpy.ndarray are allowed")
    if n_chunks > len(arr):  # preventing the n_chunks > n_observations
        n_chunks = int(np.ceil(len(arr) / 2))

    # creating shuffled array of int for random selection on arr
    shuffler = np.array(list(range(n_chunks)) * int(len(arr)/ n_chunks))
    np.random.shuffle(shuffler)

    # computing mean per chunk
    means = [np.mean(arr[list(np.where(shuffler == chunk)[0])]) for chunk in range(n_chunks)]

    # return median
    return np.median(means)


# slicing dataset into arrays based on proudct_id
sliced = [y for (x, y) in df.groupby('product_id')]

# creating dataframe to display the computed MoM per product
products_mom = pd.DataFrame(columns=['product_id', 'mean', 'median_of_means'])

for i in range(len(sliced)):  # iterate over the sliced dataset
    mom = median_of_means_estimator(np.array(sliced[i]['price']), 10)  # computing the MoM per product
    mean = sliced[i]['price'].mean()

    # getting the product id number from the sliced dataset
    product_id = int(sliced[i]['product_id'].unique())
    products_mom = pd.concat([pd.DataFrame([[product_id, mean, mom]], columns=products_mom.columns), products_mom], ignore_index=True)
    
# printing out the result
display(products_mom.sort_values(by='product_id'))


end_time = time()  # end time of execution

t1 = end_time - start_time

print ('The computation took %s seconds' % t1)
## The computation took 0.026923656463623047 seconds ##


## Execution time ##

# Over Size
start_time2 = time()

first_population = np.random.standard_t(df=1, size=1000000)
print(median_of_means_estimator(first_population, 10))

end_time2 = time()

t2 = end_time2 - start_time2
print ('The computation took %s seconds' % t2)
## The computation took 0.45382094383239746 seconds ##


# Over Size and values 

start_time3 = time()

second_population= np.random.uniform(0, 1000000, 10000000)
print(median_of_means_estimator(second_population, 10))
end_time3 = time()

t3 = end_time3 - start_time3
print ('The computation took %s seconds' % t3)
## The computation took 3.2399840354919434 seconds ##

