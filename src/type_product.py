import skincare as SkinCareProduct

class Toner(SkinCareProduct):
    def __init__(self, brand, suitable_for):
        super().__init__(brand, 'Toner', suitable_for)

    def __str__(self):
        return super().__str__()
    
class Cleanser(SkinCareProduct):
    def __init__(self, brand, suitable_for):
        super().__init__(brand, 'Cleanser', suitable_for)

    def __str__(self):
        return super().__str__()
    
class Moisturizer(SkinCareProduct):
    def __init__(self, brand, suitable_for):
        super().__init__(brand, 'Moisturizer', suitable_for)

    def __str__(self):
        return super().__str__()
    
class Serum(SkinCareProduct):
    def __init__(self, brand, suitable_for):
        super().__init__(brand, 'Serum', suitable_for)

    def __str__(self):
        return super().__str__()

class Sunscreen(SkinCareProduct):
    def __init__(self, brand, suitable_for):
        super().__init__(brand, 'Sunscreen', suitable_for)

    def __str__(self):
        return super().__str__()