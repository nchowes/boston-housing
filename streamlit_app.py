"""
# My first app
Here's our first attempt at using streamlit:
"""

import streamlit as st
import pandas as pd

@st.cache
def load_and_prepare():

    # Read data 
    df = pd.read_csv("housingData2014prepared.csv")

    # Reorder 
    df = df.reindex(columns=["Town", "pr2013", "pr2012", "pr2008", "pr2003", "pc1y", "pc5y", "pc10y", "dm2013", "dm2012", "dc1y"])

    # Display names 
    df = df.rename(columns={
        "pr2013": "2013 Price",    
        "pr2012": "2012 Price",   
        "pr2008": "2008 Price",    
        "pr2003": "2003 Price",    
        "pc1y": "1Yr Change",      
        "pc5y": "5Yr Change",     
        "pc10y": "10Yr Change",       
        "dm2013": "2013 Days on Market",  
        "dm2012": "2012 Days on Market",  
        "dc1y": "1Yr DOM Change",    
    })

    return df

# Load data 
df = load_and_prepare()

# Layout app 

# Title
st.title('Metro Boston housing market')
st.subheader('Single family home prices')

# Table
st.write(df)

st.subheader('By Town')

# Selectbox
option = st.selectbox(
    'Which town would you like to see?',
     df["Town"])

#By Town
df2 = df.set_index("Town", inplace = False)

st.bar_chart( 
    df2.loc[[option],["2013 Price", "2012 Price", "2008 Price", "2003 Price"]].T[option]
     )


