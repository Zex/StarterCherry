#!/usr/bin/env python

def show(entry):
    print entry

def cmdshow(entry):
    print "-------", entry, "-------"

from sqlalchemy import create_engine

engine = create_engine('sqlite:///::memory::', echo=True)
cmdshow(dir(engine))

cmdshow(engine.url)

from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()
cmdshow(dir(base))

from sqlalchemy import Column, Integer, String

class User(base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)

cmdshow(User.__table__)

base.metadata.create_all(engine)

user1 = User(name='user1', fullname='user1 X', password='333777')

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
#Session = sessionmake()
#Session.configure(bind=engine)

cmdshow(type(Session))

session = Session()

cmdshow(dir(session))
cmdshow("session.add(user1)")
session.add(user1)
cmdshow("que = session.query(User)")
que = session.query(User)
cmdshow("que.count()")
que.count()
cmdshow("que.filter_by(name='user1')")
cmdshow(que.filter_by(name='user1'))
cmdshow("que.filter_by(name='user1').all()")
cmdshow(que.filter_by(name='user1').all())



