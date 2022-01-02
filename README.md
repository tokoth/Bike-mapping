# `Bike Mapping`


### About
A  project looking into how to process, clean, and visualize huge open datasets.

![Image](https://drive.google.com/uc?export=view&id=12RrVqvfGr7JIgHuept4swzHCWKOchnHF)
 
Huge credits to [Citi Bike System Data](https://ride.citibikenyc.com/system-data) New York City, for publishing there bike rides data, this is used as my datasource for the project.

### Objective

The main objective was to visualize geospatial data in Python.

The bike rides monthly data is a huge dataset. Depending on the season, the trip data files contain one record for each ride, with roughly two million records every month. It's a standard bike share system with fixed stations where a user takes up a bike from one dock and returns it to another using a key fob or a code. For each ride, the station and time the ride began and ended are recorded.

For this data visualization project a few assumptions were made so as to map only a sample of the data.

    1. Only data from the month of December was used for our mapped years i.e. year 2018, 2019 & 2020
    
    2. The data was cleaned and grouped by Station name and Station id.
    
    3. The resulting cleaned data indicated all the bike station where atleast one bike trip originated from the station.


### Data Processing

For this project the Python language and its packages were used in data manipulation, cleaning, processing and visualization.

Packages used was; Pandas, Geopandas, Matplotlib, Contextily, and Folium.

The logical steps taken for this task is:
1. Download the [Citi Bike System Data](https://ride.citibikenyc.com/system-data), December data for years 2018, 2019 and 2020. 
2. Using Pandas to read the downloaded data, observe, analyse, group(by Station name and Station id), aggregate and write to an output csv file containing the cleaned data.
3. Using GeoPandas to read in the cleaned data to a dataframe, convert it to a geodataframe. Create a backup copy of our data, assign a coordinate reference system(crs) to our geodataframe.
4. Using Matplotlip to plot our geodataframes into static maps, using Contextily to add a basemap to our static maps and write to an output file of image format.
5. Using Folium to create an interactive map instance, add all the geodataframes for the years as a feature group to our map instance. Save and output an interactive map to a webpage.


### Results


[`Interactive Map`]()





