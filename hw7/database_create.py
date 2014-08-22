import pandas as pd
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_, or_
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy import *


data = pd.read_csv("https://raw.githubusercontent.com/dinohadzic/python-washu-2014/master/hw5/mathofpolitics.csv")

engine = sqlalchemy.create_engine('sqlite:////Users/dinohadzic/Documents/scrape_database.db', echo=False)

Base = declarative_base() 

class Blog(Base):
    __tablename__ = 'blog_post'
    id = Column(Integer, primary_key=True)
    url = Column(String)
    is_post = Column(Integer)
    publish_date = Column(String)
    author = Column(String)
    post_title = Column(String)
    comment_count = Column(Integer)
    source_id = Column(Integer, ForeignKey('sources.id'))
    def __init__(self, url, is_post, publish_date, author, post_title, comment_count):
        self.url = url
        self.is_post = int(is_post)
        if isinstance(publish_date, float): #means NaN and not a post
            self.publish_date = 'Not a post'
            self.author = 'Not a post'
            self.post_title = 'Not a post'
            self.comment_count = 0
        else:
            self.publish_date = str(publish_date)
            self.author = str(author)
            self.post_title = unicode(str(post_title), encoding='utf-8')
            self.comment_count = int(comment_count)
    def __repr__(self):
        if self.is_post == 0: return 'Not a post. URL: %s' %self.url
        else:
            return 'name: %s\nURL: %s'%(self.post_title, self.url)


class Source(Base):
    __tablename__ = 'sources'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    url = Column(String)
    blogs = relationship("Blog")
    def __init__(self, name, url):
        self.name = name
        self.url = url
    def __repr__(self):
        return 'name: %s\nurl: %s' %(self.name, self.url)
      
  

Base.metadata.create_all(engine) 
Session = sessionmaker(bind=engine)
session = Session()


patty = Source('The Math of Politics', 'http://www.mathofpolitics.com/')
session.add(patty)
blogs=[]
for i in range(data.count()[0]):
    blogs.append(Blog(data.loc[i, 'url'], data.loc[i, 'is_post'], data.loc[i, 'publish_date'], data.loc[i, 'author'], data.loc[i, 'post_title'], data.loc[i, 'comment_count']))
    patty.blogs.append(blogs[i])


session.add_all(blogs)

session.commit()
