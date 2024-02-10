import os
from pymongo import MongoClient
from bson.objectid import ObjectId

mongo_uri = os.getenv('MONGO_URI')
client = MongoClient(mongo_uri)
db = client['students']
collection = db['students']


def add(student=None):
    if collection.find_one({'first_name': student.first_name, 'last_name': student.last_name}):
        return 'already exists', 409

    student_id = collection.insert_one(student.to_dict()).inserted_id
    return str(student_id)


def get_by_id(student_id=None, subject=None):
    student = collection.find_one({'_id': ObjectId(student_id)})
    if not student:
        return 'not found', 404
    # student['student_id'] = str(student['_id'])
    # del student['_id']
    print(student)
    return student


def delete(student_id=None):
    result = collection.delete_one({'_id': ObjectId(student_id)})
    if result.deleted_count == 0:
        return 'not found', 404
    return student_id
