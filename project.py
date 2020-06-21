import streamlit as st
import pandas as pd
import numpy as np


#- Title
st.write('## Random Line Chart')

data = pd.DataFrame(
	np.random.randn(20, 3),
	columns=['a', 'b', 'c'])

st.write('### var experiments')
x = st.slider('x')
st.write(x, 'squared is', x * x)

select = st.selectbox('Filter to:', ['car', 'truck'])
st.write('selected:', select)

#progress_bar = st.sidebar.progress(100)
#status_text = st.sidebar.empty()

st.write('### st.line_chart')
chart = st.line_chart(data=data)

st.write('### st.write')
st.write(np.transpose(data))

st.write('### st.area_chart')
st.area_chart(data)

st.write('### st.bar_chart')
st.bar_chart(data)

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")