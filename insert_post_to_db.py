import sqlite3

from config import DATABASE


c = sqlite3.connect(DATABASE)
title = input("Enter post title> ")
slug = input("Enter post slug> ")
date = input("Enter post creation date (mm/dd/yyyy)> ")
filename = input("Enter filename containing post content> ")

with open(filename) as f:
    data = f.read()


cursor = c.cursor()
cursor.execute('insert into posts (title,created,content,slug) values (?,?,?,?)',(title, date, data, slug))
c.commit()
c.close()
