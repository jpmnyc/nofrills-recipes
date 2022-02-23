# [START bookshelf_firestore_client_import]
from google.cloud import firestore
# [END bookshelf_firestore_client_import]

from logger import log

RECIPE = u'Recipe'
RECIPE_CACHE = dict()


def recipe_cache():
    return RECIPE_CACHE

@log
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
def recipe_ref(recipe_id):
    cache = recipe_cache()
    ref = cache.get(recipe_id)
    if ref is None:
        db = firestore.Client()
        ref = db.collection(RECIPE).document(recipe_id)
        cache[recipe_id] = ref

    return ref


@log
def read(recipe_id):
    ref = recipe_ref(recipe_id)
    recipe_header = document_to_dict(ref.get())
    ingredients = document_to_dict(recipe_header['ingredient_list'].get())['ingredients']
    _, directions = read_directions(recipe_id)
    return recipe_header, ingredients, directions


@log
def read_directions(recipe_id):
    ref = recipe_ref(recipe_id)
    recipe_header = document_to_dict(ref.get())
    directions = document_to_dict(recipe_header['directions'].get())['directions']
    return recipe_header['name'], directions


@log
def update(data, book_id=None):
    db = firestore.Client()
    book_ref = db.collection(RECIPE).document(book_id)
    book_ref.set(data)
    return document_to_dict(book_ref.get())


create = update


@log
def delete(id):
    db = firestore.Client()
    book_ref = db.collection(RECIPE).document(id)
    book_ref.delete()
