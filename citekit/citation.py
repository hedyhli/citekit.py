class Citation:
    """Basic citation class"""

    def __init__(self, data: dict):
        self.data = data

    @property
    def data_(self):
        return self.data

    def __str__(self):
        return str(self.data)

    def __repr(self):
        return str(self.data)
