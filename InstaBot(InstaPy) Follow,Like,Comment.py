# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 16:48:32 2017

@author: shaur
"""
#Install Instapy First before proceeding
from instapy import InstaPy

insta_username = 'test'
insta_password = 'test'

# if you want to run this script on a server,
# simply add nogui=True to the InstaPy() constructor
session = InstaPy(username=insta_username, password=insta_password)
session.login()

session.set_do_comment(enabled=True,percentage=15)
session.set_comments(['Awesome','Nicey','Lovely','I like it','Looks Good'])
session.set_do_follow(enabled=True,percentage=5)


session.like_by_tags(['delhifood','foodstalker','foodkiss','japanfood','usafood','indiafood','yummy','foodporn','recipe','coffee','foodie','pizza','#foodlove'],amount=30)
session.set_dont_like(['girl','boy','human','animal','pet','object','thing','shop','instagramer','insta'])


session.unfollow_users(amount=10,onlyNotFollowMe=True,onlyInstapyMethod="FIFO",sleep_delay=80)

session.end()