import streamlit as st

from modules import functions

todos = functions.get_todos()

def add_todo():
    #functions check the position of cursor
    # and add activities
    new_todo = st.session_state["activity"]
    todos.append(new_todo)
    functions.cursor_position()
    functions.write_todos(todos)


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