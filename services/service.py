from database.database import init_db,get_session,get_engine
from sqlmodel import Session,select
from model.models import BookData

engine = get_engine()

def get_all():
    with Session(engine) as session:
        record = session.exec(select(BookData)).all()
        return record
    
def get_book_id(id):
    with Session(engine) as session:
        record = session.get(BookData,id)
        return record
    
def add_book(book):
    with Session(engine) as session:
        session.add(book)
        session.commit()
        session.refresh(book)
        return book
    
def delete_book(id):
    with Session(engine) as session:
        record = session.get(BookData,id)
        session.delete(record)
        session.commit()
        
def update_book(id, updated_data):
    with Session(engine) as session:
        record = session.get(BookData,id)
        record.Description = updated_data.Description
        session.add(record)
        session.commit()
        session.refresh(record)
        return record