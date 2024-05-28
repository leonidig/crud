from .. import Base
from sqlalchemy.orm import Mapped

class Book(Base):
    __tablename__ = 'books'

    author: Mapped[str]
    name: Mapped[str]
    price: Mapped[float]