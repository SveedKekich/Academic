class EntityContext:
    def __init__(self, provider, filename: str):
        self.provider = provider
        self.filename = filename

    def save(self, obj):
        self.provider.save(obj, self.filename)

    def load(self):
        return self.provider.load(self.filename)
