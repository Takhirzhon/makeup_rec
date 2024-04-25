import abc as SkinCareProduct

class Serum(SkinCareProduct):
    """
    Represents a serum, a specific type of skin care product known for concentrated ingredients.

    Attributes
    ----------
    _consistency : str
        Describes the consistency of the serum (e.g., gel, liquid, oil).
    """

    def __init__(self, brand, suitable_for, consistency):
        super().__init__(brand, 'Serum', suitable_for)
        self._consistency = consistency

    @property
    def consistency(self):
        """str: Gets or sets the consistency of the serum."""
        return self._consistency

    @consistency.setter
    def consistency(self, value):
        if not isinstance(value, str):
            raise ValueError("Consistency must be a string.")
        self._consistency = value

    def __str__(self):
        return super().__str__() + f" with a {self._consistency} consistency"
