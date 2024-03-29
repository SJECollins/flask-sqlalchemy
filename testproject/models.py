from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from testproject import db


class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String, nullable=False)
