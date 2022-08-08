class ABSObject(object):
    def __init__(self, name: str, id: int) -> None:
        if name is None:
            self.__name = "Beverley hills"
        else:
            self.__name = name
        self.id = id

    def get_name(self) -> str:
        return self.__name

    def get_id(self) -> int:
        return self.id

    def print_name(self) -> None:
        print(self.__name)

    def print_id(self) -> None:
        print(self.id)
