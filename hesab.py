import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")

        self.entry = tk.Entry(master, width=30, borderwidth=5, font=('Arial', 16))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('**', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('=', 5, 1, 1, 3)
        ]

        for btn in buttons:
            text = btn[0]
            row = btn[1]
            col = btn[2]
            rowspan = btn[3] if len(btn) > 3 else 1
            colspan = btn[4] if len(btn) > 4 else 1

            b = tk.Button(self.master, text=text, padx=20, pady=20,
                          font=('Arial', 14), command=lambda t=text: self.on_click(t))
            b.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, sticky="nsew")

    def on_click(self, button):
        if button == 'C':
            self.entry.delete(0, tk.END)
        elif button == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except ZeroDivisionError:
                messagebox.showerror("Error", "Cannot divide by zero!")
            except Exception:
                messagebox.showerror("Error", "Invalid input!")
        else:
            self.entry.insert(tk.END, button)

# اجرای برنامه
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

