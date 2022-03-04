from entities.DictComparable import DictComparable


class Ingredient(DictComparable):

    def __init__(self, name, amount, measurement, preparation=''):
        self.name=name
        self.amount = amount
        self.measurement = measurement
        self.preparation = preparation

    @staticmethod
    def from_dict(source):
        return Ingredient(**source)

    def to_dict(self):
        return dict(
            name=self.name,
            amount=self.amount,
            measurement=self.measurement,
            preparation=self.preparation
        )

    def __repr__(self):
        return 'Ingredient({0} {1}{2}: {3})'.format(self.name, self.amount, self.measurement, self.preparation)


class IngredientList(DictComparable):

    def __init__(self, ingredients):
        self.ingredients = ingredients

    @staticmethod
    def from_dict(source):
        ingredients = [Ingredient.from_dict(d) for d in source['ingredients']]
        return IngredientList(ingredients=ingredients)

    def to_dict(self):
        return dict(
            ingredients=[i.to_dict() for i in self.ingredients]
        )

    def __repr__(self):
        ingredients = '\n  '.join(map(str, self.ingredients))
        return f'IngredientList([\n  {ingredients}\n])'
