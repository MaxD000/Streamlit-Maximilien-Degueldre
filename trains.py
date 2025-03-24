import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("Simple Interactive Visualizations")   
slider_value = st.sidebar.slider("Select a value", 0, 100, 50) 
st.write(f"Selected value: {slider_value}") 

#data import 
df = pd.read_csv('listings copy.csv')


import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Charger les données
df = pd.read_csv("listings copy.csv")

# Scatter plot
st.title("Bar chart")
fig=px.bar(df, x='room_type', y='price', title='bar chart of price according to room type')
st.plotly_chart(fig)

# Bar chart du nombre de modèles par marque
st.title("Box plot of the number of reviews")
fig=px.box(df, x='number_of_reviews')
st.plotly_chart(fig)

# Heatmap
st.title('Line chart')
fig = px.line(df, x='price', y='id', title="Ths is a line chart of the price according to the id")
st.plotly_chart(fig)
