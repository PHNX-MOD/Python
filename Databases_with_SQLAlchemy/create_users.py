from main import User, Session, engine
import csv


data =[]
local_session=Session(bind=engine)

with open(r'TestData.csv',encoding='utf-8') as csvf:
  csvreader = csv.DictReader(csvf)

  for row in csvreader:
    data.append(row)

for user in data:
  new_user = User(username=user["username"], email=user["email"])
  local_session.add(new_user)
  local_session.commit()

  print(f"added",{user["username"]})


