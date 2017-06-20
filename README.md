# Logs Analysis

### Requirements

This project includes a [Vagrant](https://www.vagrantup.com/) virtual environment and [VirtualBox](https://www.virtualbox.org/). To use it, install VirtualBox and (Vagrant).<a href="https://www.vagrantup.com/">This </a>is the link you need to go to.
To Import modules you have to Environmental Variable. <a href="http://hanzratech.in/2015/01/16/setting-up-flask-in-ubuntu-14-04-in-virtual-environment.html">Here </a>is the Link to make one.

### Steps

Once you have installed Vagrant and VirtualBox, Open CLI and follow the following Steps.

```
$ git clone https://github.com/Aadit-Bhojgi/Log-Analysis.git
$ vagrant up
$ vagrant ssh
$ cd /vagrant
```
1st Choice:
To make a server and then accessing it, run:
```
python Project_Tool.py
* Running on http://0.0.0.0:8000/ (Press CTRL+C to quit)
```
Then, go to you browser and type `https://http://localhost:8000/`

Now, 2nd Choice
If you want to just run Project_Tool_DB.py file then make the changes mentioned 
in the comments of the file and run:
```

### Create Views

article_view

```
$ CREATE VIEW article_views AS
SELECT articles.title, 
COUNT(CASE WHEN log.status LIKE '%200 OK%' THEN 1 END) AS views
FROM articles LEFT JOIN log
ON log.path LIKE '%' || articles.slug || '%'
GROUP BY articles.title
ORDER BY views DESC;

```

query_2

```
$ CREATE VIEW query_2 AS SELECT authors.name, COUNT(*) 
AS vi FROM articles 
JOIN authors on articles.author = authors.id JOIN log 
ON log.path LIKE concat('%', articles.slug, '%') where 
log.status LIKE '%200%' GROUP BY authors.name ORDER BY vi DESC")
```

query_3

```
$

