import datetime
from unittest import TestCase
from entities.Recipe import Recipe


class TestRecipe(TestCase):
    def test_from_dict(self):
        r = Recipe()
        d = dict()
        r1 = Recipe.from_dict(d)
        self.assertEqual(r1, r)
        self.assertEqual(Recipe.from_dict(r1.to_dict()), r1)

        r = Recipe(name='Cake')
        d = dict(name='Cake')
        r1 = Recipe.from_dict(d)
        self.assertEqual(r1, r)
        self.assertEqual(Recipe.from_dict(r1.to_dict()), r1)

    def test_creation_date_string(self):
        r = Recipe(creation_time=datetime.datetime(2022, 3, 3, 12, 1, 1))
        self.assertEqual("2022-03-03", r.creation_date_string)

    def test_update_time_string(self):
        r = Recipe(update_time=datetime.datetime(2022, 3, 3, 12, 1, 1))
        self.assertEqual("2022-03-03 12:01:01", r.update_time_string)
