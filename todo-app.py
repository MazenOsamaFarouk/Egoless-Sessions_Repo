# This is a todolist application that saves the todolist on a file
# instead of just on runtime

def print_choices():
    print("|"+"*"*25+"|")
    print("| 1. Add new item         |")
    print("| 2. Mark item as Done    |")
    print("| 3. Print TODO list      |")
    print("| 4. Print Done list      |")
    print("| 5. Print ALL lists      |")
    print("| q: quit application     |")

def add_item(todo_list, done_list):
    item = input("Add new item: ")
    todo_list.append(item)



while(True):    
    print_choices()