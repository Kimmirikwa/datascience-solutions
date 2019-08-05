# solution to the data science exercise

For the problem description, kindly refer [here](https://github.com/jumo/de-public/tree/master/play/PLS/PLS0001)

The input data is in ```input.csv```. The requirement here is to aggregate the data on the ```Network```, ```Product``` and ```Month```. 
I decided to use *Python* in this exercise. This is because Python is easy to understand and a very intuitive language. There are very many great python libraries like *Pandas*(use here!), *Numpy*, *Scipy*, *Matplotlib* and others which are very easy to use when tacking data analysis. I have not used these libraries here as it is especially advised not to use any library like *Pandas* which has an implementation of aggregation. It also quite easy to have a python script to achieve something. Python is also highly portable.

I have used *csv* python library to read and write csv files.

The input data in this exercise was mostly clean except for some values having singles quotes i.e. ```'```. I removed them to make my analysis easier and cleaner. There were no missing data points too. I therefore made so many assumptions and came up with a simple solution to handle this data case. The following are some of the assumptions I had when coming up with my solution.

- I assumed that I was required to do any aggregation on the amount, so I chose to do the ```sum``` and ```mean```.
- I assumed that I was to group by ```Network```, then ```Product``` and finally ```Month``` as they were given in that order.
- The input data does not have any missing values. This is a very naive assumption as we it is well known that sometimes we usually have some data missing. I can improve this by handling missing values.
- I assumed that the columns used in aggregation had all their data points in the same case. For example, my solution treats ```Network 2``` and ```network 2``` as 2 different networks. This is definetely an issue.
- The function to extract month from ```Date``` assumed a constant date format for example ```12-Mar-2016```. My solution will not work if date is in any other format.

My solution goes through all the data examples serially as as it does the aggregation. With many examples, this could take a lot of time as it has a ```O(n)``` operational time. Parallelization of this processing will be very helpful especially for very many examples.

The result of my aggregation is in ```output/Output.csv```. Unfortunately for this data, all the ```Network```, ```Product``` and ```Month``` combinations were unique and we never had an aggregation with a count of more than 1.
