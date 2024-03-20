###############################################################
# import python libraries
###############################################################
import streamlit as st
import pandas as pd
import plotly.express as px

###############################################################
# page info 
###############################################################

st.set_page_config(
    page_title="Analysis and Display - Demo class | 2024-03-22 HUMA5630 Digital Humanities",
    page_icon="🌞", 
    layout="wide",
    initial_sidebar_state="expanded", 
)

###############################################################
# page content
###############################################################

st.title("Play around with the data with your creativity!")
st.markdown("https://lbezone.hkust.edu.hk/rse/western-collection")


###############################################################
# Data
###############################################################
filepath = 'data/data_rse-western-collection.xlsx'
data = pd.read_excel(filepath, sheet_name='data')


###############################################################
# Select and filter
###############################################################

st.markdown("## Select and Filter")

# Create a multi-select widget with the unique languages as options
unique_languages = data['Language'].unique()
selected_languages = st.multiselect(
    'Select Languages:',
    unique_languages,
    default=[] 
)

# Filter the DataFrame based on the selected languages
if selected_languages:
    data1 = data[data['Language'].isin(selected_languages)]
    st.dataframe(data1, hide_index=True)
else:
    st.dataframe(data, hide_index=True)


###############################################################
# Count
###############################################################
st.markdown("---")
st.markdown("## Total number of books in this collection")

booknum = len(data)
st.metric(label="No. of books", value=booknum)
st.write(f'There are a total of {booknum} books in this collection online as of 19 March 2024.')


###############################################################
# Chart
###############################################################
st.markdown("## Chart")

# Count the occurrences of each language
language_counts = data['Language'].value_counts()

# Create a DataFrame from the counts
df_languages = pd.DataFrame({'Language': language_counts.index, 'Count': language_counts.values})

# Create a pie chart using Plotly Express
fig = px.pie(df_languages, values='Count', names='Language', title='Distribution of Languages')

# Display the pie chart in Streamlit
st.plotly_chart(fig)


st.markdown("---")


###############################################################
# Make use of "for loop"
###############################################################

st.markdown("## Using `for loop` to display thumbnails like catalog/gallery")


# Display thumbnail images with titles and URLs
colnum = 6
for i in range(0, len(data), colnum):
    row = data.iloc[i:i+colnum]

    columns = st.columns(colnum)
    for index, row in row.iterrows():
        title = row["Title"]
        year = row["Year"]
        lang = row["Language"]
        url = row["URL"]
        image = row["Thumbnail image"]

        with columns[index % colnum]:
            st.image(image, caption=f"Year: {year} | {lang}")
            with st.expander("Title"):
                st.write(title)
            st.write(url)
            st.markdown("---")

