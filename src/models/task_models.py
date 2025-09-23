from typing import Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime


class Base(DeclarativeBase):
    pass


class TaskOrm(Base):
    __tablename__ = "tasks"

    task_id: Mapped[int] = mapped_column(primary_key=True)
    task: Mapped[str]
    description: Mapped[Optional[str]]
    user_id: Mapped[int]
    status: Mapped[str]
    deadline: Mapped[Optional[datetime]]
    # как сделать выбор в поле из неск вариантов
