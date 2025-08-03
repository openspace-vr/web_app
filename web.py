import streamlit as st
from streamlit import checkbox

from modules import functions

todos = functions.get_todos()

def add_todo():
    new_todo = st.session_state["activity"]
    todos.append(new_todo)
    functions.cursor_position()
    functions.write_todos(todos)
    #print(todo)

st.title('My Web App')
st.subheader('Todos List')
st.write('Create a checklist of activities')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key= todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a new To Do", placeholder="Add activity",
              on_change=add_todo, key="activity")

#print("testing")
#session state type which is a string similar to a dictionary
#st.session_state

