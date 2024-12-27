import tkinter as tk
from tkinter import messagebox

menu_items = {
        "Pizza"   : 40.00,
        "Tacos"   : 49.00,
        "Sandwich": 30.00,
        "Burger"  : 32.00,
        "Frites"  : 15.00,
        "Nuggets" : 35.00,
        "Soda"    : 15.00,
        "Limonade": 18.00

}


window = tk.Tk()
window.title("MD Restaurant Menu")
window.geometry("700x600")




header_label = tk.Label(window, text="MD Restaurant Menu", font=("Arial", 18, "bold"))
header_label.pack(pady=10)
menu_frame = tk.Frame(window)
menu_frame.pack(pady=10)

price_frame = tk.Frame(window)
price_frame.pack()

actions_frame = tk.Frame(window)
actions_frame.pack(pady=10)

selected_items = {}
total_price = tk.DoubleVar(value=0.0)

def add_item(item):
    """Add an item to the selected list and update total price."""
    if item not in selected_items:
        selected_items[item] = 1
    else:
        selected_items[item] += 1
    update_total()



def remove_item(item):
    """Remove an item from the selected list and update total price."""
    if item in selected_items:
        if selected_items[item] > 1:
            selected_items[item] -= 1
        else:
            del selected_items[item]
        update_total()

def update_total():
    """Calculate and update the total price."""
    total = sum(menu_items[item] * count for item, count in selected_items.items())
    total_price.set(total)

def confirm_order():
    """Display the current order and total price."""
    if not selected_items:
        messagebox.showinfo("Order Summary", "No items selected.")
    else:
        order_details = "\n".join([f"{item} x {count}" for item, count in selected_items.items()])
        messagebox.showinfo("Order Summary", f"Your Order:\n{order_details}\nTotal: ${total_price.get():.2f}")




tk.Label(menu_frame, text="Item", font=("Arial", 14, "bold")).grid(row=0, column=0, padx=10)
tk.Label(menu_frame, text="Price ($)", font=("Arial", 14, "bold")).grid(row=0, column=1, padx=10)

for i, (item, price) in enumerate(menu_items.items(), start=1):
    tk.Label(menu_frame, text=item, font=("Arial", 12)).grid(row=i, column=0, padx=10, pady=5)
    tk.Label(menu_frame, text=f"{price:.2f}", font=("Arial", 12)).grid(row=i, column=1, padx=10, pady=5)


    tk.Button(menu_frame, text="Add", command=lambda i=item: add_item(i), bg="green", fg="white").grid(row=i, column=2, padx=10)
    tk.Button(menu_frame, text="Remove", command=lambda i=item: remove_item(i), bg="red", fg="white").grid(row=i, column=3, padx=10)





tk.Label(actions_frame, text="Total Price:", font=("Arial", 14)).grid(row=0, column=0, padx=10)
tk.Label(actions_frame, textvariable=total_price, font=("Arial", 14), fg="blue").grid(row=0, column=1, padx=10)

tk.Button(actions_frame, text="Confirm Order", command=confirm_order, bg="blue", fg="white", font=("Arial", 12)).grid(row=1, column=0, pady=10, columnspan=2)
tk.Button(actions_frame, text="Exit", command=window.quit, bg="black", fg="white", font=("Arial", 12)).grid(row=2, column=0, pady=10, columnspan=2)

window.mainloop()