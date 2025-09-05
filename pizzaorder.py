import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class PizzaOrder():
    def __init__(self, root):
        self.root = root
        self.root.title("Pizza Order")
        self.root.geometry("700x900")

        #customer information
        customer_frame = ttk.LabelFrame(root, text="Customer Info")
        customer_frame.pack(fill="x", padx=10, pady=5)

        ttk.Label(customer_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.name_entry = ttk.Entry(customer_frame, width=25)
        self.name_entry.grid(row=0, column=1, padx=5)

        ttk.Label(customer_frame, text="Phone:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.phone_entry = ttk.Entry(customer_frame, width=25)
        self.phone_entry.grid(row=1, column=1, padx=5)

        ttk.Label(customer_frame, text="Address:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.address_entry = ttk.Entry(customer_frame, width=40)
        self.address_entry.grid(row=2, column=1, padx=5)

        #pizza options
        options_frame = ttk.LabelFrame(root, text="Pizza Options")
        options_frame.pack(fill="x", padx=10, pady=5)

        #size selection
        size_frame = ttk.LabelFrame(options_frame, text="Size", relief=tk.RIDGE, padding=6)
        size_frame.pack(fill="x", padx=10, pady=5)

        self.size_variable = tk.StringVar()
        self.size_variable.set("Small")

        radiobutton1 = ttk.Radiobutton(size_frame, text="Small ($6.99)",
                                       variable=self.size_variable, value="Small")
        radiobutton2 = ttk.Radiobutton(size_frame, text="Medium ($9.99)",
                                       variable=self.size_variable, value="Medium")
        radiobutton3 = ttk.Radiobutton(size_frame, text="Large ($11.99)",
                                       variable=self.size_variable, value="Large")
        radiobutton1.grid(row=4, column=2, sticky=tk.W)
        radiobutton2.grid(row=5, column=2, sticky=tk.W)
        radiobutton3.grid(row=6, column=2, sticky=tk.W)

        #crust type selection
        crust_frame = ttk.LabelFrame(options_frame, text="Crust", relief=tk.RIDGE, padding=6)
        crust_frame.pack(fill="x", padx=10, pady=5)

        self.crust_variable = tk.StringVar()
        self.crust_variable.set("Regular")

        radiobutton1 = ttk.Radiobutton(crust_frame, text="Thin",
                                       variable=self.crust_variable, value="Thin")
        radiobutton2 = ttk.Radiobutton(crust_frame, text="Regular",
                                       variable=self.crust_variable, value="Regular")
        radiobutton3 = ttk.Radiobutton(crust_frame, text="Thick (+$2.00)",
                                       variable=self.crust_variable, value="Thick")
        radiobutton1.grid(row=4, column=2, sticky=tk.W)
        radiobutton2.grid(row=5, column=2, sticky=tk.W)
        radiobutton3.grid(row=6, column=2, sticky=tk.W)



        #toppings_frame = ttk.LabelFrame(options_frame, text="Toppings (+$2 each)")
        #toppings_frame.pack(fill="x", padx=10, pady=5)

        #checkbutton1 = ttk.Checkbutton(toppings_frame, text="Pepperoni")
        #checkbutton1.grid(row=1, column=2)
        #checkbutton2 = ttk.Checkbutton(toppings_frame, text="Mushrooms")
        #checkbutton2.grid(row=2, column=2)
        #checkbutton3 = ttk.Checkbutton(toppings_frame, text="Onions")
        #checkbutton3.grid(row=3, column=2)
        #checkbutton4 = ttk.Checkbutton(toppings_frame, text="Sausage")
        #checkbutton4.grid(row=4, column=2)



        #toppings selection
        toppings_frame = ttk.LabelFrame(options_frame, text="Toppings (+$2 each)")
        toppings_frame.pack(fill="x", padx=10, pady=5)
        self.toppings_vars = {}
        toppings = ["Pepperoni", "Mushrooms", "Onions", "Sausage", "Cheese", "Olives"]
        for i, topping in enumerate(toppings):
            var = tk.BooleanVar()
            self.toppings_vars[topping] = var
            ttk.Checkbutton(toppings_frame, text=topping, variable=var).grid(row=i, column=0, sticky=tk.W)

        #order summary
        order_frame = ttk.LabelFrame(root, text="Order Summary")
        order_frame.pack(fill="both", expand=True, padx=10, pady=5)
        self.order_text = tk.Text(order_frame, height=10)
        self.order_text.pack(padx=5, pady=5)
        self.total_label = ttk.Label(order_frame, text="Total: $0")
        self.total_label.pack()

        #
        button_frame = ttk.Frame(root)
        button_frame.pack(fill="x", pady=5)
        ttk.Button(button_frame, text="Add Pizza", command=self.add_pizza).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Submit Order", command=self.submit_order).pack(side="right", padx=5)

        self.total_price = 0

    def add_pizza(self):
        size = self.size_variable.get()
        crust = self.crust_variable.get()
        toppings = [t for t, var in self.toppings_vars.items() if var.get()]

        price = 0
        if size == "Small":
            price += 6.99
        elif size == "Medium":
            price += 9.99
        elif size == "Large":
            price += 11.99
        if crust == "Thick": price += 2
        price += 2 * len(toppings)

        #updating order summary
        pizza_desc = f"{size} pizza, {crust} crust"
        if toppings:
            pizza_desc += ", Toppings: " + ", ".join(toppings)
        self.order_text.insert(tk.END, f"{pizza_desc} - ${price}\n")
        self.total_price += price
        self.total_label.config(text=f"Total: ${self.total_price}")


    def submit_order(self):
        name = self.name_entry.get()
        if not name.strip():
            self.order_text.insert(tk.END, "\nPlease enter customer name!\n")
            return
        self.order_text.insert(tk.END, f"\nOrder submitted for {name}. Thank you!\n")



root = tk.Tk()
program = PizzaOrder(root)

program.root.mainloop()



