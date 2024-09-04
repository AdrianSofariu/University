from src.domain.errors import UndoRedoError


class Command:

    def __init__(self, fn, *args):
        self._fn = fn
        self._params = args

    def execute(self):
        self._fn(*self._params)


class Operation:

    def __init__(self, undo_action: Command, redo_action: Command):
        self._undo_action = undo_action
        self._redo_action = redo_action

    def undo(self):
        self._undo_action.execute()

    def redo(self):
        self._redo_action.execute()


class CascadedOperation:

    def __init__(self, operations: list[Operation]):
        self._operations = operations

    def undo(self):
        for op in self._operations:
            op.undo()

    def redo(self):
        for op in self._operations:
            op.redo()


class UndoService:

    def __init__(self):
        self.__undo_stack = []
        self.__redo_stack = []
        self.__is_undoredo = False

    def record_undo(self, operation: Operation):
        if self.__is_undoredo:
            return
        self.__undo_stack.append(operation)
        self.__redo_stack = []

    def undo(self):
        if len(self.__undo_stack) == 0:
            raise UndoRedoError("No more undo")
        self.__is_undoredo = True
        operation = self.__undo_stack.pop()
        operation.undo()
        self.__redo_stack.append(operation)
        self.__is_undoredo = False

    def redo(self):
        if len(self.__redo_stack) == 0:
            raise UndoRedoError("No more redo")
        self.__is_undoredo = True
        operation = self.__redo_stack.pop()
        operation.redo()
        self.__undo_stack.append(operation)
        self.__is_undoredo = False

