###############################################################
# import python libraries
###############################################################
import streamlit as st
import pandas as pd

###############################################################
# page info 
###############################################################

st.set_page_config(
    page_title="Import data - Demo class | 2024-03-22 HUMA5630 Digital Humanities",
    page_icon="🌞", 
    layout="wide",
    initial_sidebar_state="expanded", 
)

###############################################################
# page content
###############################################################

st.title("Read Excel data from your own folder")

###############################################################
# Display code
###############################################################
st.code("""
filepath = 'data/data_rse-western-collection.xlsx'
data = pd.read_excel(filepath, sheet_name='data')
st.dataframe(data, hide_index=True)
        """)

###############################################################
# read Excel file data 
###############################################################
filepath = 'data/data_rse-western-collection.xlsx'
data = pd.read_excel(filepath, sheet_name='data')


###############################################################
# Display as dataframe 
###############################################################
st.dataframe(data, hide_index=True)

