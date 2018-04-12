import tkinter
from tkinter import ttk
import random

# Creating button
# root = tkinter.Tk()
# ttk.Button(root, text="Hello Kiryha").grid()
# root.mainloop()

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

# To do list, with default tasks
tasks = ['Read CS book for 30 minutes', 'Self-development', 'Practise coding', 'Plan my next day']

# Creating functions
def update_listbox():
    # Clear current list
    clear_listbox()
    for task in tasks:
        lb_tasks.insert('end',task)

def clear_listbox():
    lb_tasks.delete(0, 'end')

def add_task():
    # Get a task frob text_input
    task = text_input.get()
    # Append it to the list
    tasks.append(task)
    # Update the listbox
    update_listbox()

def delete_all():
    # we are deleting globally
    global tasks
    # Clear the tasks
    tasks = []
    # Update the listbox
    update_listbox()

def delete_one():
    # Delete currently selected method
    task = lb_tasks.get('active')
    if task in tasks:
        tasks.remove(task)
    # Update the listbox
    update_listbox()

def sort_asc():
    tasks.sort()
    # Update the listbox
    update_listbox()

def sort_desc():
    tasks.sort(reverse=True)
    # Update the listbox
    update_listbox()

def choose_rand():
    task = random.choice(tasks)
    # Display the choosed label from tasks
    lbl_dislpay['text'] = task

def num_of_tasks():
    number_of_tasks = len(tasks)
    msg = 'Number of tasks: %s' %number_of_tasks
    lbl_dislpay['text'] = msg

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