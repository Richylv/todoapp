import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo']
    todos.append('\n' + todo)
    functions.write_todos(todos)
    print(todo)


st.title('My to Do app')
st.subheader('this is my to do app')
st.write('this is an app to increase productibity')

for index, todo in enumerate(todos):
    check_box = st.checkbox(todo,key=todo)
    if check_box:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input('Enter a to Do', on_change=add_todo, key='new_todo')

#st.session_state
