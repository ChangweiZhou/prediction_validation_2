# Prediction and validation - Insight data science challenge

I used the following library for my script:

Pandas, Numpy, io, os, decimal and sys. 

The use of pandas and numpy  is standard. I used io to import the time window file, and sys to take inputs from the system. I used module Decimal to round up the float numbers. 

The main idea is to create a data frame with both actual value and prediction value by matching the time and stock name. If either actual value or prediction value is not available, the output is 'NA'. Then I filtered out the NA values. 

To compute the average error, I first sum up the errors during each time window and the number of non-NA value pairs in the time window. Then I divide using the Decimal module. 

