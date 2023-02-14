def gettodos(fname=''):
    with (open(fname, "r")) as flocal:
        todos_local = flocal.readlines()
        return todos_local


def writetodos(todos=[]):
    with (open("todos.txt", "w")) as flocal:
        flocal.writelines(todos)


def writetodos(fname='', todos=[]):
    with (open(fname, "w")) as flocal:
        flocal.writelines(todos)


if __name__ == "__main__":
    print("Hello from main!!!")

