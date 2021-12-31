#Import pandas package
import pandas as pd

#Define filepath either relative or absolutepath to file
path = r"D:\WorkSpace\Bike Mapping\201912-citibike-tripdata\201912-citibike-tripdata.csv"

#Open csv file
data = pd.read_csv(path)

#Check our data columns
print(data.columns)

#Group data by columns we are interested in our case station where ride started
group1 = data.groupby(['start station id',
       'start station name', 'start station latitude',
       'start station longitude'])

#Check our length of group
print(len(group1))

#Create a list to store our group keys
key = [key for key, _ in group1]

#Create a dataframe from the list
df = pd.DataFrame(key)

#Check our new dataframe first 5 rows
print(df.head)

#Rename our columns
df.rename(columns = {0 :'StationID', 1 :'StationName',
                    2 :'Lat', 3 :'Lon'}, inplace = True)

# saving the dataframe to csv file
outpath = r'./2019Dec.csv'
df.to_csv(outpath, index=False)

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