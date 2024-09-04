class IdObject:
    """
    this class serves as a base for other domain classes that have an id
    """
    def __init__(self, _id: int):
        if not isinstance(_id, int):
            raise TypeError("Id cannot be non-integer.")
        self.__id = _id

    @property
    def id(self):
        return self.__id
