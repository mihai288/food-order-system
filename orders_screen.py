import tkinter as tk


def update_orders():
    try:
        with open("started_orders.txt", "r") as f:
            pending_orders = f.readlines()
    except FileNotFoundError:
        pending_orders = ["No pending orders found."]

    try:
        with open("completed_orders.txt", "r") as f:
            completed_orders = f.readlines()
    except FileNotFoundError:
        completed_orders = ["No completed orders found."]

    pending_orders_text.set("Pending Orders:\n" + "".join(pending_orders))
    completed_orders_text.set("Completed Orders:\n" + "".join(completed_orders))

    root.after(3000, update_orders)

root = tk.Tk()
root.title("Order Status")

pending_orders_text = tk.StringVar()
pending_orders_label = tk.Label(root, textvariable=pending_orders_text, width=50, height=10, relief="solid",
                                anchor="nw", justify="left", padx=10, pady=10)
pending_orders_label.pack(pady=10)

completed_orders_text = tk.StringVar()
completed_orders_label = tk.Label(root, textvariable=completed_orders_text, width=50, height=10, relief="solid",
                                  anchor="nw", justify="left", padx=10, pady=10)
completed_orders_label.pack(pady=10)

update_orders()

root.mainloop()
