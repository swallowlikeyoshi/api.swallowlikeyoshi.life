from . import blog
from .queryPost import get_post, get_post_list, put_post
from flask import request, json

@blog.route('/posts/get_post', methods=['GET'])
def route_get_post():
    try:
        query_id = request.args.get('id')
        post = get_post(query_id)
        if post is not None:
            post['_id'] = str(post['_id'])
            return json.jsonify(post), 200  # 성공적으로 게시물을 찾은 경우 200 상태 코드와 함께 반환합니다.
        else:
            return json.jsonify({'error': '게시물을 찾을 수 없습니다.'}), 404  # 게시물이 없는 경우 404 상태 코드를 반환합니다.
    except Exception as e:
        print(f"route_get_post 에러: {e}")
        return json.jsonify({'error': '서버 오류입니다.'}), 500  # 서버에서 오류가 발생한 경우 500 상태 코드를 반환합니다.
    
@blog.route('/posts/get_post_list', methods=['GET'])
def route_get_post_list():
    try:
        posts = get_post_list()
        for post in posts:
            post['_id'] = str(post['_id'])
        post_list = {
            'num': len(posts),
            'post_list': posts,
        }
        return json.jsonify(post_list)
    except Exception as e:
        print(f'route_get_post_list 에러: {e}')
        return None
    
@blog.route('/posts/put_post', methods=['POST'])
def route_put_post():
    try:
        data = request.get_json()  # 요청으로부터 JSON 데이터를 가져옵니다.
        new_post = {
            'id': data['id'],
            'title': data['title'],
            'contents': data['contents']
        }
        if get_post(data['id']):
            return json.jsonify({'error': '이미 존재하는 포스트입니다.'}), 400
        put_post(new_post)  # 새로운 게시물을 데이터베이스에 추가합니다.
        return json.jsonify({'message': '게시물이 성공적으로 추가되었습니다.'}), 201  # 성공적으로 게시물을 추가한 경우 201 상태 코드를 반환합니다.
    except KeyError:
        return json.jsonify({'error': '요청 데이터가 올바르지 않습니다.'}), 400  # 요청 데이터가 올바르지 않은 경우 400 상태 코드를 반환합니다.
    except Exception as e:
        print(f'route_put_post 에러: {e}')
        return json.jsonify({'error': '서버 오류입니다.'}), 500  # 서버에서 오류가 발생한 경우 500 상태 코드를 반환합니다.