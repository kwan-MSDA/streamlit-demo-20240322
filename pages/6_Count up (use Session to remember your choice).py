###############################################################
# import python libraries
###############################################################
import streamlit as st

###############################################################
# page info 
###############################################################

st.set_page_config(
    page_title="Count up (use Session to remember your choice) - Demo class | 2024-03-22 HUMA5630 Digital Humanities",
    page_icon="🌞", 
    layout="wide",
    initial_sidebar_state="expanded", 
)

###############################################################
# page content
###############################################################

'''
# Count up (use Session to remember your choice)
https://docs.streamlit.io/library/advanced-features/session-state
'''


###############################################################
# Method 1
###############################################################

'''## Method 1 (cannot remember your choice ☹️)'''

count_m1 = 0

increment_m1 = st.button('Increment_m1')
if increment_m1:
    count_m1 += 1

st.write('Count = ', count_m1)

st.code("""
count_m1 = 0

increment_m1 = st.button('Increment_m1')
if increment_m1:
    count_m1 += 1

st.write('Count = ', count_m1)
        """)

###############################################################
# Method 2
###############################################################

'''## Method 2 (ok! 👍)'''

if 'count_m2' not in st.session_state:
    st.session_state.count_m2 = 0

increment = st.button('Increment_m2')
if increment:
    st.session_state.count_m2 += 1

st.write('Count = ', st.session_state.count_m2)

st.code("""
if 'count_m2' not in st.session_state:
    st.session_state.count_m2 = 0

increment = st.button('Increment_m2')
if increment:
    st.session_state.count_m2 += 1

st.write('Count = ', st.session_state.count_m2)
        """)

###############################################################
# Method 3
###############################################################

'''## Method 3 (Use function 👍)'''

if 'count_m3' not in st.session_state:
    st.session_state.count_m3 = 0

def increment_counter():
    st.session_state.count_m3 += 1

st.button('Increment_m3', on_click=increment_counter)

st.write('Count = ', st.session_state.count_m3)

st.code("""
if 'count_m3' not in st.session_state:
    st.session_state.count_m3 = 0

def increment_counter():
    st.session_state.count_m3 += 1

st.button('Increment_m3', on_click=increment_counter)

st.write('Count = ', st.session_state.count_m3)
        """)
