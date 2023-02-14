import streamlit
import FileUtilFunctions as fuf

todos = fuf.gettodos("todos.txt")


def add():
    todo = streamlit.session_state["newtodo"]
    todos.append(todo+"\n")
    fuf.writetodos(fname="todos.txt", todos=todos)
    streamlit.session_state["newtodo"] = ""


def complete():
    sessionstate = streamlit.session_state
    items = sessionstate.items()
    for item in items:
        if item[0].startswith("todo_checkbox_"):
           if bool(item[1]):
               key = (item[0].split("_"))[2]
               del todos[int(key)]
               del sessionstate[f"{item[0]}"]
    fuf.writetodos(fname="todos.txt", todos=todos)


streamlit.title("Todolist web app")

streamlit.subheader("Todo list items...")

for ind,todo in enumerate(todos):
    streamlit.checkbox(todo, key=f"todo_checkbox_{ind}")

streamlit.text_input(key="newtodo", placeholder="enter...", label="Add new todo")

streamlit.button(key="add", on_click=add, label="Add")

streamlit.button(key="complete", on_click=complete, label="Complete")


