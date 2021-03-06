# class Task:
#     def __init__(self, name: str, due_date: str, ):
#         self.name = name
#         self.due_date = due_date
#         self.comments = []
#         self.completed = False

#     def change_name(self, new_name: str):
#         if not new_name == self.name:
#             self.name = new_name
#             return new_name
#         else:
#             return "Name cannot be the same."

#     def change_due_date(self, new_date: str):
#         if not new_date == self.due_date:
#             self.due_date = new_date
#             return new_date
#         else:
#             return "Date cannot be the same."

#     def add_comment(self, comment: str):
#         self.comments.append(comment)

#     def edit_comment(self, comment_number: int, new_comment: str):
#         if 0 <= comment_number < len(self.comments):
#             self.comments[comment_number] = new_comment
#             return ", ".join(self.comments)

#         else:
#             return "Cannot find comment."

#     def details(self):
#         return f"Name: {self.name} - Due Date: {self.due_date}"


class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name):
        if not new_name == self.name:
            self.name = new_name
            return self.name
        return "Name cannot be the same."

    def change_due_date(self, new_date):
        if not new_date == self.due_date:
            self.due_date = new_date
            return self.due_date
        return "Date cannot be the same."

    def add_comment(self, comment):
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str):
        if comment_number < 0 or comment_number >= len(self.comments):
            return "Cannot find comment."
        self.comments[comment_number] = new_comment
        return ", ".join([x for x in self.comments])

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"
