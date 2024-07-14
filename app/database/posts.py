from datetime import datetime
from sqlalchemy import ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.dependencies import Base


class Post(Base):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    text: Mapped[str] = mapped_column(String(1000), nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=func.now())
    author_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    author = relationship("User", back_populates="posts")
