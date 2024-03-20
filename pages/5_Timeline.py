###############################################################
# import python libraries
###############################################################
import streamlit as st
from streamlit_timeline import st_timeline #pip install streamlit-vis-timeline
import streamlit.components.v1 as components

###############################################################
# page info 
###############################################################

st.set_page_config(
    page_title="Timeline - Demo class | 2024-03-22 HUMA5630 Digital Humanities",
    page_icon="🌞", 
    layout="wide",
    initial_sidebar_state="expanded", 
)

###############################################################
# Timeline 1
# https://discuss.streamlit.io/t/new-component-streamlit-timeline-creating-beautiful-timelines-with-bi-directional-communication/31804
###############################################################

'''
# Timeline (Method 1)
Info from: https://registry.hkust.edu.hk/calendar_dates/dates23-24confirmed.pdf
'''

items = [
    {"id": 1, "content": "Spring Term commences", "start": "2024-01-31"},
    {"id": 2, "content": "Lasy day of Spring Term classes", "start": "2024-05-10"},
    {"id": 3, "content": "Last day of Spring Term", "start": "2024-05-29"},
]

timeline = st_timeline(items, groups=[], options={}, height="300px")

st.code("""
import streamlit as st
from streamlit_timeline import st_timeline #pip install streamlit-vis-timeline
        
items = [
    {"id": 1, "content": "Spring Term commences", "start": "2024-01-31"},
    {"id": 2, "content": "Lasy day of Spring Term classes", "start": "2024-05-10"},
    {"id": 3, "content": "Last day of Spring Term", "start": "2024-05-29"},
]

timeline = st_timeline(items, groups=[], options={}, height="300px")      
""")

###############################################################
# Timeline 2
# https://timeline.knightlab.com/
###############################################################
'''
---
# Timeline (Method 2)
'''

components.html("""

    <iframe src='https://cdn.knightlab.com/libs/timeline3/latest/embed/index.html?source=1O7a3ZfcviR21p5ryCp-ODm-2EmujIlNqhDb7HR2o-6I&font=Default&lang=en&initial_zoom=2&height=650' width='100%' height='650' webkitallowfullscreen mozallowfullscreen allowfullscreen frameborder='0'></iframe>

    """, 
    height=800)



###############################################################
# guide for Timeline 2
###############################################################
'''
## Detailed instructions from the official site
https://timeline.knightlab.com/#make

## Below is a quick guide
1. Make a copy of this Google Spreadsheet template to your Google Drive: https://docs.google.com/spreadsheets/d/1O7a3ZfcviR21p5ryCp-ODm-2EmujIlNqhDb7HR2o-6I/
'''
'''2. Click "File" → "Share" → "Publish to web"  '''
st.image("images/timelineJS3_1.jpg")

'''3. Click "Publish"  '''
st.image("images/timelineJS3_2.jpg")

'''4. Copy the ID in the URL in your own Google Spreadsheet '''
st.image("images/timelineJS3_3.jpg")


st.markdown("#")

gsheetID = st.text_input('Your Google Sheet ID', '1O7a3ZfcviR21p5ryCp-ODm-2EmujIlNqhDb7HR2o-6I')
if st.button("Re-generate the embed code"):
    st.code(f"<iframe src='https://cdn.knightlab.com/libs/timeline3/latest/embed/index.html?source={gsheetID}&font=Default&lang=en&initial_zoom=2&height=650' width='100%' height='650' webkitallowfullscreen mozallowfullscreen allowfullscreen frameborder='0'></iframe>")
else:
    st.code(f"<iframe src='https://cdn.knightlab.com/libs/timeline3/latest/embed/index.html?source={gsheetID}&font=Default&lang=en&initial_zoom=2&height=650' width='100%' height='650' webkitallowfullscreen mozallowfullscreen allowfullscreen frameborder='0'></iframe>")



###############################################################
# code template
###############################################################
codedemo = '''
components.html("""

    <paste the embed code here>

    """, 
    height=800)
'''

st.code(codedemo, language='python')
