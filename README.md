# Prediction and validation

I used the following library for my script:

Pandas, Numpy, io, os, decimal and sys. 

The use of pandas and numpy  is standard. I used io to import the time window file, and sys to take inputs from the system. I used module Decimal to round up the float numbers. 

The main idea is to create a data frame with both actual value and prediction value by matching the time and stock name. If either actual value or prediction value is not available, the output is 'NA'. Then I filtered out the NA values. 

To compute the average error, I first sum up the errors during each time window and the number of non-NA value pairs in the time window. Then I divide using the Decimal module. Since we are only computing over the time window from the predicted time, some care must be taken with NA values if two values do not match. I take the time from the predicted file as the default time, and assign 0 if the difference between the two values is not available. This take care of the edge cases. 

For the custom test case, I checked the situation when there is no match during an hour, and no match during an entire time window. The later case should output NA while the previous one should give me modified output values. 

