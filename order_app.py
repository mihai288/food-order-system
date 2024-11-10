import tkinter as tk
from tkinter import messagebox

order = []
order_number = 0
order_price = 0

root = tk.Tk()
root.title("Food Order")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f"{screen_width}x{screen_height}+0+0")
root.attributes("-fullscreen", False)

root.resizable(True, True)
root.configure(bg="#F8F8F8")

def update_price():
    price_label.config(text=f"Total Price: ${order_price:.2f}")
    price_label.update_idletasks()

def add_to_list(text, price):
    global order_price
    order.append((text, price))
    order_price += price
    update_order_display()
    update_price()

def update_order_display():
    for widget in order_frame_inner.winfo_children():
        widget.destroy()

    for item, _ in order:
        item_label = tk.Label(order_frame_inner, text=item, bg="#FFFFFF", font=("Helvetica", 10), anchor="w")
        item_label.pack(fill="x", padx=5, pady=2)
        item_label.bind("<Button-1>", lambda e, item=item: remove_from_list(item))

    order_frame_inner.update_idletasks()
    order_canvas.config(scrollregion=order_canvas.bbox("all"))

def remove_from_list(item):
    global order_price
    for i, (food, price) in enumerate(order):
        if food == item:
            order_price -= price
            order.pop(i)
            break
    update_order_display()
    update_price()

def submit_order():
    global order_number, order_price
    order_number += 1

    with open("order.txt", "a") as file:
        file.write(f"Order #{order_number}\n")
        for food, _ in order:
            file.write(f"-   {food}\n")
        file.write(f"=== Total: ${order_price:.2f} ===\n\n")
    messagebox.showinfo("Order Started", f"Order {order_number} | Total Price: ${order_price:.2f}")

    order.clear()
    order_price = 0
    update_order_display()
    update_price()

    with open("started_orders.txt", "a") as f:
        f.write(f"{order_number}\n")


food_dict = {
    'BBQ Bacon Cheeseburger': 9.49,
    'Spicy Chicken Sandwich': 7.99,
    'Double Cheeseburger': 8.99,
    'Veggie Burger': 7.49,
    'Pulled Pork Sandwich': 8.99,
    'Buffalo Wings (8 pc)': 10.49,
    'Chicken Tenders (4 pc)': 5.99,
    'Loaded Nacho Fries': 4.99,
    'Iced Latte': 3.49,
    'Strawberry Lemonade': 2.99,
    'Chocolate Chip Cookie': 1.49,
    'Apple Pie': 1.99
}

food_list_label = tk.Label(root, text="=== Your Order ===", font=("Helvetica", 12), bg="#F8F8F8", fg="#333333")
food_list_label.pack(pady=10)

button_frame = tk.Frame(root, bg="#F8F8F8")
button_frame.pack(pady=10)

for food, price in food_dict.items():
    button = tk.Button(button_frame, text=f"{food} - ${price}", font=("Helvetica", 10), bg="#4CAF50", fg="#FFFFFF",
                       command=lambda food=food, price=price: add_to_list(food, price))
    button.pack(fill="x", pady=2, padx=10)

order_canvas = tk.Canvas(root, height=150, bg="#FFFFFF", highlightthickness=0)
order_frame = tk.Frame(order_canvas, bg="#FFFFFF")
scrollbar = tk.Scrollbar(root, orient="vertical", command=order_canvas.yview)
order_canvas.configure(yscrollcommand=scrollbar.set)

order_canvas.create_window((0, 0), window=order_frame, anchor="nw")
order_frame_inner = tk.Frame(order_frame, bg="#FFFFFF")
order_frame_inner.pack(fill="both", expand=True)
order_canvas.pack(side="left", fill="both", expand=True, padx=10, pady=10)
scrollbar.pack(side="right", fill="y")

price_label = tk.Label(root, text=f"Total: ${order_price:.2f}", font=("Helvetica", 12), bg="#F8F8F8", fg="#333333")
price_label.pack(pady=10)

submit_button = tk.Button(root, text="Submit Order", font=("Helvetica", 10), bg="#FF5733", fg="#FFFFFF",
                          command=submit_order)
submit_button.pack(pady=10)

root.mainloop()
