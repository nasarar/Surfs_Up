# Surfs_Up

## Project Overview
The client is looking for a weather analyisis to determine if the new Surf and Shake shop is viable business to run all year long in the island of Oahu. The investors provided the weather dataset that the analysis is being performed including the breakdown of precipitation and temperatures all year. A list of deliverables is hightlighted below as per the investor's requirements.

1. Query the dataset to retrieve and plot the last 12 months of precipitation.
2. Find the most active weather station.
3. Query the last 12 months of temperature observation and plot the data.
4. Filter the data specifically for the month of June and December, and create a dataframe of the results.
5.  Create a summary statistics including the count, mean, standard deviation, minimum, maximum and 25/50/75 quartiles for the precipitation data and temperature data.


## Resources
- Data Source: hawaii.sqlite
- Software: Jupyter Notebook 6.2.0, Anaconda 2020.11, Python 3.6.7, Visual Studio Code 1.52.1

## Results

June Summary
![](Resources/June_Summary.png)

December Summary
![](Resources/December_Summary.png)
- Given the start of summer and winter in Oahu, Hawaii; the average temperature difference between two opposite months are not drastically different with the summer averaging at about 74 degrees while winter at 71 degrees Farenheit. With this information, the demand for the business should not taper off drastically in the 'off season'.
-  The median for December's temperature is 71 degrees while the Summer's median is 75 degrees farenheit, it can be safely assumed that although the difference isnt drastic like stated in the first argument, there will be more slower days during the winter especially if half of the time the temperatures fall below 71 degrees. 
-  Strictly loooking at one of the 'worst' weathers in terms of temperature that is analyzed, it can also be safely assumed that 25% of the time during the month of December it will be a slower day considering the temperatures fall below 69 degrees farenheit. Different sets of data including precipitation has to be analyzed in order to solidify this statement. Nonetheless it is a good starting point for an assumption. 


## Summary
While this particular analyis heavily revolved around the opposite weather seasons of summer and winter, the initial invesitigation shows that the temperatures differences between the two are quite similar therefore in theory there won't be a big drop off in sales. However there are further investigations that could be done to aid the decision of the investors, particularly looking at the precipations averages for each month. Although the temperatures might be similar the precipitation might deter tourists from visiting a particular month therefore less business. Another query that could be performed with the given dataset is finding out the where the lowest and highest rates of precipitation is on the island is on the given month by filtering precipitation rates by the weather station. Within the 'station' table of the dataset, there will be a set of coordinates that would indicate its observation location. The dataset provided is limited to the precipitation and temperature rates, to expand the analysis; data on the number of tourists and further weather analyis like humidity and cloud coverage  should be provided. 
