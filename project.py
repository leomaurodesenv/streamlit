import streamlit as st
import pandas as pd
import numpy as np
import pandas as pd

import time

#- Title
st.write('## Random Line Chart')

data = pd.DataFrame(
	np.random.randn(20, 3),
	columns=['a', 'b', 'c'])

#progress_bar = st.sidebar.progress(100)
#status_text = st.sidebar.empty()

st.write('### st.line_chart')
size = st.slider('width', 0, 100, 17)
chart = st.line_chart(data=data, width=size)

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