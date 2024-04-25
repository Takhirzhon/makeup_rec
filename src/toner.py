import abc as SkinCareProduct

class Toner(SkinCareProduct):
    """
    Represents a toner, a specific type of skin care product.

    Attributes
    ----------
    _ingredients : list of str
        List of active ingredients in the toner.
    """

    def __init__(self, brand, suitable_for, ingredients):
        super().__init__(brand, 'Toner', suitable_for)
        self._ingredients = ingredients

    @property
    def ingredients(self):
        """list of str: Gets or sets the active ingredients of the toner."""
        return self._ingredients

    @ingredients.setter
    def ingredients(self, value):
        if not isinstance(value, list) or not all(isinstance(i, str) for i in value):
            raise ValueError("Ingredients must be a list of strings.")
        self._ingredients = value

    def __str__(self):
        return super().__str__() + f" containing {', '.join(self._ingredients)}"
