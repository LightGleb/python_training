from sys import maxsize


class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        # Проверки для name нужны для того, чтобы при создании ообъекта Group не передавать ему
        # никакие аргументы, в случае создании пустой группы.
        return (self.id is None or other.id is None or self.id == other.id) \
            and (self.name is None or other.name is None or self.name == other.name)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
