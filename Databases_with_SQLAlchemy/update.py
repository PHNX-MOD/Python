from main import Session, User, engine

local_session = Session(bind=engine)

user_to_update = local_session.query(User).filter(User.username == "test12").first()

user_to_update.username = "test_changed_user"
user_to_update.email = "changed_test12@gmail.com"

local_session.commit()