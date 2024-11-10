import tkinter as tk

started_orders = []
completed_orders = []

def update_orders():
    with open("order.txt", "r") as f:
        orders = f.readlines()

    orders_display.config(text="\n".join(orders))

    canvas.config(scrollregion=canvas.bbox("all"))

    root.after(2000, update_orders)

root = tk.Tk()
root.title("Vizualizare Comenzi")

label = tk.Label(root, text="Order:")
label.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

entered_order = ""

def complete_order():
    global entered_order
    entered_order = entry.get()
    with open("completed_orders.txt", "a") as f:
        f.write(entered_order + "\n")

    file_name = "started_orders.txt"
    value_to_remove = entered_order

    with open(file_name, "r") as file:
        lines = file.readlines()

    with open(file_name, "w") as file:
        for line in lines:
            if value_to_remove not in line:
                file.write(line)

def order_received():
    global entered_order
    entered_order = entry.get()

    file_name = "completed_orders.txt"
    value_to_remove = entered_order

    with open(file_name, "r") as file:
        lines = file.readlines()

    with open(file_name, "w") as file:
        for line in lines:
            if value_to_remove not in line:
                file.write(line)

canvas = tk.Canvas(root)
canvas.pack(pady=10, side="left", fill="both", expand=True)

frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.config(yscrollcommand=scrollbar.set)

orders_display = tk.Label(frame, text="", justify="left", font=("Arial", 10))
orders_display.pack(pady=1)

def update_orders():
    with open("order.txt", "r") as f:
        orders = f.readlines()

    orders_display.config(text="\n".join(orders))

    canvas.config(scrollregion=canvas.bbox("all"))

    root.after(2000, update_orders)

update_orders()
def clear_screen():
    with open("order.txt","w") as f:
        f.write("")

submit_button = tk.Button(root, text="Complete Order", command=complete_order)
submit_button.pack(pady=10)

submit_button = tk.Button(root, text="Order received", command=order_received)
submit_button.pack(pady=10)

submit_button = tk.Button(root, text="Clear Screen", command=clear_screen)
submit_button.pack(pady=10)
root.mainloop()
