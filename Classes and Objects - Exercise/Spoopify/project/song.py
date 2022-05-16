# class Song:
#     def __init__(self, name: str, length: float, single: bool):
#         self.name = name
#         self.length = length
#         self.single = single
#
#     def get_info(self):
#         return f"{self.name} - {self.length}"


class Song:
    def __init__(self, name, length, single):
        self.name = name
        self.length = length
        self.single = single

    def get_info(self):
        return f"{self.name} - {self.length}"