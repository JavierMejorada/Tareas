import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación de Lista de Tareas")
        
        self.tasks = []
        
        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.pack(pady=10)
        
        self.add_button = tk.Button(self.root, text="Añadir Tarea", width=20, command=self.add_task)
        self.add_button.pack(pady=5)
        
        self.task_listbox = tk.Listbox(self.root, height=10, width=50, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)
        
        self.delete_button = tk.Button(self.root, text="Eliminar Tarea", width=20, command=self.delete_task)
        self.delete_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Debe ingresar una tarea.")
    
    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Advertencia", "Debe seleccionar una tarea para eliminar.")
    
    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
