

class LocText():
    prefix: str
    @classmethod
    def create(cls):
        return LocText()
        
    def add(self, key: str):
        ...