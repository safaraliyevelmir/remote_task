from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from app.database.dependencies import Base


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    password: Mapped[str] = mapped_column()

    created_at: Mapped[datetime] = mapped_column(default=func.now())
    updated_at: Mapped[datetime] = mapped_column(default=func.now(), onupdate=func.now())

    def __repr__(self) -> str:
        return f'<User {self.email}>'
