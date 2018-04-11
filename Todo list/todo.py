import tkinter
from tkinter import ttk
import random

# Creating button
# root = tkinter.Tk()
# ttk.Button(root, text="Hello Kiryha").grid()
# root.mainloop()

# Creating root window
root = tkinter.Tk()

# Creating functions
def add_task():
    pass

def delete_all():
    pass

def delete_one():
    pass

def sort_asc():
    pass

def sort_desc():
    pass

def choose_rand():
    pass

def num_of_tasks():
    pass

lbl_title = tkinter.Label(root, text="first labellolol")
lbl_title.pack()

lbl_dislpay = tkinter.Label(root, text="")
lbl_dislpay.pack()

lbl_input = tkinter.Entry(root, width=25)
lbl_input.pack()

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