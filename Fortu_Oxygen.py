class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print("Product:", self.name)
        print("Price: ₱", self.price)
        print("Quantity:", self.quantity)

    def sell(self, quantity):
        if quantity <= self.quantity:
            self.quantity -= quantity
            print(f"Sold {quantity} units of {self.name}.")
        else:
            print(f"Insufficient stock for {self.name}. Only {self.quantity} units available.")

    def restock(self, amount):
        if amount > 0:
            self.quantity += amount
            print(f"Restocked {amount} units of {self.name}. New quantity: {self.quantity}.")
        else:
            print("Invalid quantity. Please enter a positive number.")

    def remove(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            print(f"Removed {amount} units of {self.name}. New quantity: {self.quantity}.")
        else:
            print(f"Cannot remove {amount} units of {self.name}. Only {self.quantity} units available.")


# Store class to manage multiple products
class Store:
    """Simple store inventory manager for Product objects."""
    def __init__(self):
        self.products = {}
        self.sales_total = 0.0
        self.expenses_total = 0.0

    def add_product(self, product):
        self.products[product.name.lower()] = product

    def get_product(self, name):
        return self.products.get(name.lower())

    def restock_product(self, name, amount):
        product = self.get_product(name)
        if product:
            product.restock(amount)
        else:
            print(f"Product '{name}' not found in inventory.")

    def remove_product(self, name, amount):
        product = self.get_product(name)
        if product:
            product.remove(amount)
        else:
            print(f"Product '{name}' not found in inventory.")

    def sell_product(self, name, quantity):
        product = self.get_product(name)
        if product:
            product.sell(quantity)
        else:
            print(f"Product '{name}' not found in inventory.")

    def sell_to_customer(self, name, quantity):
        """Sell items to a customer: deduct stock and record revenue."""
        product = self.get_product(name)
        if not product:
            print(f"Product '{name}' not found in inventory.")
            return
        if quantity <= 0:
            print("Quantity must be positive.")
            return
        if quantity > product.quantity:
            print(f"Insufficient stock for {product.name}. Only {product.quantity} units available.")
            return
        total = product.price * quantity
        product.quantity -= quantity
        self.sales_total += total
        print(f"Sold {quantity} x {product.name} for ₱{total:.2f}.")

    def buy_from_supplier(self, name, quantity, cost_per_unit):
        """Buy stock from a supplier: increase stock and record expense."""
        product = self.get_product(name)
        if not product:
            print(f"Product '{name}' not found in inventory.")
            return
        try:
            qty = int(quantity)
            cost = float(cost_per_unit)
        except (TypeError, ValueError):
            print("Invalid quantity or cost.")
            return
        if qty <= 0 or cost <= 0:
            print("Quantity and cost must be positive.")
            return
        product.quantity += qty
        expense = qty * cost
        self.expenses_total += expense
        print(f"Bought {qty} x {product.name} for ₱{expense:.2f}. New qty: {product.quantity}.")

    def display_inventory(self):
        rows = []
        for i, p in enumerate(self.products.values(), start=1):
            rows.append([str(i), p.name, f"₱{p.price:.2f}", str(p.quantity)])
        if not rows:
            print("No products in inventory.")
            return
        headers = ["#", "Product", "Price", "Quantity"]
        # compute column widths
        widths = [len(h) for h in headers]
        for r in rows:
            for idx, cell in enumerate(r):
                widths[idx] = max(widths[idx], len(cell))
        # build format strings
        fmt = f"{{:<{widths[0]}}}  {{:<{widths[1]}}}  {{:>{widths[2]}}}  {{:>{widths[3]}}}"
        sep = '  '.join('-' * w for w in widths)
        print("Store Inventory:")
        print(fmt.format(*headers))
        print(sep)
        for r in rows:
            print(fmt.format(*r))

    def display_item(self, name):
        product = self.get_product(name)
        if not product:
            print(f"Product '{name}' not found in inventory.")
            return
        headers = ["#", "Product", "Price", "Quantity"]
        row = ["1", product.name, f"₱{product.price:.2f}", str(product.quantity)]
        widths = [len(h) for h in headers]
        for idx, cell in enumerate(row):
            widths[idx] = max(widths[idx], len(cell))
        fmt = f"{{:<{widths[0]}}}  {{:<{widths[1]}}}  {{:>{widths[2]}}}  {{:>{widths[3]}}}"
        sep = '  '.join('-' * w for w in widths)
        print(fmt.format(*headers))
        print(sep)
        print(fmt.format(*row))

    def change_price(self, name, new_price):
        product = self.get_product(name)
        if not product:
            print(f"Product '{name}' not found in inventory.")
            return
        try:
            price = float(new_price)
            if price <= 0:
                print("Price must be greater than zero.")
                return
        except (TypeError, ValueError):
            print("Invalid price value.")
            return
        product.price = price
        print(f"Price of {product.name} updated to ₱{product.price}.")


# Create some product objects and manage them via Store
product1 = Product("Laptop", 50000, 10)
product2 = Product("Smartphone", 20000, 25)
product3 = Product("Headphones", 3000, 50)
product4 = Product("Smartwatch", 8000, 15)
product5 = Product("Tablet", 15000, 20)

store = Store()
for p in (product1, product2, product3, product4, product5):
    store.add_product(p)
def _choose_product_name(store):
    names = list(store.products.keys())
    if not names:
        print("No products available.")
        return None
    print("Select a product by number:")
    for i, n in enumerate(names, start=1):
        p = store.get_product(n)
        print(f"{i}. {p.name} (Qty: {p.quantity})")
    while True:
        choice = input("Enter number (or 'c' to cancel): ").strip()
        if choice.lower() == 'c':
            return None
        if choice.isdigit() and 1 <= int(choice) <= len(names):
            return store.get_product(names[int(choice) - 1]).name
        print("Invalid selection.")


def _prompt_positive_int(prompt):
    while True:
        val = input(prompt).strip()
        try:
            n = int(val)
            if n > 0:
                return n
            print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")


def _prompt_positive_float(prompt):
    while True:
        val = input(prompt).strip()
        try:
            f = float(val)
            if f > 0:
                return f
            print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")


def run_interactive(store):
    actions = {
        '1': 'Display inventory',
        '2': 'Sell product',
        '3': 'Restock product',
        '4': 'Remove product quantity',
        '5': 'Display item',
        '6': 'Change price',
        '7': 'Sell to customer',
        '8': 'Buy from supplier',
        'q': 'Quit',
    }
    while True:
        print('\nMenu:')
        for k, v in actions.items():
            print(f"{k}) {v}")
        choice = input('Choose an action: ').strip().lower()
        if choice == '1':
            store.display_inventory()
        elif choice == '2':
            name = _choose_product_name(store)
            if name:
                qty = _prompt_positive_int('Quantity to sell: ')
                store.sell_product(name, qty)
        elif choice == '3':
            name = _choose_product_name(store)
            if name:
                amt = _prompt_positive_int('Amount to restock: ')
                store.restock_product(name, amt)
        elif choice == '4':
            name = _choose_product_name(store)
            if name:
                amt = _prompt_positive_int('Amount to remove: ')
                store.remove_product(name, amt)
        elif choice == '5':
            name = _choose_product_name(store)
            if name:
                store.display_item(name)
        elif choice == '6':
            name = _choose_product_name(store)
            if name:
                new_price = _prompt_positive_float('New price (numeric): ')
                store.change_price(name, new_price)
        elif choice == '7':
            name = _choose_product_name(store)
            if name:
                qty = _prompt_positive_int('Quantity to sell to customer: ')
                store.sell_to_customer(name, qty)
        elif choice == '8':
            name = _choose_product_name(store)
            if name:
                qty = _prompt_positive_int('Quantity to buy from supplier: ')
                cost = _prompt_positive_float('Cost per unit: ')
                store.buy_from_supplier(name, qty, cost)
        elif choice == 'q':
            print('Goodbye.')
            break
        else:
            print('Invalid option.')


def run_demo_then_exit(store):
    # quick non-interactive demo used for automated sanity checks
    store.display_inventory()
    print('--' * 30)
    store.sell_product('Laptop', 2)
    store.restock_product('Laptop', 5)
    store.remove_product('Headphones', 10)
    store.sell_to_customer('Smartphone', 3)
    store.buy_from_supplier('Tablet', 5, 12000)
    print('--' * 30)
    store.display_inventory()
    print(f"Sales total: ₱{store.sales_total:.2f} | Expenses total: ₱{store.expenses_total:.2f}")


if __name__ == '__main__':
    import os
    if os.environ.get('AUTO_DEMO') == '1':
        run_demo_then_exit(store)
    else:
        run_interactive(store)