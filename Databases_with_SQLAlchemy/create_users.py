from main import User,Session,engine
import csv
import json 


def import_data_from_csv("csvFilePath"):

  with open()



local_session=Session(bind=engine)

new_user = User(id=1, username="test1", email="test1@gmail.com")

local_session.add(new_user)
local_session.commit()
