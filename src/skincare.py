from data import Product

class SkinCareProduct(Product):
    def __init__(self, brand, product_type, suitable_for):
        super().__init__(brand, product_type)
        self._suitable_for = suitable_for

    @property
    def suitable_for(self):
        """list of str: Gets or sets the skin types the product is suitable for."""
        return self._suitable_for

    @suitable_for.setter
    def suitable_for(self, value):
        if not isinstance(value, list) or not all(isinstance(s, str) for s in value):
            raise ValueError("Suitable for must be a list of strings.")
        self._suitable_for = value

    def __str__(self):
        return super().__str__() + f" (suitable for {', '.join(self._suitable_for)})"
