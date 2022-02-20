NAME = 'Chocolate Cake'


def recipe_dict():
    return dict(
        name=NAME,
        source='Martha Stewart'
    )


def read_directions(*args, **kwargs):
    return 'Empty Name', [dict(title='', text='Do Something'),
                          dict(title='Bake the Cake', text='Pat-a-cake, pat-a-cake, baker''s man. Bake me a cake just as fast as you can')]


def read(recipe_id):
    return recipe_dict(), [dict(), dict()], ["Do one thing", "Do another thing"]


def next_page(limit=10, start_after=None):
    return recipe_dict(), NAME
