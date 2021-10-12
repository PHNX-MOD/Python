from main import Session, User, engine
from sqlalchemy import desc

local_session = Session(bind=engine)

#ascending
users_asc = local_session.query(User).order_by(User.username).all()

user_desc = local_session.query(User).order_by(desc(User.username)).all()


for user in user_desc:
    print(f"User {user.username}")