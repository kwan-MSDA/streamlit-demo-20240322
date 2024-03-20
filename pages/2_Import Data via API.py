###############################################################
# import python libraries
###############################################################
import streamlit as st
import pandas as pd
import requests
import xml.etree.ElementTree as ET
import streamlit.components.v1 as components

###############################################################
# page info 
###############################################################

st.set_page_config(
    page_title="Import data via request url - Demo class | 2024-03-22 HUMA5630 Digital Humanities",
    page_icon="🌞", 
    layout="wide",
    initial_sidebar_state="expanded", 
)

###############################################################
# page content
###############################################################

st.title("Example of extracting data from API")

"""
XML content from here: https://lbezone.hkust.edu.hk/rse/OAI/Server.php?verb=ListRecords&metadataPrefix=oai_dc&set=western_collection
"""

###############################################################
# Request data
###############################################################

# Send a GET request to the URL and retrieve the XML content
#https://lbezone.hkust.edu.hk/rse/western-collection

url = "https://lbezone.hkust.edu.hk/rse/OAI/Server.php?verb=ListRecords&metadataPrefix=oai_dc&set=western_collection"
response = requests.get(url)
response.encoding = 'utf-8'
xml_content = response.content

# Parse the XML content
root = ET.fromstring(xml_content)

# Create lists to store the extracted information
titles = []
dates = []
languages = []
urls = []
thumb_urls =[]

# Iterate over each record and extract the desired information
for record in root.findall(".//{http://www.openarchives.org/OAI/2.0/}record"):
    title = record.find(".//{http://purl.org/dc/elements/1.1/}title").text
    date = record.find(".//{http://purl.org/dc/elements/1.1/}date").text
    lang = record.find(".//{http://purl.org/dc/elements/1.1/}language").text

    titles.append(title)
    dates.append(date)
    languages.append(lang)

    identifiers = record.findall('.//{http://purl.org/dc/elements/1.1/}identifier')
    thumb_url = identifiers[1].text
    thumb_urls.append(thumb_url)

    doi_url = identifiers[4].text
    urls.append(doi_url)

# Create a dataframe from the extracted information
data = {
    "Title": titles,
    "Year": dates,
    "Language": languages,
    "URL": urls,
    "Thumbnail image": thumb_urls
}

st.dataframe(data, hide_index=True)

###############################################################
# More info
###############################################################

"""
#
#
# Possible data from [HKUST Library's Rare & Special e-Zone](https://lbezone.hkust.edu.hk/rse/)!
"""

###############################################################
# Radio button options for selection
###############################################################
col1, col2 = st.columns([1, 3])

with col1:
    rseColls = [
        ("antique_maps", "Antique Maps of China"),
        ("ancient_east_asian_maps", "Ancient East Asian Maps"),
        ("maps_china_late_qing", "Maps of China, Late Qing Dynasty-1949"),
        ("rare_books", "Rare Books on History of Science"),
        ("james_lee", "James Lee Collection"),
        ("paul_soong", "Paul Lin and Soong Ching-ling Correspondence"),
        ("shafei", "Sha Fei Photographic Collection"),
        ("thread_bounds", "Chinese books before 1949 (Thread Bound)"),
        ("artwork", "HKUST Library Artwork"),
        ("posters", "HKUST Posters"),
        ("chinese_collection", "Chinese books before 1949"),
        ("western_collection", "Western books about China before 1949")
    ]

    coll = st.radio(
        "Select a collection to get its OAI url: ",
        [right for _, right in rseColls],
        index=None
    )

    selected_coll = next(left for left, right in rseColls if right == coll) if coll else rseColls[11][0]

with col2:
    c = st.container(border=True, height=350)
    c.markdown("#")
    c.markdown("#")
    c.markdown(f" ### OAI url: https://lbezone.hkust.edu.hk/rse/OAI/Server.php?verb=ListRecords&metadataPrefix=oai_dc&set={selected_coll}")

st.markdown("#")
st.markdown("#")


###############################################################
# Embed HTML
###############################################################
components.html("""
<iframe loading="lazy" style="position: absolute; width: 100%; height: 100%; top: 0; left: 0; border: none; padding: 0; margin: 0;"
src="https://www.canva.com/design/DAF9OL_Atz4/oFSRCl8fZQuV4z65LYMNWA/view?embed#20" allowfullscreen="allowfullscreen" allow="fullscreen">
</iframe>
""", height = 800)
