import tkinter as tk

def on_click(event):
    current_text = entry.get()
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

def create_button(text, row, col, col_span=1):
    button = tk.Button(root, text=text, font=("Helvetica", 18), bd=5, bg="light blue")
    button.grid(row=row, column=col, columnspan=col_span, padx=5, pady=5, sticky="nsew")
    button.bind("<Button-1>", on_click)
    return button

root = tk.Tk()
root.title("Calculator")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 500
window_height = 350

x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

root.configure(background="#FFD1DC")

heading_label = tk.Label(root, text="Calculator", font=("Helvetica", 16, "bold"), bg="#FFD1DC")
heading_label.grid(row=0, column=0, columnspan=4, pady=20)

entry = tk.Entry(root, font=("Helvetica", 24), bd=5, justify=tk.RIGHT)
entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

create_button("7", 2, 0)
create_button("8", 2, 1)
create_button("9", 2, 2)
create_button("/", 2, 3)

create_button("4", 3, 0)
create_button("5", 3, 1)
create_button("6", 3, 2)
create_button("*", 3, 3)

create_button("1", 4, 0)
create_button("2", 4, 1)
create_button("3", 4, 2)
create_button("-", 4, 3)

create_button("0", 5, 0)
create_button(".", 5, 1)
create_button("=", 5, 2)
create_button("+", 5, 3)

create_button("C", 6, 0, 3)

for i in range(7):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
