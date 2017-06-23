# Logs Analysis

### Requirements

This project includes a [Vagrant](https://www.vagrantup.com/) virtual environment and [VirtualBox](https://www.virtualbox.org/). To use it, install VirtualBox and (Vagrant).<a href="https://www.vagrantup.com/downloads.html">This </a>is the link you need to go to.
To Import modules you have to make Environmental Variable environment. <a href="http://hanzratech.in/2015/01/16/setting-up-flask-in-ubuntu-14-04-in-virtual-environment.html">Here </a>is the Link to make one.

### Steps

Once you have installed Vagrant and VirtualBox, Open CLI and follow the following Steps.

```
$ git clone https://github.com/Aadit-Bhojgi/Log-Analysis.git
$ vagrant up
$ vagrant ssh
$ cd /vagrant
```
#### 1st Choice:
To make a server and then accessing it, run `Project_Tool.py` file:
```
$ python Project_Tool.py
* Running on http://0.0.0.0:8000/ (Press CTRL+C to quit)
```
Then, go to you browser and type `https://localhost:8000/`

#### 2nd Choice:
Now, If you want to just run `Project_Tool_DB.py` file then make the changes mentioned 
in the comments of the file and run:
```
$ python Project_Tool_DB.py > Result.txt
```

### Create Views

#### article_view

```
$ CREATE VIEW article_view AS
SELECT articles.title, 
COUNT(CASE WHEN log.status LIKE '%200 OK%' THEN 1 END) AS views
FROM articles LEFT JOIN log
ON log.path LIKE '%' || articles.slug || '%'
GROUP BY articles.title
ORDER BY views DESC;
```

#### author_view

```
$ CREATE VIEW author_view AS SELECT authors.name, COUNT(*) as vi 
from articles JOIN authors ON articles.author = authors.id 
JOIN log ON log.path LIKE ('%' || articles.slug || '%') 
WHERE log.status LIKE '200 OK' GROUP BY authors.name 
ORDER BY vi DESC;
```

#### date_view

```
$ CREATE VIEW date_view AS SELECT day, perc from 
(SELECT day, round((sum(requests)/(select count(*) FROM log WHERE
substring(cast(log.time as text), 0, 11) = day) * 100), 2) as
perc from (select substring(cast(log.time as text), 0, 11) as day, 
count(*) as requests from log where status like '404 NOT FOUND' group by day)
as log_percentage group by day order by perc desc) as final_query
where perc >= 1;
```

