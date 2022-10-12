class RulesException(Exception):
    def __init__(self, msg: str) -> None:
        super(RulesException, self).__init__(msg)
        self.msg = msg


class NotFoundException(RulesException):
    def __init__(self, msg: str) -> None:
        super(NotFoundException, self).__init__(msg)


class NotInsertedException(RulesException):
    def __init__(self, msg: str) -> None:
        super(NotInsertedException, self).__init__(msg)
        

class NotUpdatedException(RulesException):
    def __init__(self, msg: str) -> None:
        super(NotUpdatedException, self).__init__(msg)