from logging import PlaceHolder

import streamlit as st
from modules import functions

todos = functions.get_todos()


st.title('My Web App')
st.subheader('Todos List')
st.write('Create a checklist of activities')

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a new To Do", placeholder="Add activity", key="activity")

