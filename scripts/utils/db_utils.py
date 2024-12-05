from pymongo import MongoClient

def test_mongodb_connection():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["LosAngeles_Data"]
    print("MongoDB connected:", db.list_collection_names())

if __name__ == "__main__":
    test_mongodb_connection()
