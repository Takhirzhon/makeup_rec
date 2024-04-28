import json

class Product:
    """
    Represents a product with brand, product type, and suitability information.

    Attributes:
    _brand (str): Brand of the product
    _product_type (str): Type of the product
    _suitable_for (list): List of skin types the product is suitable for
    """

    def __init__(self, brand, product_type, suitable_for):
        """
        Initializes a Product instance with the given brand, product type, and suitability information.

        :param brand: Brand of the product
        :param product_type: Type of the product
        :param suitable_for: List of skin types the product is suitable for
        """
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

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return (self.brand.lower() == other.brand.lower() and
                any(skin.lower() in self.suitable_for for skin in other.suitable_for))
        
def load_data(file_path='data/source.json'):
    """
    Loads product data from a JSON file and returns a list of Product instances.

    :param file_path: Path to the JSON file containing product data (default: 'data/source.json')
    :return: List of Product instances created from the data in the JSON file
    """
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            return [Product(brand=product['brand'],
                            product_type=product['type'],
                            suitable_for=product['suitable_for'])
                    for product in data]
    except FileNotFoundError:
        print("Error: The file was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: The file is not a valid JSON.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []
