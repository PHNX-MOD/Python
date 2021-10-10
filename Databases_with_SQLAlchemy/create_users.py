from main import User,Session,engine
import csv
import json 



"""local_session=Session(bind=engine)

new_user = User(id=1, username="test1", email="test1@gmail.com")

local_session.add(new_user)
local_session.commit()"""

 
data =[]

with open(r'TestData.csv',encoding='utf-8') as csvf:
  csvreader = csv.DictReader(csvf)

  for row in csvreader:
    data.append(row)

jsonString = json.dumps(data, indent=4)



for user in jsonString:
  new_user = User(username=user["username"], email=user["email"])





