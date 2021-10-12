from main import User, Session, engine

local_session = Session(bind=engine)


# retrieving for user in users:
#users = local_session.query(User).all()[:3]

#for user in users:
 #   print(user.username)

#quesiy for one specific object
test12 = local_session.query(User).filter(User.username=="test12").first()
print(test12)


