import os
from pymongo import MongoClient
from dotenv import load_dotenv
from typing import TypedDict, Optional, Any, List

load_dotenv()

username = os.getenv('MONGO_USERNAME')
password = os.getenv('MONGO_PASSWORD')
DB_URL = "192.168.0.9:27017"

client = MongoClient(f'mongodb://{username}:{password}@{DB_URL}/')

db = client['blogPost']
collection = db['posts']

class PostContents(TypedDict):
    id: int
    title: str
    contents: str

def get_post(id) -> PostContents:
    try:
        post = collection.find_one({'id': str(id)})
        return post
    except Exception as e:
        print(f"get_post 오류: {e}")
        return None
    
def get_post_list() -> List[str]:
    try:
        posts = collection.find({}, {'id': 1, 'title': 1})
        return list(posts)
    except Exception as e:
        print(f"get_post_list 오류: {e}")
        return None

def put_post(contents: PostContents) -> Optional[Any]:
    try:
        new_post = {
            "id": contents['id'],
            "title": contents['title'],
            "contents": contents['contents']
        }
        result = collection.insert_one(new_post)
        return result
    except Exception as e:
        print(f'put_post 오류: {e}')
        return None

if __name__ == "__main__":
    # print(put_post({ "id": "2", "title": "2. 세상 사람들이여, 꿈을 가져라!", "contents": "제곧내"}))
    # print(get_post_list())
    print(get_post("2"))