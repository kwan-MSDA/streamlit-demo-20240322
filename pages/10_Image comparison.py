###############################################################
# import python libraries
###############################################################
import streamlit as st
from streamlit_image_comparison import image_comparison

###############################################################
# page info 
###############################################################

st.set_page_config(
    page_title="Image comparison - Demo code",
    page_icon="🌞", 
    layout="wide",
    initial_sidebar_state="expanded", 
)

###############################################################
# page content
###############################################################

st.markdown("# Streamlit Image Comparison Component")
st.markdown("https://pypi.org/project/streamlit-image-comparison/")

st.markdown("Possible use example:")

with st.echo(code_location="below"):
    import streamlit as st
    from streamlit_image_comparison import image_comparison
    
    image_comparison(
        img1="./images/sanbao-l.png", # local image 1
        img2="./images/sanbao-r.png", # local image 2
        label1="historical map",  
        label2="modern map",
        width=1100,
        starting_position=50,
        show_labels=True,
        make_responsive=True,
        in_memory=True,
    )


