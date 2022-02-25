import datetime
from entities.Ingredient import Ingredient
from entities.IngredientList import IngredientList

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
    return 'Empty Name', [dict(title='', text='Do Something'),
                          dict(title='Bake the Cake', text='Pat-a-cake, pat-a-cake, baker''s man. Bake me a cake just as fast as you can')]


def read_ingredients(*args, **kwarg):
    return ingredient_list()


def read(recipe_id):
    _, directions = read_directions()
    return recipe1_dict(), [dict(), dict()], directions


def next_page(limit=10, start_after=None):
    return [recipe1_dict(), recipe2_dict()], NAME
