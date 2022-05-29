import os

from pymongo import MongoClient
from pymongo.database import Database


class MongoDB:

    instance: Database = None

    @classmethod
    def get_instance(cls) -> Database:
        if cls.instance is None:
            cls.instance = cls.create_instance()
            return cls.instance

        return cls.instance

    @classmethod
    def create_instance(cls) -> Database:
        user = os.environ.get("MONGO_USER")
        password = os.environ.get("MONGO_PASSWORD")

        connection_string = f"mongodb+srv://{user}:{password}@cluster0.fz9ncw0.mongodb.net/?retryWrites=true&w=majority"

        client = MongoClient(connection_string)

        return client.twitter
