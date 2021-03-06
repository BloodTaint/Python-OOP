from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def __found_category(self, category_id):
        for i in self.categories:
            if i.id == category_id:
                return i

    def __found_topic(self, topic_id):
        for i in self.topics:
            if i.id == topic_id:
                return i

    def __found_document(self, document_id):
        for i in self.documents:
            if i.id == document_id:
                return i

    def edit_category(self, category_id: int, new_name: str):
        category = self.__found_category(category_id)
        category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.__found_topic(topic_id)
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.__found_document(document_id)
        document.file_name = new_file_name

    def delete_category(self, category_id):
        category = self.__found_category(category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.__found_topic(topic_id)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.__found_document(document_id)
        self.documents.remove(document)

    def get_document(self, document_id):
        document = self.__found_document(document_id)
        return document

    def __repr__(self):
        result = ''
        for i in self.documents:
            result += repr(i)
            result += '\n'
        return result


# from project.category import Category
# from project.document import Document
# from project.topic import Topic
#
#
# class Storage:
#     def __init__(self):
#         self.categories = []
#         self.topics = []
#         self.documents = []
#
#     def add_category(self, category: Category):
#         if any([x for x in self.categories if x.id == category.id]):
#             return
#         self.categories.append(category)
#
#     def add_topic(self, topic: Topic):
#         if any([x for x in self.topics if x.id == topic.id]):
#             return
#         self.categories.append(topic)
#
#     def add_document(self, document: Document):
#         if any([x for x in self.documents if x.id == document.id]):
#             return
#         self.categories.append(document)
#
#     def edit_category(self, category_id: int, new_name: str):
#         category = self.__get_obj_by_id(self.categories, category_id)
#         category.edit(new_name)
#
#     def __get_obj_by_id(self, objects, id):
#         for obj in objects:
#             if obj.id == id:
#                 return obj
#
#     def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
#         topic = self.__get_obj_by_id(self.topics, topic_id)
#         topic.edit(new_topic, new_storage_folder)
#
#     def edit_document(self, document_id: int, new_file_name: str):
#         document = self.__get_obj_by_id(self.documents, document_id)
#         document.edit(new_file_name)
#
#     def delete_category(self, category_id):
#         category = self.__get_obj_by_id(self.categories, category_id)
#         self.categories.remove(category)
#
#     def delete_topic(self, topic_id):
#         topic = self.__get_obj_by_id(self.topics, topic_id)
#         self.topics.remove(topic)
#
#     def delete_document(self, document_id):
#         document = self.__get_obj_by_id(self.documents, document_id)
#         self.documents.remove(document)
#
#     def get_document(self, document_id):
#         return self.__get_obj_by_id(self.documents, document_id)
#
#     def __repr__(self):
#         return '\n'.join([str(x) for x in self.documents])
# #     ToDo - ne e kakto trqbwa tuk
