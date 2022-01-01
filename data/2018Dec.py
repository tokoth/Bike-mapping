# Import pandas package
import pandas as pd


# Define filepath either relative or absolute path to file
#In our cases we use a relative path
path = r"D:\WorkSpace\Bike Mapping\201812-citibike-tripdata\201812-citibike-tripdata.csv"

# Open csv file
data = pd.read_csv(path)

# Check our data columns
print(data.columns)

# Group data by columns we are interested in our case station where ride started
group1 = data.groupby(['start station id',
       'start station name', 'start station latitude',
       'start station longitude'])

# Check our length of group
print(len(group1))

# Create a list to store our group keys
key = [key for key, _ in group1]

# Create a dataframe from the list
df = pd.DataFrame(key)

# Check our new dataframe first 5 rows
print(df.head)

# Rename our columns
df.rename(columns={0: 'StationID', 1: 'StationName', 2: 'Lat', 3: 'Lon'}, inplace=True)

# Saving the dataframe to csv file
outpath = r'./2018Dec.csv'
df.to_csv(outpath, index=False)

#Converting Dataframe to GeoDataframe

# Import necessary package geopandas
import geopandas as gpd

#Read in our cleaned data
#Define file path add relative filepath to our data
path = r'../data/2018Dec.csv'

data2018 = pd.read_csv(path)
data2018.head()

#Convert DataFrame to GeoDataFrame
gdf_2018 = gpd.GeoDataFrame(
    data2018, geometry=gpd.points_from_xy(data2018.Lon, data2018.Lat))
gdf_2018.head()

#Assign crs to the geodataframe
gdf_2018 = gdf_2018.set_crs('epsg:4326')

# Let's make a backup copy of our data
gdf_merc18 = gdf_2018.copy()

#We will use the backup in our subsequent analysis
gdf_merc18 = gdf_merc18.to_crs(epsg=3857)

#Import matplotlib package for our plotting and contextly for our basemaps
import matplotlib.pyplot as plt
import contextily as ctx

# Create one subplot. Control figure size in here.
fig, ax = plt.subplots(figsize=(10,20))

#Plot the static map
gdf_merc18.plot(ax=ax,c="black")

# Set title and label axes
plt.title("Map Showing Bike usage in NewYork City, 2018", 
          fontsize=14,color="black")
plt.xlabel('Longitude', fontsize=18)
plt.ylabel('Latitude', fontsize=18)

#Add basemap from contextly
ctx.add_basemap(ax)

#Save the figure as png file with resolution of 100 dpi
outfp = "2018_static_map2.png"
plt.savefig(outfp, dpi=100)

#Repeat the same process for the 2019 and 2020 cleaned data

#2019

#Define file path add relative filepath to our data
path = r'../data/2019Dec.csv'

data2019 = pd.read_csv(path)

#Convert DataFrame to GeoDataFrame
gdf_2019 = gpd.GeoDataFrame(
    data2019, geometry=gpd.points_from_xy(data2019.Lon, data2019.Lat))
gdf_2019.head()

#Assign crs to the geodataframe
gdf_2019 = gdf_2019.set_crs('epsg:4326')
# Let's make a backup copy of our data
gdf_merc19 = gdf_2019.copy()
#We will use the backup in our subsequent analysis
gdf_merc19 = gdf_merc19.to_crs(epsg=3857)
gdf_merc19.crs
print('Finished with 2019')

#2020

#Define file path add relative filepath to our data
path = r'../data/2020Dec.csv'

data2020 = pd.read_csv(path)

#Convert DataFrame to GeoDataFrame
gdf_2020 = gpd.GeoDataFrame(
    data2020, geometry=gpd.points_from_xy(data2020.Lon, data2020.Lat))
gdf_2020.head()

#Assign crs to the geodataframe
gdf_2020 = gdf_2020.set_crs('epsg:4326')
# Let's make a backup copy of our data
gdf_merc20 = gdf_2020.copy()
#We will use the backup in our subsequent analysis
gdf_merc20 = gdf_merc20.to_crs(epsg=3857)
gdf_merc20.crs
print('Finished with 2020')

#Interactive Mapping
#Import folium package for interactive mapping
import folium

#Create Map instance

m=folium.Map(location=[40.707222,-73.9909],tiles='OpenStreetMap', zoom_start=14, min_zoom=12, max_zoom=18)

#Add another basemap layer
folium.TileLayer('cartodbpositron').add_to(m)

#Create feature groups
f1=folium.FeatureGroup("Stations 2018")
f2=folium.FeatureGroup("Stations 2019")
f3=folium.FeatureGroup("Stations 2020")

#Add the dataframes to our feature groups
gd2018 = folium.GeoJson(gdf_merc18,marker=folium.Marker(
                        icon=folium.Icon(color='darkblue')),
                        tooltip=folium.GeoJsonTooltip(fields=["StationName"]),
                       ).add_to(f1)
gd2019 = folium.GeoJson(gdf_merc19,marker=folium.Marker(
                        icon=folium.Icon(color='darkblue')),
                        tooltip=folium.GeoJsonTooltip(fields=["StationName"]),
                       ).add_to(f2)
gd2020 = folium.GeoJson(gdf_merc20,marker=folium.Marker(
                        icon=folium.Icon(color='darkblue')),
                        tooltip=folium.GeoJsonTooltip(fields=["StationName"]),
                       ).add_to(f3)

#Add feature groups to Map instance
f1.add_to(m)
f2.add_to(m)
f3.add_to(m)

#Add layer Control
folium.LayerControl().add_to(m)  # use folium to add layer control
m

#Save the interactive map to webpage
outfp = "interactive_map2.html"
m.save(outfp)