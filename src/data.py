import json

class Product:
    def __init__(self, brand, product_type, suitable_for):
        self._brand = brand
        self._product_type = product_type
        self._suitable_for = suitable_for

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str):
            raise ValueError("Brand must be a string.")
        self._brand = value

    @property
    def product_type(self):
        return self._product_type

    @product_type.setter
    def product_type(self, value):
        if not isinstance(value, str):
            raise ValueError("Product type must be a string.")
        self._product_type = value

    @property
    def suitable_for(self):
        return self._suitable_for

    @suitable_for.setter
    def suitable_for(self, value):
        if not isinstance(value, list) or not all(isinstance(s, str) for s in value):
            raise ValueError("Suitable for must be a list of strings.")
        self._suitable_for = value

    def __str__(self):
        return f"{self._brand} {self._product_type} (suitable for {', '.join(self._suitable_for)})"

def load_data():
    with open('./data/source.json') as f:
        data = json.load(f)
    return [Product(brand=product['brand'], product_type=product['type'], suitable_for=product['suitable_for']) for product in data]
