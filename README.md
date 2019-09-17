# Project 1. Log Analysis - Udacity
### Full Stack Web Development ND
_______________________

##Required softwares:
* python
* psycopg2 - sudo apt-get install python-psycopg2
* PostgreSQL

## Install VM:

to bring up the vm: vagrant up
then log into: vagrant ssh

## Downloads the data:
unzip the file and put newsdata.sql into vagrant dir: \Downloads\fsnd-virtual-machine\FSND-Virtual-Machine\vagrant

to load data : psql -d news -f newsdata.sql

## to run the query: psql -d news

### Query 1:
news=> select articles.title as article, count (*) as views from articles,log where log.path = '/article/' || articles.slug group by articles.title order by views desc limit 3;
             article              | views
----------------------------------+--------
 Candidate is jerk, alleges rival | 338647
 Bears love berries, alleges bear | 253801
 Bad things gone, say good people | 170098
(3 rows)

### Query 2:
news=> select  authors.name as author, count(*) as views from authors, log, articles  where log.path = '/article/' ||articles.slug and articles.author=authors.id group by authors.name order by views desc;
         author         | views
------------------------+--------
 Ursula La Multa        | 507594
 Rudolf von Treppenwitz | 423457
 Anonymous Contributor  | 170098
 Markoff Chaney         |  84557
(4 rows)

### Query 3:
news=> select to_char(date,'Mon DD, YYYY') as date, (count(*)*100.0) / requests.total_requests  as errors from log , (select time::date as date, count(*) as total_requests from log group by time::date) as requests where log.time::date= requests.date and log.status <> '200 OK' group by date,requests.total_requests having (log.count*100.0)/requests.total_requests > 1 ;
     date     |       errors
--------------+--------------------
 Jul 17, 2016 | 2.2626862468027260
(1 row)

## put the project1-log-analysis.py file into vagrant dir
## run python project1-log-analysis.py > output.txt



