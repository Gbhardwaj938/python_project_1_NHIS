import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("400x420")
root.resizable(False, False)

# Entry field
equation = tk.StringVar()
entry = tk.Entry(
    root,
    textvariable=equation,
    font=("Arial", 22),
    bd=10,
    relief=tk.RIDGE,
    justify="right"
)
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# Functions
def press(value):
    equation.set(equation.get() + str(value))

def clear():
    equation.set("")

def calculate():
    try:
        result = eval(equation.get())
        equation.set(result)
    except:
        equation.set("Error")

# Buttons layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

frame = tk.Frame(root)
frame.pack()

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(frame, text=text, width=6, height=2,
                        font=("Arial", 14),
                        command=calculate)
    elif text == "C":
        btn = tk.Button(frame, text=text, width=6, height=2,
                        font=("Arial", 14),
                        command=clear)
    else:
        btn = tk.Button(frame, text=text, width=6, height=2,
                        font=("Arial", 14),
                        command=lambda t=text: press(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Run application
root.mainloop()
