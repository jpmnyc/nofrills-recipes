import datetime

from entities.DictComparable import DictComparable


class Recipe(DictComparable):
    def __init__(self,
                 name=None,
                 source=None,
                 difficulty=None,
                 creation_time=None,
                 ingredient_list=None,
                 rating=None,
                 directions=None,
                 update_time=None):
        self.name = name
        self.source = source
        self.difficulty = difficulty
        self.creation_time = creation_time
        self.ingredient_list = ingredient_list
        self.rating = rating
        self.directions = directions
        self.update_time = update_time

    def to_dict(self):
        return(dict(
            name=self.name,
            source=self.source,
            difficult=self.difficulty,
            creation_time=self.creation_time,
            ingredient_list=self.ingredient_list,
            rating=self.rating,
            directions=self.directions,
            update_time=self.update_time
        ))

    @staticmethod
    def from_dict(source):
        return Recipe(
            source.get('name'),
            source.get('source'),
            source.get('difficulty'),
            source.get('creation_time'),
            source.get('ingredient_list'),
            source.get('rating'),
            source.get('directions'),
            source.get('update_time')
        )

    def get_creation_date_string(self):
        return self.creation_time.strftime('%Y-%m-%d')

    def get_update_time_string(self):
        return self.update_time.strftime('%Y-%m-%d %H:%M:%S')

    creation_date_string = property(get_creation_date_string)
    update_time_string = property(get_update_time_string)

