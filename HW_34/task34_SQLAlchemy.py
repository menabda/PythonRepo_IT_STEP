# შექმენით User და Profile ცხრილი, დაამატეთ 5 ჩანაწერი თითოეულისთვის. 
# დაწერეთ sqlalchemy გამოყენებით:

# User ცხრილი:
# 	id (Primary Key, Integer, Auto-increment)
# 	username (String, Unique, Not Null)
# 	email (String, Unique, Not Null)

# Profile ცხრილი:
# 	id Primary Key
# 	user_id მეორადი გასაღები მომხარებლების ცხრილზე ((Foreign Key to User's id)
# 	bio String
# 	profile_picture String

# დაიმახსოვრეთ უნდა გქონდეთ one-to-one relationship

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('mysql+mysqlconnector://root:123asdASD@localhost/it_step_db')
Session = sessionmaker(bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    profiles = relationship('Profile', backref='user', cascade='all, delete-orphan')

class Profile(Base):
    __tablename__ = 'Profile'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    bio = Column(Text)
    profile_picture = Column(String(255))


Base.metadata.create_all(engine)


with Session() as session:
    
    user_data = [
        User(username="Daviti", email="daviti@gmail.com"),
        User(username="Giorgi", email="giorgi@gmail.com"),
        User(username="Armazi", email="armazi@gmail.com"),
        User(username="Vano", email="vano@gmail.com"),
        User(username="Beqa", email="beqa@gmail.com")
    ]
    session.add_all(user_data)
    session.commit()

    profile_data = [
        Profile(user_id=1, bio="Bio for Daviti", profile_picture="daviti.jpg"),
        Profile(user_id=2, bio="Bio for Giorgi", profile_picture="giorgi.jpg"),
        Profile(user_id=3, bio="Bio for Armazi", profile_picture="armazi.jpg"),
        Profile(user_id=4, bio="Bio for Vano", profile_picture="vano.jpg"),
        Profile(user_id=5, bio="Bio for Beqa", profile_picture="beqa.jpg")
    ]
    session.add_all(profile_data)
    session.commit()
