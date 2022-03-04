from unittest import TestCase
from entities.Recipe import Recipe


class TestRecipe(TestCase):
    def test_from_dict(self):
        r = Recipe()
        d = dict()
        r1 = Recipe.from_dict(d)
        assert(r1 == r)
        assert(Recipe.from_dict(r1.to_dict()) == r1)

        r = Recipe(name='Cake')
        d = dict(name='Cake')
        r1 = Recipe.from_dict(d)
        assert(r1 == r)
        assert(Recipe.from_dict(r1.to_dict()) == r1)
