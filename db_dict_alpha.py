class DBDictAlpha:
    def __init__(self):
        self.__dict = {}

    def add_item(self, key, value):
        if self.__dict.get(key) is None:
            self.__dict[key] = [value]
        else:
            self.__dict[key].append(value)

    def get_item(self, key):
        return self.__dict.get(key)
