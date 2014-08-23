#Dave and Dino's script for hw7
#creates databases for scraping data and twitter api data

import pandas as pd
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_, or_
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy import *
import time

#scraping data

data = pd.read_csv("https://raw.githubusercontent.com/dinohadzic/python-washu-2014/master/hw5/mathofpolitics.csv") #csv from hw5

engine = sqlalchemy.create_engine('sqlite:////Users/dinohadzic/python-washu-2014/hw7/scrape_database.db', echo=False)

Base = declarative_base() 

class Blog(Base): #table for blog posts
    __tablename__ = 'blog_post'
    id = Column(Integer, primary_key=True)
    url = Column(String)
    is_post = Column(Integer)
    publish_date = Column(String)
    author = Column(String)
    post_title = Column(String)
    comment_count = Column(Integer)
    source_id = Column(Integer, ForeignKey('sources.id')) #points to source of blog
    def __init__(self, url, is_post, publish_date, author, post_title, comment_count):
        self.url = url
        self.is_post = int(is_post)
        self.publish_date = str(publish_date)
        self.author = str(author)
        self.post_title = post_title.decode('ascii','ignore')
        self.comment_count = int(comment_count)
    def __repr__(self):
        if self.is_post == 0: return 'Not a post. URL: %s' %self.url
        else:
            return 'name: %s\nURL: %s'%(self.post_title, self.url)


class Source(Base): #stores source of blogs
    __tablename__ = 'sources'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    url = Column(String)
    blogs = relationship("Blog") #relationship to blogs from source
    def __init__(self, name, url):
        self.name = name
        self.url = url
    def __repr__(self):
        return 'name: %s\nurl: %s' %(self.name, self.url)
      
  

Base.metadata.create_all(engine) 
Session = sessionmaker(bind=engine)
session = Session()


patty = Source('The Math of Politics', 'http://www.mathofpolitics.com/') #initialize a source
session.add(patty) #add instance
blogs=[] #list to store blogs
for i in range(data.count()[0]): #loop through rows, add an instance of Blog to list
    if data.loc[i, 'is_post']==0: #means not a blog
        blogs.append(Blog(data.loc[i, 'url'], data.loc[i, 'is_post'], 'None', 'None', 'None', 0))
    else: blogs.append(Blog(data.loc[i, 'url'], data.loc[i, 'is_post'], data.loc[i, 'publish_date'], data.loc[i, 'author'], data.loc[i, 'post_title'], data.loc[i, 'comment_count']))
    patty.blogs.append(blogs[i]) #append the blog to the source instance


session.add_all(blogs) #add all the blogs

session.commit()

#twitter data

engine = sqlalchemy.create_engine('sqlite:////home/david/python-washu-2014/hw7/twitter_database.db', echo=False)

Base = declarative_base() 


class Users(Base): #table to store user info - num of followers and num of tweets (activity measure)
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    number_followers = Column(String)
    number_tweets = Column(Integer)
    crawl_id = Column(Integer, ForeignKey('crawls.id')) #points to crawl instance
    def __init__(self, name, number_followers, number_tweets):
        self.name = name
        self.number_followers = number_followers
        self.number_tweets = number_tweets
    def __repr__(self):
        return 'name: %s\nNumber of followers: %s\nNumber of Tweets: %s' %(self.name, self.number_followers, self.number_tweets)


class Crawls(Base): #stores crawl info - starting user and date/time of start
    __tablename__ = 'crawls'
    id = Column(Integer, primary_key=True)
    starting_user = Column(String)
    time_begin = Column(String)
    users = relationship("Users")
    def __init__(self, starting_user):
        self.starting_user = starting_user
        time_begin = time.strftime("%d/%m/%Y - %H:%M:%S") #date and time at point of initialization
    def __repr__(self):
        return 'Beginning user: %s\nStart date - time: %s'%(self.starting_user, self.time_begin)


Base.metadata.create_all(engine) 
Session = sessionmaker(bind=engine)
session = Session()


#api set on different code

henry_crawl_follower = Crawls('Henry Hackney') #initializes crawl

session.add(henry_crawl_follower) #adds instance

people = api.followers_ids('Atticushack')+api.friends_ids('Atticushack') # Extract IDs for Henry's followers and friends
people = list(set(people)) #extract unique user ids
userlist = []
i=0
while i<len(people): # Code below loops through all users who follow and are followed by Henry
    try:
        user = api.get_user(people[i])
        userlist.append(Users(user.name.encode('ascii','ignore'), user.followers_count, user.statuses_count))
        i+=1
    except: time.sleep(.25) # Should we hit the limit, waits 0.25 seconds before making another request. Permits for loop to remain active until limit is reset.


session.add_all(userlist) #add users

session.commit()

