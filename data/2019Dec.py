#Import pandas package
import pandas as pd

#Define filepath either relative or absolutepath to file
path = r"D:\WorkSpace\Bike Mapping\201912-citibike-tripdata\201912-citibike-tripdata.csv"

#Open csv file
data = pd.read_csv(path)

#Check our data columns
print(data.columns)

#Group data by columns we are interested in our case station where ride started

#Using the aggregate with groupby to group and 
#count the number of occurences in each group and assign to a new dataframe
df_grouped = data.groupby(['start station id',
       'start station name', 'start station latitude',
       'start station longitude'], as_index=False).agg(
    count_col=pd.NamedAgg(column="start station id", aggfunc="count")
)

# Rename our columns
df_grouped.rename(columns={'start station id': 'Station ID', 
                    'start station name': 'Station Name', 
                    'start station latitude': 'Lat', 
                    'start station longitude': 'Lon', 
                    'count_col':'Number of Trips'}, inplace=True)

# Saving the dataframe to csv file
outpath = r'./2019Dec.csv'
df_grouped.to_csv(outpath, index=False)

#Converting Dataframe to GeoDataframe

# Import necessary package geopandas
import geopandas as gpd

#Read in our cleaned data
#Define file path add relative filepath to our data
path = r'../data/2019Dec.csv'

gdata = pd.read_csv(path)
gdata.head()

#Convert DataFrame to GeoDataFrame
gdf = gpd.GeoDataFrame(
    gdata, geometry=gpd.points_from_xy(gdata.Lon, gdata.Lat))
gdf.head()

#Assign crs to the geodataframe
gdf = gdf.set_crs('epsg:4326')

# Let's make a backup copy of our data
gdf_merc = gdf.copy()

#We will use the backup in our subsequent analysis
gdf_merc = gdf_merc.to_crs(epsg=3857)

#Import matplotlib package for our plotting and contextly for our basemaps
import matplotlib.pyplot as plt
import contextily as ctx

# Create one subplot. Control figure size in here.
fig, ax = plt.subplots(figsize=(10,20))

#Plot the static map
gdf_merc.plot(ax=ax,c="black")

# Set title and label axes
plt.title("Map Showing Bike usage in NewYork City, 2019", 
          fontsize=14,color="black")
plt.xlabel('Longitude', fontsize=18)
plt.ylabel('Latitude', fontsize=18)

#Add basemap from contextly
ctx.add_basemap(ax)

#Save the figure as png file with resolution of 100 dpi
outfp = "2019_static_map.png"
plt.savefig(outfp, dpi=100)