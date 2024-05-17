class Product:
    def __init__(self, name, description, cost, price, amount, purchased, sold, weight, manufacturer, group, subgroup=None ):
        self.name = name
        self.description = description
        self.cost = cost
        self.price = price
        self.amount = amount
        self.purchased = purchased
        self.sold = sold
        self.weight = weight
        self.manufacturer = manufacturer
        self.group = group
        self.subgroup = subgroup


class ProductFactory:
    @staticmethod
    def create_Product(Product_type: str) -> Product:
        pass

products = [
    {   'id': 1,
        'name': 'coffee',
        'price': 2.5
     },
    {
        'id': 2,
        'name': 'cake',
        'price': 10
    },
    {
        'id': 3,
        'name': 'tea',
        'price': 3.2
    },
    {
        'id': 4,
        'name': 'croissant',
        'price': 5.79
    }
]