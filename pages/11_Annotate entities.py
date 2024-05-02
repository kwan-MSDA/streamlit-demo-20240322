###############################################################
# import python libraries
###############################################################
import streamlit as st
from annotated_text import annotated_text
import re
import ast

###############################################################
# page info 
###############################################################

st.set_page_config(
    page_title="Annotate entities - Demo code",
    page_icon="🌞", 
    layout="wide",
    initial_sidebar_state="expanded", 
)

###############################################################
# page content
###############################################################

st.markdown("# Annotate Text")
st.markdown("https://github.com/tvst/st-annotated-text")

with st.echo(code_location="below"):
    import streamlit as st
    from annotated_text import annotated_text
    import re
    import ast

    text = "南山經之首曰䧿山。其首曰招搖之山，臨于西海之上，多桂，多金玉。有草焉，其狀如韭而青花，其名曰祝餘，食之不飢。有木焉，其狀如穀而黑理，其花四照，其名曰迷穀，佩之不迷。有獸焉，其狀如禺而白耳，伏行人走，其名曰狌狌，食之善走。麗𪊨之水出焉，而西流注于海，其中多育沛，佩之無瘕疾。"

    nameList = ["祝餘", "狌狌"]
    placeList = ["南山", "䧿山", "西海"]


    def highlight_name(text):
        # name
        for word in nameList:
            regex = re.compile(word)
            text = regex.sub('",("' + word + '", "name"),"', text)
        #place
        for word in placeList:
            regex = re.compile(word)
            text = regex.sub('",("' + word + '", "place"),"', text)
        return text


    highlighted_text = '"' + highlight_name(text) + '"'
    highlighted_text = ast.literal_eval(highlighted_text) # Convert string to a list
    annotated_text(*highlighted_text)
