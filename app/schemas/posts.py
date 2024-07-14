from pydantic import BaseModel


class CreatePost(BaseModel):
    text: str

class GetPosts(BaseModel):
    id: int
    text: str
    author_id: int

class DeletePost(BaseModel):
    id: int
