from .. import Base
from sqlalchemy.orm import Mapped

class User(Base):
    __tablename__ = 'users'

    login: Mapped[str]
    password: Mapped[str]
    age: Mapped[str]