# -*- coding: utf-8 -*-
import csv
import numpy as np
with open("winequality-red.csv") as f:
    wines = list(csv.reader(f,delimiter=";"))

print(wines[:3])

#iterate over all the rows and trasfer as float
qualities = [float(item[-1]) for item in wines[1:]]
sum(qualities) / len(qualities)             

#all the elements in an array have to be of the same type

#how to auto create keyword argument?
wines = np.array(wines[1:], dtype = np.float)

#numpy array has shape property

#we can laso create n-dimension array
np.random.rand(3,3,3,3)
#if we want to creat a array that contains two years quaterly data
dimen3 = np.random.rand(2,4,3)
#extract second years first quarter data
dimen3[1,0,:]

#we used skip_header to avoid reading it as float
wines2 = np.genfromtxt("winequality-red.csv", delimiter =';', skip_header=1)
wines2[2,3]

#we can check the data types like this
wines.dtype
#these are the most important data types in numpy
#float, int, string, object

int_wines = wines.astype(int)
int_wines

#control over the bit value
int_wines = wines.astype(np.int64)
int_wines.dtype

#if you do any of the basic mathematical operations with an array and a value
#it will apply the operation to each of the elements in the array
wines[:11]+10

#if we want to directly modify the array
wines[:11]+=10

#check indexing
np.shape(wines[1:2])

#Its also possible to do mathematical operations between arrays
np.shape(wines[:,11] + wines[:,11])

#all of the common operations will work between arrays
wines[:,11]*wines[:,10]

#Broadcasting!!!!
'''
rules!

the last dimension of each array is compared

if the dimension lengths are equl, or one of the dimensions is of length1
then we can keep going

if the dimension lengths aren't equal, and none of the dimensions have length 1
then there's an error

continue checking dimensions until the shortest array is out of dimensions
'''
#for example
'''
(50,3)
(3,)

These shapes are compatible:
because the length of the trailing dimension of array A and B is equal,
then B is out of elements


The following two shapes are also compatible
(1,2)
(50,2)
'''
#is this possible?
a = np.random.rand(6,10)
b= np.zeros([2,10])
#not possible, why?


#numpy method
wines[:,11].sum()

#we can pass the axis keyword argument into the sum method to find sums over an axis
len(wines.sum(axis=0))

#axis = 0 mean columnwise, axis = 1 mean rowwise
wines.sum(axis=1)

#we can also do things like
wines.mean()
wines.std()
wines.min()
wines.max()

#numpy array comparision is also possible
(wines[:,11]<30).sum()

high_qual = wines[:,11]>7
wines[high_qual,:]

#Reshaping Numpy Arrays

#first transpose
np.transpose(wines).shape

#flatten an array into vector
wines.ravel()

#reshape
wines[1,:].reshape((2,6))

#combining numpy arrays
first = np.genfromtxt("winequality-red.csv", delimiter=";", skip_header=1)
first.shape
#vertically
all_wines = np.vstack((wines,first))
#horizontally
all_cols = np.hstack((wines,first))
#both of the methods above can be done by using
np.concatenate((wines,first), axis=0) 
np.concatenate((wines,first), axis=1)
