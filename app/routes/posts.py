from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.routes.auth import get_current_user
from app.schemas.posts import GetPosts, CreatePost, DeletePost
from app.database import Post
from app.utils.get_posts_query import get_all_posts_query

router = APIRouter(prefix="/posts", tags=["post"])

@router.post("/create/", response_model=CreatePost)
async def create_post(post: CreatePost, db: Session = Depends(get_db), token: str = Depends(get_current_user)) -> CreatePost:
    """Create a new post"""
    new_post = Post(
        content=post.text,
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)    
    return new_post

@router.get("/get/", response_model=GetPosts)
async def get_posts(db: Session = Depends(get_db), token: str = Depends(get_current_user)) -> GetPosts:
    """Get all posts"""
    posts = get_all_posts_query(db)
    return posts


@router.delete("/delete/", response_model=DeletePost)
async def delete_post(post: DeletePost, db: Session = Depends(get_db), token: str = Depends(get_current_user)) -> DeletePost:
    """Delete a post"""
    post = db.query(Post).filter(Post.id == post.id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    
    db.delete(post)
    db.commit()
    return post


