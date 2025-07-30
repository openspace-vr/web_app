import streamlit as st
from modules import functions

todos = functions.get_todos()

def add_todo():
    new_todo = st.session_state["activity"]
    todos.append(new_todo)
    #functions.cursor_position()
    functions.write_todos(todos)
    #print(todo)




st.title('My Web App')
st.subheader('Todos List')
st.write('Create a checklist of activities')

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a new To Do", placeholder="Add activity",
              on_change=add_todo, key="activity")

