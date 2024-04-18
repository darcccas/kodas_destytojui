class CoffeeShop:
    def __init__(self, name: str, meniu: list, order: list = None):
        if order is None:
            order = []
        self.name = name
        self.meniu = meniu
        self.order = order

    def add_order(self, item):
        for element in self.meniu:
            if element["name"] == item:
                self.order.append(item)
                print(f"Order of {item} is added")
                break
        else:
            print(f"Cafe {self.name}, doesen't have {item} in meniu")

    def filfill_order(self):
        if len(self.order) > 0:
            print(f"{self.order[-1]} yra paruosta")
            self.order.pop()
        else:
            print("Visi uzsakymai ivykditi")

    def list_order(self):
        return self.order if len(self.order) > 0 else []

    def due_amount(self):
        total = 0
        for x in self.order:
            for y in self.meniu:
                if y["name"] == x:
                    total += y["price"]
        return total

    def cheapes_item(self):
        return min(self.meniu, key=lambda x: x["price"])["name"]

    def drinks_only(self):
        pass

    def food_only(self):
        pass


menu_list = [
    {"name": "Cheeseburger", "type": "food", "price": 9.99},
    {"name": "Caesar Salad", "type": "food", "price": 8.49},
    {"name": "Margherita Pizza", "type": "food", "price": 11.99},
    {"name": "Spaghetti Carbonara", "type": "food", "price": 12.99},
    {"name": "Grilled Chicken Sandwich", "type": "food", "price": 10.99},
    {"name": "Mojito", "type": "drink", "price": 7.99},
    {"name": "Iced Latte", "type": "drink", "price": 4.49},
    {"name": "Red Wine (glass)", "type": "drink", "price": 8.99},
    {"name": "Margarita", "type": "drink", "price": 9.99},
    {"name": "Lemonade", "type": "drink", "price": 3.99},
    {"name": "BBQ Ribs", "type": "food", "price": 15.99},
    {"name": "Vegetable Stir Fry", "type": "food", "price": 11.49},
    {"name": "Fish and Chips", "type": "food", "price": 13.99},
    {"name": "Chocolate Cake", "type": "food", "price": 6.99},
    {"name": "Cappuccino", "type": "drink", "price": 4.99},
    {"name": "Green Tea", "type": "drink", "price": 3.49},
    {"name": "Chicken Caesar Wrap", "type": "food", "price": 9.49},
    {"name": "Soda (can)", "type": "drink", "price": 2.49},
    {"name": "Beef Tacos", "type": "food", "price": 10.99},
    {"name": "Mai Tai", "type": "drink", "price": 8.49},
]

cafe = CoffeeShop("ANA", menu_list)

cafe.add_order("Fish and Chips")
print(cafe.due_amount())
cafe.add_order("Lemonade")

cafe.add_order("Green Tea")
print(cafe.due_amount())
print(cafe.cheapes_item())
print(cafe.list_order())
cafe.filfill_order()
cafe.filfill_order()
cafe.filfill_order()
cafe.filfill_order()
print(cafe.due_amount())
