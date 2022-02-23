import Ingredient


class IngredientList(object):

    def __init__(self, ingredients):
        self.ingredients = ingredients

    @staticmethod
    def from_dict(source):
        ingredients = [Ingredient.from_dict(d) for d in source.ingredients]
        return IngredientList(ingredients=ingredients)

    def to_dict(self):
        return dict(
            ingredients=[i.to_dict() for i in self.ingredients]
        )