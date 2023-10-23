import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)

root = tk.Tk()
root.title("ToDo List") #само окно

root.configure(bg='blue') #цвет фона

listbox = tk.Listbox(root)
listbox.pack(pady=10) #сам список задач

listbox.configure(font=('Helvetica', 12), fg='purple') #меняю шрифт и цвет текста.

entry = tk.Entry(root)
entry.pack() #для ввода задачи

add_button = tk.Button(root, text="Добавить задачу", command=add_task)
add_button.pack() #кнопка которая добавляет задачу

remove_button = tk.Button(root, text="Удалить задачу", command=remove_task)
remove_button.pack() #кнопка для удаления задачи

root.mainloop() #запуск
