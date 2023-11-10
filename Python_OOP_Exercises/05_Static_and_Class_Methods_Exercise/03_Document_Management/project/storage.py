from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:

    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str) -> None:
        category = self.__find_object(category_id, self.categories)
        if category:
            category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        topic = self.__find_object(topic_id, self.topics)
        if topic:
            topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        document = self.__find_object(document_id, self.documents)
        if document:
            document.edit(new_file_name)

    def delete_category(self, category_id) -> None:
        category = self.__find_object(category_id, self.categories)
        if category:
            self.categories.remove(category)

    def delete_topic(self, topic_id) -> None:
        topic = self.__find_object(topic_id, self.topics)
        if topic:
            self.topics.remove(topic)

    def delete_document(self, document_id) -> None:
        document = self.__find_object(document_id, self.documents)
        if document:
            self.documents.remove(document)

    def get_document(self, document_id):
        return self.__find_object(document_id, self.documents)

    @staticmethod
    def __find_object(object_id, objects_collection):
        return next((obj for obj in objects_collection if obj.id == object_id), None)

    def __repr__(self) -> str:
        return "\n".join(str(d) for d in self.documents)
