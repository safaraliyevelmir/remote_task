from cachetools.func import ttl_cache
from app.database import Post

@ttl_cache(maxsize=128, ttl=300)
def get_all_posts_query(db):
    """Get all posts from the database and cache the result"""
    posts = db.query(Post).all()
    return posts