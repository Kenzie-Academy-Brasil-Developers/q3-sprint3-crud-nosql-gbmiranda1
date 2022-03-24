from app.routes.post_routes import posts_routes

def init_app(app):
    posts_routes(app)