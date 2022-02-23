class Ingredient(object):

    def __init__(self, name, quantity, measurement, preparation):
        self.name = name
        self.quantity = quantity
        self.measurement = measurement
        self.preparation = preparation

    @staticmethod
    def from_dict(source):
        return Ingredient(**source)

    def to_dict(self):
        return dict(
            name=self.name,
            quantity=self.quantity,
            measurememt=self.measurement,
            preparation=self.preparation
        )