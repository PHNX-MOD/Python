from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime, Integer
from datetime import datetime


Base = declarative_base()

"""
Class = User
id int
username str
email str
date_created datetime"""

class User(Base):
  __tablename__ = 'users'
  id=Column(Integer(), primary_key=True)
  username=Column(String(25),nullable=False, unique=True)
  email=Column(String(80),unique=True, nullable= False)
  date_created = Column(DateTime(), default=datetime.utcnow)

  def __repr__(self):
    return f"<User username{self.username} email={self.email}>"




new_user=User(id=1,username="modith", email="modithross")
print(new_user)