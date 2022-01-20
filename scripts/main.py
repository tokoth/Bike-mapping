import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import geopandas as gpd
import folium


def read_file(datapath):
    """read and create a dataframe from csv fileread_file
    Args:
        datapath ([url]): Location of the raw csv file
    Returns:
        data: Returns a pandas dataframe 
    """
    #Read in the downloaded data
    data = pd.read_csv(datapath, parse_dates=['started_at','ended_at'])
    return data



    