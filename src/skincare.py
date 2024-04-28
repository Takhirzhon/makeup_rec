from data import Product


class SkinCareProduct(Product):
    def __init__(self, brand, product_type, suitable_for):
        self.brand = brand
        self.product_type = product_type
        self.suitable_for = suitable_for

    def __str__(self):
        return f"{self.brand} {self.product_type} (suitable for {', '.join(self.suitable_for)})"