"""
All the materials including presentation slides are openly accessible in the following GitHub Repository:

https://github.com/hkust-dh/streamlit-demo-20240322

"""

###############################################################
# import python libraries
###############################################################
import streamlit as st

###############################################################
# page info 
# https://docs.streamlit.io/library/api-reference/utilities/st.set_page_config
###############################################################

##############################
### use emoji as page icon ###
##############################

st.set_page_config(
    page_title="Demo class | 2024-03-22 HUMA5630 Digital Humanities",
    page_icon="🌞", # https://emojicopy.com/
    layout="wide",
    initial_sidebar_state="expanded", # "auto", "expanded", or "collapsed"
)


##################################
### use image URL as page icon ###
##################################

# st.set_page_config(
#     page_title="Demo class | 2024-03-22 HUMA5630 Digital Humanities",
#     page_icon="https://cdn.discordapp.com/emojis/612122990338899995.png?size=64", # image source: https://blobs.gg/
# )


#################################
### use an image as page icon ###
#################################

# from PIL import Image
# custom_icon = Image.open("favicon.ico") # Favicon Generators https://favicon.io/
# st.set_page_config(
#     page_title="Demo class | 2024-03-22 HUMA5630 Digital Humanities",
#     page_icon=custom_icon,
#     }
# )

###############################################################
# page content
###############################################################

st.caption("This is caption")
st.title("This is title")

###############################################################
# Use markdown
###############################################################
'''
## Welcome to this demo site!
This website serves as a demo to showcase the capabilities and functionalities of Streamlit in creating web applications. 

If you are interested in learning how this website was created, please refers to the source code in [this repo](https://github.com/hkust-dh/streamlit-demo-20240322) and [this repo](https://github.com/hkust-dh/streamlit-demo) for the detailed instructions and explanations.
'''

# some empty space
st.markdown('#')

###############################################################
# Image
###############################################################

# image at folder
st.image('images/img1.jpg', caption='https://digitalhumanities.hkust.edu.hk/learn-python-from-zero-for-absolute-beginner')

# image url
#st.image('https://digitalhumanities.hkust.edu.hk/wp-content/uploads/2023/09/20230928-DH-python_webpagePromoArea1_r.jpg')


###############################################################
# Click to expand
###############################################################

with st.expander("Click to expand"):
    st.write("""
        Click to read more:
        https://digitalhumanities.hkust.edu.hk/learn-python-from-zero-for-absolute-beginner
   """)

# some empty space
st.markdown('#')
st.markdown('#')

###############################################################
# Columns layout
###############################################################
st.markdown('# Column Layout')

col1, col2, col3 = st.columns(3)

with col1:
   st.header("this is column 1")
   c1 = st.container(border=True, height=350)
   c1.markdown("""
               Series 1:
               [Data Cleaning](https://digitalhumanities.hkust.edu.hk/tutorials/learn-python-from-zero-for-absolute-beginner-1-data-cleaning)
               """)
   c1.image("https://digitalhumanities.hkust.edu.hk/wp-content/uploads/2023/08/python-groupby-count-1.png")

with col2:
   st.header("this is column 2")
   c2 = st.container(border=True, height=350)
   c2.markdown("""
               Series 2:
               [Data Visualization](https://digitalhumanities.hkust.edu.hk/tutorials/learn-python-from-zero-for-absolute-beginner-2-data-visualization/)
               """)
   c2.image("https://digitalhumanities.hkust.edu.hk/wp-content/uploads/2023/08/plotly_chart3.gif")

with col3:
   st.header("this is column 3")
   c3 = st.container(border=True, height=500)
   c3.markdown("""
               Series 3:
               [Create Website](https://digitalhumanities.hkust.edu.hk/tutorials/learn-python-from-zero-for-absolute-beginner-3-create-website)
               """)
   c3.image("https://digitalhumanities.hkust.edu.hk/wp-content/uploads/2023/08/streamlit-preview-online-s.gif")


# some empty space
st.markdown('#')
st.markdown('#')

###############################################################
# Tab layout
###############################################################
st.markdown('# Tab Layout')

tab1, tab2, tab3 = st.tabs(["1️⃣ 1", "2️⃣ and this is tab 2", "3️⃣ can create more tabs"])

tab1.subheader("Tab 1 content area")
tab2.subheader("Hi")
tab2.text("Here is Tab 2 content")
tab3.markdown("# Hello, this is tab 3")

###############################################################
# Some more styles
###############################################################

st.markdown('#')
st.markdown('#')
st.markdown('# Status box')

st.success('Success')
st.info('Info')
st.warning('Warning')
st.error('Error', icon='⚠️')