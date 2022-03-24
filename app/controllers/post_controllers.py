from flask import jsonify, request
from app.model.post_model import Posts
from http import HTTPStatus

def get_posts():
    posts_list = list(Posts.get_post_all())
    for post in posts_list:
        post.update({"_id": post["_id"]})
        del post['_id']
    return jsonify(posts_list), HTTPStatus.OK

def post_posts():
    data = request.get_json()
    try:
        post = Posts(**data)
        Posts.create_post(post)
        post._id = str(post._id)
        post = post.__dict__
        del post['_id']
        return jsonify(post), HTTPStatus.OK
    except (AttributeError, TypeError):
        return {"error": "correct the values"}, HTTPStatus.BAD_REQUEST

def remove_post(post_id):
    try:
        remove_post = Posts.delete_post(post_id)
        del remove_post['_id']
        return jsonify(remove_post), HTTPStatus.OK
    except:
        return {"error": "id Not Found"}, HTTPStatus.NOT_FOUND

def get_by_id_post(post_id):

    try:
        post = Posts.filter_post(post_id)
        del post['_id']
        return jsonify(post), HTTPStatus.OK
    except:
        return {"error": "id Not Found"}, HTTPStatus.NOT_FOUND

def update_post(post_id):
    data = request.get_json()
    try:
        post = Posts.update_post(post_id, data)
        post.update({"_id": str(post["_id"])})
        del post['_id']
        return jsonify(post), HTTPStatus.OK
    except:
        return {"error": "id Not Found"}, HTTPStatus.NOT_FOUND
