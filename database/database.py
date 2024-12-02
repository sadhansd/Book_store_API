from sqlmodel import Field, Session, SQLModel, create_engine, select
import pandas as pd
from model.models import BookData

sqlite_file_name = "database\db.sqlite"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)
    df = pd.read_csv("data\BooksDatasetClean.csv")
    df = df.head(10)
    with Session(engine) as session:
        for index,row in df.iterrows():
            record = BookData(Title=row['Title'],Authors=row['Authors'],Description=row['Description'],Category=row['Category'],Publisher=row['Publisher'],Price=row['Price Starting With ($)'],Publish_Month=row['Publish Date (Month)'],Publish_Date=row['Publish Date (Year)'])
            session.add(record)
        session.commit()

def get_session():
    with Session(engine) as session:
        yield session
        
def get_engine():
    return engine
