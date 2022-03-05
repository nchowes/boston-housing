"""
# My first app
Here's our first attempt at using streamlit:
"""

import streamlit as st
import pandas as pd

@st.cache
def load_and_prepare():
    df = pd.read_csv("./data/product/housing-data-y19y21price-manual.csv")
    return df

# Load data 
df = load_and_prepare()

# Layout app 

# Title
st.title('Metro Boston Housing: 2019-2021')
st.subheader('Single family home prices')

# Table
st.write(df)

st.subheader('By City/Town')

# Selectbox
option = st.selectbox(
    'Which town would you like to see?',
     df["City/Town"])

#By Town
df2 = df.set_index("City/Town", inplace = False)

st.text('Housing price')

st.bar_chart( 
    df2.loc[[option],["2021 Price", "2020 Price", "2019 Price"]].T[option]
     )

st.text('Housing price percent change')

st.bar_chart( 
    df2.loc[[option],["2Yr %Change ('19-'21)", "1Yr %Change ('20-'21)", "1Yr %Change ('19-'20)"]].T[option]
     )
