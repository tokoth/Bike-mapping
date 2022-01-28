<a name="top"></a>
<h1 align="center">BIKE MAPPING</h1>

***
[![Twitter](https://img.shields.io/badge/tyson_okoth-%231DA1F2.svg?style=for-the-badge&logo=Twitter&logoColor=white)](https://twitter.com/tyson_okoth)
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/okoth-tyson-0968a9178/)
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/tokoth)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:tysonokoth8@gmail.com)

***
## Table of Contents
* [About](#About)
* [Objective](#About)
* [Results](#Results)
* [Maps (Static and Interactive)](#Maps)
* [Credits](#Credits)

***

<a name="About"></a>
### About
A  project looking into processing, cleaning, and visualizing huge open datasets, by exploring NYC Bike Share Data

![Image](https://drive.google.com/uc?export=view&id=12RrVqvfGr7JIgHuept4swzHCWKOchnHF)
 
Huge credits to [Citi Bike System Data](https://ride.citibikenyc.com/system-data) New York City, for publishing there bike rides data, this is used as my datasource for the project.

### Objective

The main objective was to visualize geospatial data in Python.

The bike rides monthly data is a huge dataset. Depending on the season, the trip data files contain one record for each ride, with roughly two million records every month. It's a standard bike share system with fixed stations where a user takes up a bike from one dock and returns it to another using a key fob or a code. For each ride, the station and time the ride began and ended are recorded.

For this data visualization project a few assumptions were made so as to map only a sample of the data.

    1. Only data from the month of December was used for years 2018, 2019 & 2020.
    
    2. The data was cleaned and grouped by Station name and Station id.
    
    3. The resulting cleaned data indicated all the bike station where atleast one bike trip originated from the station
    and the number of trips recorder from the station.


#### Data Processing

For this project the Python language and its packages were used in
data reading, observing, cleaning, processing and visualization of the data.

Packages used was; Pandas, Seaborn, Geopandas, Matplotlib, Contextily, and Folium.

<p align="left">  <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="30" height="30"/> </a> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="30" height="30"/> </a> <a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" alt="pandas" width="30" height="30"/> </a> <a href="https://seaborn.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://seaborn.pydata.org/_images/logo-mark-lightbg.svg" alt="seaborn" width="30" height="30"/> </a>  <a href="https://matplotlib.org/" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/8/84/Matplotlib_icon.svg" alt="matplotlib" width="30" height="30"/> </a></p>


The logical steps taken for this task is:
1. Download the [Citi Bike System Data](https://ride.citibikenyc.com/system-data), December data for years 2018, 2019 and 2020. 
2. Using Pandas to read the downloaded data, observe, analyse, group(by Station name and Station id), aggregate and write to an output csv file containing the cleaned data.
3. Using Seaborn to show and visaulize graphs and charts of the observed data.
4. Using GeoPandas to read in the cleaned data to a dataframe, convert it to a geodataframe. Create a backup copy of our data, assign a coordinate reference system(crs) to our geodataframe for our mapping.
5. Using Matplotlip to plot our geodataframes into static maps, using Contextily to add a basemap to our static maps and write to an output file of image format.
6. Using Folium to create an interactive map instance, add all the geodataframes for the years as a feature group to our map instance. Save and output an interactive map to a webpage.

<a name="Results"></a>
### Results

Read in the downloaded data and display using Pandas.

  ```Python
 #Read and display the data
    data = pd.read_csv("201812-citibike-tripdata.csv")
```

We display the first 5 rows using head() method.
   
```Python
    data.head()
```

![Image](https://drive.google.com/uc?export=view&id=1doIVdoiJGHNn2Mas2wnC4-4wze8S8Nc1)
<h6 align="center">Output head, First 5 rows</h6>

We can get some information about the columns with the info() method.

```Python
    data.info()
```
![Image](https://drive.google.com/uc?export=view&id=1w78j-xzkyHdq6OOc-40E9hBVGS56uUcL)

The output shows the number of rows (just over a million) and the number of columns.

We can now prepare the data further using Pandas and explore some descriptive information from the data. 
Using Seaborn and matplotlib to plot and display graphs of busiest days, and top 10 busiest stations.

![Image](https://drive.google.com/uc?export=view&id=1UoY0_zKNhcNx0AqyGRMbXc0ch5A3kSf1)

![Image](https://drive.google.com/uc?export=view&id=18LqKspwDEi6eNE-PMNzQ4wj5fmgX025p)

After cleaning, grouping the data by (Station ID and Station Name) and aggregating we go ahead,and write to an output csv file.

We use GeoPandas to read in the cleaned data, convert it to a geodataframe. Assign a Coordinate reference system (CRS) to our geodataframe for our mapping

We display the first 5 rows using head() method, the geodataframe has a geometry column that allows us to plot the data to a location map.

```Python
    geodata.head()
```

![Image](https://drive.google.com/uc?export=view&id=1nhVr3_0OjZvORRTNsQnMDhIPZZRxXti5)

We check the CRS of our geodataframe using .crs method, which shows the EPSG code of the data.

```Python
    print(geodata.crs)
```

![Image](https://drive.google.com/uc?export=view&id=1zwrgfgcDSvmcbYABTeQIqZVyHmiOKccz)

The CRS of our geodataframe, Web Mercator(EPSG:3857) is projected coordinate system used for rendering maps in Google Maps, OpenStreetMaps. It is mostly used in web mapping and visualization applications.

We will use the geodataframe to plot a Static map with basemap as well as an Interactive map.


<a name="Maps"></a>
### Maps (Static and Interactive)

A Static Map plotted with Matplotlib and Contextily using information of the 2018 bike stations cleaned data.

![Image](https://drive.google.com/uc?export=view&id=1Y_ABD8DDLMuEzFMJaRdyIpNJhsgT2vtA)

An Interactive map plotted with Folium showing the busiest bike stations used in the years 2018, 2019 ,and 2020. 
You can interact with the map and change the basemap as well as switch and display the interested year.

<iframe src="data/interactive_map.html" height="800" width="1000"></iframe>

Explore the interactive map further [here](https://tokoth.github.io/Bike-mapping/data/interactive_map.html).

<a name="Credits"></a>
### Credits

The cleaned datasets, python scripts and notebooks used for this project can be accessed [here](https://github.com/tokoth/Bike-mapping/tree/main/data).

Huge credits to [Citi Bike System Data](https://ride.citibikenyc.com/system-data) New York City, for publishing there bike rides data, this is used as my datasource for the project.

[Explore Bike share data](https://towardsdatascience.com/exploring-bike-share-data-3e3b2f28760c), The blog was a helpful guide when processing the data using Pandas. 

[`Back to Top`](#top)
