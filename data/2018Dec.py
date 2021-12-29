# Import pandas package
import pandas as pd


# Define filepath either relative or absolute path to file
#In our cases we use a relative path
path = r'./201812-citibike-tripdata.csv'

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
df.to_csv(outpath)