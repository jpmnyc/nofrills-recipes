class DictComparable:
    def to_dict(self):
        raise NotImplementedError('Must be overridden')

    @staticmethod
    def from_dict(source):
        raise NotImplementedError('Must be overridden')

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()
    