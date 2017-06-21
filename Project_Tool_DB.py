#!/usr/bin/env python3
"""This is the file connecting us with the database in our 
system For now the queries will be sent to the server File
(Project_Tool_DB.py) to print these files jus run the COMMAND 
below file, the code you need is in the comments Below Though 
I have also provided a text File of the Outputs.
NOTE: (It will Take some time to open your localhost link
because of the Queries.)
Command: python Project_Tool_DB.py > Result.txt
Run This command after Making the above changes.
"""
import psycopg2

Db_name = "vagrant"


def query_1():
    """Return query 1 from the 'DATABASE: vagrant'."""
    db = psycopg2.connect(database=Db_name)
    c = db.cursor()
    # article_view here is a VIEW (Query for this is in README.md)
    c.execute("""SELECT * FROM article_view LIMIT 3""")
    query_result = c.fetchall()
    db.close()
    data = ''
    for (title, count) in query_result:
        data = data + "Article: '{}', Views: {}<br>".format(title, count)
    return data
    # print data


def query_2():
    """Return query 2 from the 'DATABASE: vagrant'."""
    db = psycopg2.connect(database=Db_name)
    c = db.cursor()
    # query_2 here is a VIEW (Query for this is in README.md)
    c.execute("""SELECT * FROM author_view""")
    query_result = c.fetchall()
    db.close()
    data = ''
    for (title, count) in query_result:
        data = data + "Author: '{}', Views: {}<br>".format(title, count)
    return data
    # print data


def query_3():
    """Return query 2 from the 'DATABASE: vagrant'."""
    db = psycopg2.connect(database=Db_name)
    c = db.cursor()
    # query_3 here is a VIEW (Query for this is in README.md)
    c.execute("""SELECT * FROM date_view""")
    query_result = c.fetchall()
    db.close()
    data = "Date: {}, Percentage: {}%".format(query_result[0][0], query_result[0][1])
    return data
    # print data


'''print "Q1. What are the most popular three articles of all time?\n"
query_1()
print "Q2. Who are the most popular article authors of all time?\n"
query_2()
print "Q3. On which days did more than 1 percent of requests lead to errors?\n"
query_3()'''
