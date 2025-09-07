from tkinter import *
from tkinter import ttk
import func

root = Tk()
root.title("shutdowner")
root.geometry("250x150")
root.resizable(False, False)

timer_id = None
remaining = 0 

def get_entry_value():
    try:
        return int(entry.get())
    except ValueError:
        return 0

def update_label():
    global remaining, timer_id
    if remaining > 0:
        label.config(text=f"Осталось: {remaining} сек.")
        remaining -= 1
        timer_id = root.after(1000, update_label)
    else:
        label.config(text="Выполняется...")
        if action_type == "shutdown":
            func.shutdown()
        elif action_type == "hibernate":
            func.hibernate()

def schedule_shutdown():
    global remaining, action_type, timer_id
    cancel_action()
    remaining = get_entry_value()
    action_type = "shutdown"
    update_label()

def schedule_hibernate():
    global remaining, action_type, timer_id
    cancel_action()
    remaining = get_entry_value()
    action_type = "hibernate"
    update_label()

def cancel_action():
    global timer_id, remaining
    if timer_id:
        root.after_cancel(timer_id)
        timer_id = None
    remaining = 0
    label.config(text="Отменено.")

entry = ttk.Entry()
entry.pack()

btn = ttk.Button(text="Выключение", command=schedule_shutdown)
btn.pack()

btn2 = ttk.Button(text="Гибернация", command=schedule_hibernate)
btn2.pack()

btn_cancel = ttk.Button(text="Отмена", command=cancel_action)
btn_cancel.pack()

label = ttk.Label(text="Таймер не запущен")
label.pack()

root.mainloop()
