from datetime import datetime
from signal import pause
import pymongo
from pymongo import ReturnDocument

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["kenzie"]


class Posts:
    def __init__(self, **kwargs):
        self.id = list(db.posts.find().sort("_id", -1).limit(1))[0]["id"]+1 if len(list(db.posts.find())) > 0 else 1
        self.created_at = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.updated_at = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.title = kwargs["title"]
        self.author = kwargs["author"]
        self.tags = kwargs["tags"]
        self.content = kwargs["content"]

    @staticmethod
    def get_post_all():
        post_list = db.posts.find()
        return post_list

    @staticmethod 
    def create_post(payload):
        db.posts.insert_one(payload.__dict__)
    
    @staticmethod
    def delete_post(post_id):
        return db.posts.find_one_and_delete({"id": post_id})
    
    @staticmethod
    def update_post(post_id, payload):
        payload["updated_at"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        return db.posts.find_one_and_update(
            {"id": post_id}, 
            {"$set": payload}, 
            return_document=ReturnDocument.AFTER
        )
        
        
    @staticmethod
    def filter_post(post_id):
        return db.posts.find_one({"id": post_id})
    
    