###############################################################
# import python libraries
###############################################################
import streamlit as st
import numpy as np
import pandas as pd 
from streamlit_folium import folium_static
import folium
import rasterio

###############################################################
# page info 
###############################################################

st.set_page_config(
    page_title="Map (advanced) - Demo code",
    page_icon="🌞", 
    layout="wide",
    initial_sidebar_state="expanded", 
)

###############################################################
# Method 1 - Using local image as overlayed map image 
###############################################################

st.markdown("# Method 1 - Using local image as overlayed map image")
st.markdown("Source of the overlayed map in this sample: https://lbezone.hkust.edu.hk/bib/991013146516503412")
st.markdown("Please note that the position of the map overlay in this example are not accurate. Below is just for demo purpose, to show you the code in action only.")

with st.echo(code_location="below"):
    # Create a folium map, with the center of the map when first view/load the map and zoom in level
    map0 = folium.Map(location=[44.59, 120.98], zoom_start=5)

    # Overlay a historical map
    overlayMap = "./images/991013146516503412map.png" # image path (in this sample, the image is located inside a folder called "images" in our project folder)
    imgSrc = rasterio.open(overlayMap)
    overlayMapArray = imgSrc.read()

    img = folium.raster_layers.ImageOverlay(
        name="historical map",
        image=np.moveaxis(overlayMapArray, 0, -1),
        bounds=[(30, 120), (50, 150)],  # position that you want to put the historical map, refresh the webpage to check and refine the number by yourself
        opacity=0.7,  # opacity of the overlay map
        interactive=True,
        cross_origin=False,
        zindex=1,
    )

    img.add_to(map0)

    # Read the CSV file containing the coordinates and pop-up content
    df = pd.read_csv('./data/data-sample_map-coordinates.csv')

    # Iterate over the rows of the DataFrame
    for index, row in df.iterrows():
        # Extract the coordinates and pop-up content from each row
        lat = row['Latitude']
        lon = row['Longitude']
        popup = row['PopupContent']
        
        # Create a folium marker with the coordinates and pop-up content
        marker = folium.Marker(location=[lat, lon], popup=popup)
        
        # Add the marker to the map
        marker.add_to(map0)

    # show the map
    folium_static(map0, width=1000, height=600)


###############################################################
# Method 2 - Using online maptiler to overlay a map
###############################################################

st.markdown("# Method 2 - Using online maptile to overlay a map")
st.markdown("please wait 3-5 seconds to load the overlayed historical image")

with st.echo(code_location="below"):
    # Create a folium map, with the center of the map when first view/load the map and zoom in level
    map1 = folium.Map(location=[39.916345, 116.397155], zoom_start=14)

    # Overlay a historical map
    tile_url = 'https://mapwarper.net/maps/tile/81667/{z}/{x}/{y}.png'
    folium.TileLayer(tile_url, attr='MapTile').add_to(map1)

    # Read the CSV file containing the coordinates and pop-up content
    df = pd.read_csv('./data/data-sample_map-coordinates.csv')

    # Iterate over the rows of the DataFrame
    for index, row in df.iterrows():
        # Extract the coordinates and pop-up content from each row
        lat = row['Latitude']
        lon = row['Longitude']
        popup = row['PopupContent']
        
        # Create a folium marker with the coordinates and pop-up content
        marker = folium.Marker(location=[lat, lon], popup=popup)
        
        # Add the marker to the map
        marker.add_to(map1)

    # Display the map in Streamlit
    folium_static(map1)

