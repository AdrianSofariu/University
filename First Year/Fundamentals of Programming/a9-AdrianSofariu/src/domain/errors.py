class InputError(Exception):
    """
    this class inherits the exception class and is meant to be used to signal bad input
    """
    pass


class BusinessLogicError(Exception):
    """
    this class inherits the exception class and is meant to be used for enforcing the business logic
    """
    pass


class RepositoryError(Exception):
    """
    this class inherits the exception class and is meant to be used for raising errors if repository operations fail
    """
    pass


class UndoRedoError(Exception):
    """
    this class inherits the exception class and is meant to be used for signaling end of undo/redo stacks
    """
    pass
