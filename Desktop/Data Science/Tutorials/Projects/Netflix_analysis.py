"""
streamlit project / Netflix price and subscription fee data from kaggle

input data paths
/Users/ootakouichi/Desktop/Data Science/Tutorials/Projects/Netflix subscription fee Dec-2021.csv
/Users/ootakouichi/Desktop/Data Science/Tutorials/Projects/netflix price in different countries.csv

"""

import streamlit as st
import numpy as np
import pandas as pd

d_sub = pd.read_csv('/Users/ootakouichi/Desktop/Data Science/Tutorials/Projects/Netflix subscription fee Dec-2021.csv')
d_p = pd.read_csv('/Users/ootakouichi/Desktop/Data Science/Tutorials/Projects/netflix price in different countries.csv')

from PIL import Image
image = Image.open('/Users/ootakouichi/Desktop/Data Science/Tutorials/Projects/netflix.png')

st.image(image, width=500)
#use_column_width="auto",

st.title('Price Analysis on Netflix')
st.header('~difference in subscription fee based on countries~')

df_p = pd.DataFrame(d_p)

#static table of price data
st.table(df_p.style.highlight_max())

#show in a metirc
col1, col2, col3 = st.columns(3)
col1.metric("Total Library Size", "Czechia", delta="7325", delta_color="normal")
col2.metric("No. of TV Shows", "Czechia", "5234")
col3.metric("No. of Movies", "Malaysia", "2387")
col4, col5, col6 = st.columns(3)
col4.metric("Cost Per Month - Basic ($)", "Liechtenstein", "12.880")
col5.metric("Cost Per Month - Standard ($)", "Liechtenstein", "20.460")
col6.metric("Cost Per Month - Premium ($)", "Liechtenstein", "26.960")


