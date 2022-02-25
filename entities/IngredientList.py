from entities.Ingredient import Ingredient
from entities.DictComparable import DictComparable

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
