from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from Shoes_Setup import *

engine = create_engine('sqlite:///shoes.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
session = DBSession()

# Delete ComputerCompanyName if exisitng.
session.query(ShoeCompanyName).delete()
# Delete ComputerNames if exisitng.
session.query(ShoeNames).delete()
# Delete User if exisitng.
session.query(User).delete()

# Create sample users data
User1 = User(name="SK BABA MALIK HUSSAIN",
             email="babamalik206@gmail.com",
             picture='malik.jpg')
session.add(User1)
session.commit()
print ("Successfully Add First User")
# Create sample computer companys
Scn1 = ShoeCompanyName(name="BATA",
                       user_id=1)
session.add(Scn1)
session.commit()

Scn2 = ShoeCompanyName(name="PUMA",
                       user_id=1)
session.add(Scn2)
session.commit

Scn3 = ShoeCompanyName(name="ADIDAS",
                       user_id=1)
session.add(Scn3)
session.commit()

Scn4 = ShoeCompanyName(name="NIKE",
                       user_id=1)
session.add(Scn4)
session.commit()

Sc5 = ShoeCompanyName(name="RED TAPE",
                      user_id=1)
session.add(Sc5)
session.commit()

Scn6 = ShoeCompanyName(name="REEBOK",
                       user_id=1)
session.add(Scn6)
session.commit()

# Populare a Shoes with models for testing
# Using different users for Shoes names year also
Sn1 = ShoeNames(name="Bata Formal",
                sole="leather",
                closure="Lace-Up",
                material="synthetic leather ",
                lifestyle="Sports",
                price="149,990",
                date=datetime.datetime.now(),
                shoecompanynameid=1,
                user_id=1)
session.add(Sn1)
session.commit()

Sn2 = ShoeNames(name="PUMA",
                sole="leather",
                closure="Lace-Up",
                material="synthetic leather ",
                lifestyle="Sports",
                price="149,990",
                date=datetime.datetime.now(),
                shoecompanynameid=2,
                user_id=1)
session.add(Sn2)
session.commit()

Sn3 = ShoeNames(name="ADIDAS",
                sole="leather",
                closure="Lace-Up",
                material="synthetic leather ",
                lifestyle="Sports",
                price="149,990",
                date=datetime.datetime.now(),
                shoecompanynameid=3,
                user_id=1)
session.add(Sn3)
session.commit()

Sn4 = ShoeNames(name="NIKE",
                sole="leather",
                closure="Lace-Up",
                material="synthetic leather ",
                lifestyle="Sports",
                price="149,990",
                date=datetime.datetime.now(),
                shoecompanynameid=4,
                user_id=1)
session.add(Sn4)
session.commit()

Sn5 = ShoeNames(name="RED TAPE",
                sole="leather",
                closure="Lace-Up",
                material="synthetic leather ",
                lifestyle="Sports",
                price="149,990",
                date=datetime.datetime.now(),
                shoecompanynameid=5,
                user_id=1)
session.add(Sn5)
session.commit()

Sn6 = ShoeNames(name="REEBOK",
                sole="leather",
                closure="Lace-Up",
                material="synthetic leather ",
                lifestyle="Sports",
                price="149,990",
                date=datetime.datetime.now(),
                shoecompanynameid=6,
                user_id=1)
session.add(Sn6)
session.commit()

print("Your Shoe database has been inserted!")
