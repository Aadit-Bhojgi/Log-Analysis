#!/usr/bin/env python3

from flask import Flask

from Project_Tool_DB import query_1, query_2, query_3

app = Flask(__name__)

html = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>Queries</title>
    <style>
      h1, h4, div { text-align: center; }
      div { margin: auto; }
    </style>
  </head>
  <body>
    <h1>Queries Result</h1><br>
    <h4>1. What are the most popular three articles of all time?</h4>
        <div>%s</div>
    <h4>2. Who are the most popular article authors of all time?</h4>
        <div>%s</div>
    <h4>3. On which days did more than 1 percent of requests lead to 
    errors?</h4>
         <div>%s</div>
  </body>
</html>
'''


@app.route('/', methods=['GET'])
def main():
    """Main page of QUERY"""
    content_1 = query_1()
    content_2 = query_2()
    content_3 = query_3()
    return html % (content_1, content_2, content_3)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
