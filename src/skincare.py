from data import Product


class SkinCareProduct(Product):
    """
    Represents a skin care product with additional information about skin types it is suitable for.

    Attributes
    ----------
    _suitable_for : list
        List of skin types the product is suitable for
    """
    def __init__(self, brand, product_type, suitable_for):
        """
        Initializes a SkinCareProduct instance with the given brand, product type, and suitability information.

        :param brand: Brand of the product
        :param product_type: Type of the product
        :param suitable_for: List of skin types the product is suitable for
        """
        super().__init__(brand, product_type)
        self._suitable_for = suitable_for

    @property
    def suitable_for(self):
        """
        Gets or sets the skin types the product is suitable for.

        :return: List of skin types the product is suitable for
        """
        return self._suitable_for

    @suitable_for.setter
    def suitable_for(self, value):
        """
        Sets the skin types the product is suitable for.

        :param value: List of strings representing skin types
        """
        if not isinstance(value, list) or not all(isinstance(s, str) for s in value):
            raise ValueError("Suitable for must be a list of strings.")
        self._suitable_for = value

    def __str__(self):
        """
        Returns a string representation of the SkinCareProduct instance.

        :return: String representation of the instance
        """
        return super().__str__() + f" (suitable for {', '.join(self._suitable_for)})"
