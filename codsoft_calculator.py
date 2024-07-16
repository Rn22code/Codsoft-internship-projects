import tkinter as tk


def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif text == "C":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, text)


root = tk.Tk()
root.title("Attractive Calculator")
root.geometry("400x600")  
root.configure(bg="#333333")  


display = tk.Entry(root, font="Arial 24", bd=10, insertwidth=5, width=14, borderwidth=5, justify='right', bg="white")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


button_style = {
    "font": ("Arial", 18),
    "bd": 1,
    "relief": "ridge",
    "width": 4,
    "height": 2,
    "bg": "#4CAF50",
    "fg": "#ffffff",
    "activebackground": "#45a049",
    "activeforeground": "#ffffff"
}


button_special_style = {
    "bg": "#f44336",
    "activebackground": "#d32f2f"
}

button_equal_style = {
    "bg": "#2196F3",
    "activebackground": "#1976D2"
}


buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]


row_val = 1
col_val = 0
for button in buttons:
    btn_style = button_style.copy()  
    if button == "C":
        btn_style.update(button_special_style)
    elif button == "=":
        btn_style.update(button_equal_style)
    b = tk.Button(root, text=button, **btn_style)
    b.grid(row=row_val, column=col_val, padx=5, pady=5)
    b.bind("<Button-1>", click)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
