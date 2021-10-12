from main import User, Session, engine

local_session = Session(bind = engine)

user_to_delete = local_session.query(User).filter(User.username=="test13").first()

local_session.delete(user_to_delete)

local_session.commit()