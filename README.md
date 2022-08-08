# Median of Means Estimator



A project to estimate the average price per product of a given dataset using the Median of Means estimator (MoM).

---------------
Why do we need the median of means estimator? 

![Research Paper](https://user-images.githubusercontent.com/96091453/169597364-bd067de8-9913-4d7b-8103-7254f49373c7.png)


------------------

Using NumPy we manage to create high-performance function using the MoM estimator; the function simply takes two arguments:
1. **arr:** takes array of the type numpy.ndarray
2. **n_splits:** number of chunks/groups/means on given arr 


![image](https://user-images.githubusercontent.com/96091453/169602676-4c61aec6-630a-453b-a3ec-bc85093d2d36.png)


We can see the importance of using the MoM estimator when we have a closer look over product 3; the mean is 10.15 while the MoM is 3, this is a huge difference, if we consider it from a pricing perspective, this happened because there is an outlier
![image](https://user-images.githubusercontent.com/96091453/170360458-6f3e848a-bd83-4b10-ba67-fd5ce182751f.png)

-------------------

## Why NumPy is fast? ##
1. **Parallel:** it divides the array into parts and computes all parts in parallel. 
2. **Same data types:** you have to tell NumPy upfront what data type is your array, it is more restrictive but this will be much more optimized on operating on these data types.
3. **Locality:** it puts all the numbers in the same area in your memory, which means that when you are doing these operations it's all happening within one chunk of your memory.

-----------------
## Execution Time ##

#### The code took 0.026 seconds to compute the median over 10 means for the 10 products ####

## And with bigger dataset? ##

#### The code took 0.453 seconds to compute the median of means on 1 Million floating numbers between -1 and 1 ####

## How about bigger dataset with bigger values? ##

#### The code took 3.239 seconds to compute the median of means on 10 Million floating numbers between 0 and 1 Million ####
----------------
[Try it yourself](https://colab.research.google.com/drive/1dUI23QSuPZaa7IcW_n2CK-0M_qE0HxKi?usp=sharing)
 
