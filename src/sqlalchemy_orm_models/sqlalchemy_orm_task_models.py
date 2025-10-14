from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """
    Базовый класс для ORM-моделей SQLAlchemy.

    Используется как точка входа для декларативного стиля описания таблиц.
    Все ORM-модели приложения должны наследоваться от этого класса
    """


class TaskOrm(Base):
    __tablename__ = "tasks"

    task_id: Mapped[int] = mapped_column(primary_key=True)
    task: Mapped[str]
    description: Mapped[str | None]
    user_id: Mapped[int]
    status: Mapped[str]
    deadline: Mapped[datetime | None]
    # как сделать выбор в поле из неск вариантов
