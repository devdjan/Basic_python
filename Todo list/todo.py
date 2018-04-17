import tkinter
import random

# Creating root window
root = tkinter.Tk()

# Change the background
root.configure(bg='white')

# Title of the GUI
root.title('Everyday To Do List!')

# Change the size of the window
root.geometry('200x450')

# What to do
tasks = []

# For future i can chage the display of the To do list
# By using .grid()
# Divide "All" like two dimensional matrix
# And not use .pack() but use grid(row = 0, column=1 or 0 or 2)

# Creating functions
def update_listbox():
    # Clear current state of list
    clear_listbox()
    # Insert to the end of the list
    for task in tasks:
        lb_tasks.insert('end', task)

def clear_listbox():
    lb_tasks.delete(0, 'end')

def add_task():
    # Read and get task from the text_input
    task = text_input.get()
    if task != "":
        # Append it to the list
        tasks.append(task)
        # And update the listbox
        update_listbox()
    else:
        lbl_dislpay['text'] = 'Please enter the task'
    text_input.delete(0, 'end')

def delete_all():
    # delete all tasks globally (glbl variable)
    global tasks
    # then we clear the list
    tasks = []
    # And update the listbox
    update_listbox()


def delete_one():
    # Deliting selected task in Tasks list
    task = lb_tasks.get('active')
    if task in tasks:
        tasks.remove(task)
    # And update the listbox
    update_listbox()

def sort_asc():
    tasks.sort()
    # And update the listbox
    update_listbox()


def sort_desc():
    tasks.sort(reverse=True)
    # And update the listbox
    update_listbox()

def choose_rand():
    # get random task from tasks, using random
    task = random.choice(tasks)
    lbl_dislpay['text'] = task


def num_of_tasks():
    number_of_tasks = len(tasks)
    msg = 'The number of tasks: %s' %number_of_tasks
    lbl_dislpay['text'] = msg

# Labels and Buttons
lbl_title = tkinter.Label(root, text="What do you want to do ?")
lbl_title.pack()

lbl_dislpay = tkinter.Label(root, text="")
lbl_dislpay.pack()

text_input = tkinter.Entry(root, width=20)
text_input.pack()

btn_add_task = tkinter.Button(root, text='Add Task', fg="blue", bg="white", width=20, command = add_task)
btn_add_task.pack()

btn_delete_all = tkinter.Button(root, text='Delete all tasks', fg='blue', bg='white', width=20, command=delete_all)
btn_delete_all.pack()

btn_delete_one = tkinter.Button(root, text='Delete task', fg='blue', bg='white', width=20, command=delete_one)
btn_delete_one.pack()

btn_sort_asc = tkinter.Button(root, text='Sort tasks (ASC)', fg='blue', bg='white', width=20, command=sort_asc)
btn_sort_asc.pack()

btn_sort_desc = tkinter.Button(root, text='Sort tasks (DESC)', fg='blue', bg='white', width=20, command=sort_desc)
btn_sort_desc.pack()

btn_choose_rand = tkinter.Button(root, text='Choose random', fg='blue', bg='white', width=20, command=choose_rand)
btn_choose_rand.pack()

btn_num_of_tasks = tkinter.Button(root, text='Number of tasks', fg='blue', bg='white', width=20, command=num_of_tasks)
btn_num_of_tasks.pack()

btn_exit = tkinter.Button(root, text='Exit', fg='blue', bg='white', width=20, command=exit)
btn_exit.pack()

lb_tasks = tkinter.Listbox(root)
lb_tasks.pack()
# Starting executing code (printing out the label etc.)
root.mainloop()