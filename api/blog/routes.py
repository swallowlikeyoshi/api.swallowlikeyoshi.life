from . import blog
from queryPost import get_post, get_post_list, put_post
from flask import request, json

@blog.route('/posts/get_post', methods=['GET'])
def route_get_post():
    try:
        query_id = request.args.get('id')
        post = get_post(query_id)
        return json.jsonify(post)
    except Exception as e:
        print(f"route_get_post 에러: {e}")
        return None
    
@blog.route('/posts/get_post_list', methods=['GET'])
def route_get_post_list():
    try:
        posts = get_post_list()
        post_list = {
            'num': len(posts),
            'post_list': posts,
        }
        return json.jsonify(post_list)
    except Exception as e:
        print(f'route_get_post_list 에러: {e}')
        return None