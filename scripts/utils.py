from numpy import mask_indices
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import geopandas as gpd
import folium
import sys

sys.path.append("../")


def read_file(args):
    """read and create a dataframe from csv file with a start day columns
    Args:
        datapath ([url]): Location of the raw csv file
    Returns:
        df: Returns a pandas dataframe
    """
    # Read in the downloaded data
    df = pd.read_csv(args, parse_dates=["started_at", "ended_at"])
    df["start_day"] = df["started_at"].apply(lambda x: x.day_name())

    return df


def plot_busy_stations(args):
    """Use seaborn and matplotlib to plot the top 10 busiest stations
    Args:
        args : pandas dataframe with station names column
    """

    startstation = args["start_station_name"].value_counts()[:10]
    plt.figure(figsize=(18, 10))
    sns.barplot(x=startstation.values, y=list(startstation.index), orient="h")

    # Add plot title, label axes and grid
    plt.title("Busiest bike stations", size=22, family="monospace")
    plt.ylabel("Station Name", fontsize=16)
    plt.xlabel("Trips taken", fontsize=16)
    plt.grid()
    plt.tight_layout

    # Save the output to file
    plt.savefig("images/busiest_stations.png", facecolor="white", dpi=300)

    plt.show()


def main():
    df = read_file(datapath)
    plot_busy_stations(df)


if __name__ == "__main__":

    datapath = "data/raw/JC-202112-citibike-tripdata.csv"
    main()
