class WrongRowFormatErr(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class RowNotFoundByIdErr(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)




