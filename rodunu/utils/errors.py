class Errors:
    data = {}
    def __init__(self, **args):
        self.data.update(**args)

    def has_errors(self):
        return len(self.data) > 0