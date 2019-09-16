#!/usr/bin/env python3

# connecting to database from the code
import psycopg2
db = psycopg2.connect("dbname=news")
cur = db.cursor()


# 1. What are the most popular three articles of all time?
def most_popular_articles():
    query = '''
	select articles.title as article, count (*) as views 
	from articles,log where log.path = '/article/' || articles.slug 
	group by articles.title 
	order by views desc 
	limit 3;
    	'''
    cur.execute(query)
    resultset = cur.fetchall()
    print("1. What are the most popular the=ree articles of all time? :\n")
    for (article, views) in resultset:
        print('\t"{}" - {} views'.format(article, views))
    print("\n\n")

# 2. Who are the most popular article authors of all time? 
def most_popular_authors():
    query = '''
	select authors.name as Author, count (*) as views 
	from authors,articles,log where log.path = '/article/' || articles.slug and authors.id = articles.author 
	group by authors.name order by views desc;
	'''

    cur.execute(query)
    resultset = cur.fetchall()
    print("2. Who are the most popular article authors of all time? :\n")
    for (author, views) in resultset:
        print('\t{} - {} views'.format(author, views))
    print("\n\n")

# 3. On which days did more than 1% of requests lead to errors?
def days_requests_lead_to_errors():
    query = '''
     select to_char(date,'Mon DD, YYYY') as date, (count(*)*100.0) / requests.total_requests  as errors from log , 
     (select time::date as date, count(*) as total_requests from log group by time::date) as requests 
     where log.time::date= requests.date and log.status <> '200 OK' 
     group by date,requests.total_requests having (log.count*100.0)/requests.total_requests > 1 ;
     '''

    cur.execute(query)
    resultset = cur.fetchall()
    print("3. On which days did more than 1% of requests lead to errors? :\n")
    for (day, errors) in resultset:
        print('\t{} - {}% errors'.format(day,errors))
    print("\n\n")


most_popular_articles()
most_popular_authors()
days_requests_lead_to_errors()

