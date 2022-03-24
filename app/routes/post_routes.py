from turtle import pos
from app.controllers import post_controllers

def posts_routes(app):
    @app.get("/posts")
    def get_posts():
        return post_controllers.get_posts();

    @app.get("/posts/<int:post_id>")
    def get_post_by_id(post_id):
        return post_controllers.get_by_id_post(post_id)

    @app.post("/posts")
    def post_posts():
        return post_controllers.post_posts()
    
    @app.patch("/posts/<int:post_id>")
    def update_post(post_id):
        print(post_id)
        return post_controllers.update_post(post_id)
    
    @app.delete("/posts/<int:post_id>")
    def remove_post(post_id):
        return post_controllers.remove_post(post_id)