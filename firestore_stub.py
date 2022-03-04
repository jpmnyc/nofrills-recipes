import datetime
from entities.IngredientList import Ingredient, IngredientList
from entities.Directions import DirectionStep, Directions
from entities.Recipe import Recipe


NAME = 'Chocolate Cake'
CREATION_TIME = datetime.datetime.now()


def recipe1_dict():
    return dict(
        id='dummy1',
        name=NAME,
        source='Martha Stewart',
        creation_time=CREATION_TIME,
        update_time=CREATION_TIME
    )


def recipe2_dict():
    return  dict(
        id='dummy2',
        name="Another Name",
        source="Food & Wine",
        creation_time=CREATION_TIME,
        update_time=CREATION_TIME
    )


def ingredients():
    return [Ingredient('all-purpose flour', 1, 'c', ''), Ingredient('butter', 8, 'tbsp', 'softened')]


def ingredient_list():
    return IngredientList(ingredients())


def read_directions(*args, **kwargs):
    return Directions([
        DirectionStep(title='', text='Do Something'),
        DirectionStep(title='Bake the Cake', text='Pat-a-cake, pat-a-cake, baker''s man. Bake me a cake just as fast as you can')])


def read_ingredients(*args, **kwarg):
    return ingredient_list()


def read(*_args):
    return recipe1_dict(), ingredient_list(), read_directions()


def read_header(*_args):
    return dict(ingredient_list=None, directions=None)


def next_page(limit=10, start_after=None):
    return [Recipe.from_dict(recipe1_dict()), Recipe.from_dict(recipe2_dict())], NAME
