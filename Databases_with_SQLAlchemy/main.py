from sqlalchemy import declarative_base
from datetime import datetime

Base = declarative_base()

"""
Class = User
id int
username str
email str
date_created datetime"""

class user(Base):
  __tablename__ = 'users'
  id=
