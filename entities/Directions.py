from entities.DictComparable import DictComparable


class DirectionStep(DictComparable):
    def __init__(self, title='', text=''):
        self.title = title
        self.text = text

    @staticmethod
    def from_dict(source):
        return DirectionStep(**source)

    def to_dict(self):
        return dict(
            title=self.title,
            text=self.text,
        )

    def __repr__(self):
        title = f'{self.title}: ' if self.title else ''
        text = self.text[:20]
        return f'{title}{text}'


class Directions(DictComparable):

    def __init__(self, steps):
        self.steps = steps

    @staticmethod
    def from_dict(source):
        steps = [DirectionStep.from_dict(d) for d in source['directions']]
        return Directions(steps=steps)

    def to_dict(self):
        return dict(
            steps=[i.to_dict() for i in self.steps]
        )

    def __repr__(self):
        steps = '\n  '.join(map(str, self.steps))
        return f'Directions([\n  {steps}\n])'
