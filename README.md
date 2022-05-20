# Median of Means Estimator


<p align="center">
  <img width="460" height="300" src="https://user-images.githubusercontent.com/96091453/169597145-2a7c9d7c-0fa6-4b7d-969c-e39dc7467f7c.png">
</p>

Take home project from buynomics, the task is to estimate the average price per product in the given dataset using the Median of Means estimator (MoM). 

---------------
Why do we need the median of means estimator? 

![Research Paper](https://user-images.githubusercontent.com/96091453/169597364-bd067de8-9913-4d7b-8103-7254f49373c7.png)


------------------

Using Numpy we manage to create high-performance function using the MoM estimator; the function simply takes two arguments:
1. **arr:** takes array of the type numpy.ndarray
2. **n_splits:** number of chunks/groups/means on given arr 


![image](https://user-images.githubusercontent.com/96091453/169602676-4c61aec6-630a-453b-a3ec-bc85093d2d36.png)


-----------------
## Execution Time ##

#### The code took 0.026 seconds to compute the median over 10 means for the 10 products ####

## And with bigger dataset? ##

#### The code took 0.453 seconds to compute the median of means on 1 Million floating numbers between -1 and 1 ####

## How about bigger dataset with bigger values? ##

#### The code took 3.239 seconds to compute the median of means on 10 Million floating numbers between 0 and 1 Million ####

