import abc as SkinCareProduct

class Moisturizer(SkinCareProduct):
    """
    Represents a moisturizer, a specific type of skin care product.

    Attributes
    ----------
    _hydration_level : str
        Indicates the hydration level provided by the moisturizer.
    """

    def __init__(self, brand, suitable_for, hydration_level):
        super().__init__(brand, 'Moisturizer', suitable_for)
        self._hydration_level = hydration_level

    @property
    def hydration_level(self):
        """str: Gets or sets the hydration level of the moisturizer."""
        return self._hydration_level

    @hydration_level.setter
    def hydration_level(self, value):
        if not isinstance(value, str):
            raise ValueError("Hydration level must be a string.")
        self._hydration_level = value

    def __str__(self):
        return super().__str__() + f" with hydration level {self._hydration_level}"
