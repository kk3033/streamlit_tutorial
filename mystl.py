"""
Here's how to turn the display to streamlit browser
'command + O' will let you choose and set the PATH you wanna have a proximity
then 'sreamlit run file.py will activate the localhost browser

copy this code below to the bash terminal
streamlit run mystl.py    <--- copy & paste it

"""

import streamlit as st
import pandas as pd
# import yfinance as yf

st.title('Streamlit Tutorial')
st.write('contents')

"""
## progress bar
"""
import time
st.write('progress bar')
"start"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

"Completed"

df = pd.DataFrame({
    'column1':[1,2,3,4,5],
    'column2':['A','B','C','D','E']
})

st.write(df)

st.write('DataFrame')
st.dataframe(df.style.highlight_max(axis=0), width=500, height=400)
st.write('Table')
st.table(df) # static table 

# magic command

"""
Magic Commands
# Title
## Chapter
### Topic

```python
import streamlit as st
import pandas as pd
st.write(df)
```

"""
"""
## Chart dipiction
"""
import numpy as np

df2 = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)
st.write('line_chart')
st.line_chart(df2)
st.write('area_chart')
st.area_chart(df2)
st.write('bar_chart')
st.bar_chart(df2)

"""
## map plotting
"""

df3 = pd.DataFrame(
    np.random.rand(30,2)/[50,50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
st.map(df3)

"""
## display image when checkbox is True
"""
from PIL import Image
if st.checkbox('show image'):
    img = Image.open('/Users/ootakouichi/Desktop/Data Science/Lecture materials/Streamlit tutorials/Btfly.jpeg')
    st.image(img, caption='Butterfly', use_column_width=True)

"""
## selectbox
"""
option = st.selectbox(
    'choose any number you like',
    list(range(1,11))
)
'The number you chose --->', option

"""
## interactive widgets
### text input
# """

text = st.text_input('enter your username here')
'Your username is:', text

"""
### slider widget
### The dynamic value can be selected using this slider widget
"""
condition = st.slider('How well are you feeling good?',0,100,0)
'How are you?',condition

"""
## sidebar
"""
st.sidebar.write('Sidebar widgets below')
st.sidebar.write('whatever here')

"""
## 2-columns layout
"""
left_col, right_col = st.columns(2)  
# since 2021-11, 'st.beta_columns' will no longer be supported
# updated to st.columns 
button = left_col.button('Press this button')
if button:
    right_col.write('This is the right column')

"""
## expander widget
"""
# st.beta_expander will be no longer supported, and instead
# st.expander will be replaced into this function 
expander1 = st.expander('Question1')
expander1.write('Answer to Q1')
expander2 = st.expander('Question2')
expander2.write('Ansewer to Q2')
expander3 = st.expander('Question3')
expander3.write('Answer to Q3')

