from fastapi import FastAPI
from db import Session, User, Book
from pydantic import BaseModel
from sqlalchemy import select
from fastapi.exceptions import HTTPException

app = FastAPI()

class User_Data(BaseModel):
    login: str
    password: str
    age: str
    
class Book_Data(BaseModel):
    author:str
    name: str
    price: float



@app.get("/users", response_model=list[User_Data])
def get_users(skip:int = 0, limit:int = 0):
    with Session.begin() as session:
        users = session.scalars(select(User)).offset(skip).limit(limit).all()
        return users
        


@app.post("/create_user")
def create_user(user: User_Data):
    with Session.begin() as session:
        user = User(**user.model_dump())
        session.add(user)
        return user
    

@app.put("/user/{user_id}")
def update_user(user_id: int, user:User_Data):
    with Session.begin() as session:
        current_user = session.scalar(select(User).where(User.id == user_id))
        if user:
            current_user.login = user.login
            current_user.password = user.password
            current_user.age = user.age
            return current_user
        raise HTTPException(status_code=400, detail="Invalid User")
            
        
        


@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    with Session.begin() as session:
        current_user = session.scalar(select(User).where(User.id == user_id))
        session.delete(current_user)
        return "User deleted"



@app.get("/books")
def get_books():
    with Session.begin() as session:
        books = session.scalars(select(Book)).all()
        return books
    

@app.post("/create_books")
def create_book(book: Book_Data):
    with Session.begin() as session:
        book = Book(**book.model_dump())
        session.add(book)
        return book


@app.put("/book/{book_id}")
def update_book(book_id: int, book: Book_Data):
    with Session.begin() as session:
        current_book = session.scalar(select(Book).where(Book.id == book_id))
        if book:
            current_book.author = book.author
            current_book.name = book.name
            current_book.price = book.price
            return current_book
        raise HTTPException(status_code=400, detail="Invalid Book Data")
        

@app.delete("/book/{book_id}")
def delete_book(book_id: int):
    with Session.begin() as session:
        current_book = session.scalar(select(Book).where(Book.id == book_id))
        session.delete(current_book)
        return "book deleted"