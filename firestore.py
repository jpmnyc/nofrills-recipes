from google.cloud import firestore
from entities.IngredientList import IngredientList
from entities.Directions import Directions

from logger import log

RECIPE = u'Recipe'
INGREDIENT_LIST = u'Ingredient List'
DIRECTIONS = u'Directions'


def document_to_dict(doc):
    if not doc.exists:
        return None
    doc_dict = doc.to_dict()
    doc_dict['id'] = doc.id
    return doc_dict


@log
def next_page(limit=10, start_after=None):

    db = firestore.Client()

    query = db.collection(RECIPE).limit(limit).order_by(u'name')

    if start_after:
        # Construct a new query starting at this document.
        query = query.start_after({u'name': start_after})

    docs = query.stream()
    docs = list(map(document_to_dict, docs))

    last_name = None
    if limit == len(docs):
        # Get the last document from the results and set as the last title.
        last_name = docs[-1][u'name']
    return docs, last_name


@log
def recipe(recipe_id):
    db = firestore.Client()
    return db.collection(RECIPE).document(recipe_id)


def read_header(recipe_id):
    return document_to_dict(recipe(recipe_id).get())


@log
def read(recipe_id):
    recipe_header = read_header(recipe_id)
    ingredients = read_ingredients(recipe_header['ingredient_list'])
    directions = read_directions(recipe_header['directions'])
    return recipe_header, ingredients, directions


def read_ingredients(ingredients_ref):
    return IngredientList.from_dict(document_to_dict(ingredients_ref.get()))


@log
def read_directions(directions_ref):
    return Directions.from_dict(document_to_dict(directions_ref.get()))


@log
def update(data, book_id=None):
    db = firestore.Client()
    book_ref = db.collection(RECIPE).document(book_id)
    book_ref.set(data)
    return document_to_dict(book_ref.get())


create = update


@log
def delete(recipe_id):
    db = firestore.Client()
    book_ref = db.collection(RECIPE).document(recipe_id)
    book_ref.delete()


def ingredient_list_example():
    db = firestore.Client()
    ref = db.collection(INGREDIENT_LIST).document('7HuyDFPFhV9Y2nAvbp06')
    return ref


def directions_example():
    db = firestore.Client()
    return db.collection(DIRECTIONS).document('fqkqgOinMdEBA5SYdV44')
