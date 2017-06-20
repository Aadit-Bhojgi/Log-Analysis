#!/usr/bin/env python3

import psycopg2

Db_name = "vagrant"


def query_1():
    """Return query 1 from the 'DATABASE: vagrant'."""
    db = psycopg2.connect(database=Db_name)
    c = db.cursor()
    c.execute("""SELECT * FROM article_view LIMIT 3""")
    query_result = c.fetchall()
    db.close()
    data = ''
    for (title, count) in query_result:
        data = data + "Article: '{}', Views: {}<br>".format(title, count)
    return data
    #print data


def query_2():
    """Return query 2 from the 'DATABASE: vagrant'."""
    db = psycopg2.connect(database=Db_name)
    c = db.cursor()
    c.execute("""SELECT * FROM query_2""")
    query_result = c.fetchall()
    db.close()
    data = ''
    for (title, count) in query_result:
        data = data + "Author: '{}', Views: {}<br>".format(title, count)
    return data
    #print data


def query_3():
    """Return query 2 from the 'DATABASE: vagrant'."""
    db = psycopg2.connect(database=Db_name)
    c = db.cursor()
    c.execute("""SELECT * FROM query_3""")
    query_result = c.fetchall()
    db.close()
    data = "Date: {}, Percentage: {}%".format(query_result[0][0], query_result[0][1])
    return data
    #print data


"""print "Q1. What are the most popular three articles of all time?\n"
query_1()
print "Q2. Who are the most popular article authors of all time?\n"
query_2()
print "Q3. On which days did more than 1 percent of requests lead to errors?\n"
query_3()"""
