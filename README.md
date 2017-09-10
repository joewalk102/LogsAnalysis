# LogsAnalysis
by Joe Walker\
Udacity Full Stack Web Developer Nanodegree

## Purpose
This python script and SQL queries pull the following information:
* Find top 3 articles
* Find how many views each author has in total
* Find percentage of errors by day over 1%

## Requirements
* Python3
* [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) from Udacity
* psycopg2 python package
* PostgreSQL with newsdata isntalled

## How To Use
1. import the news database using the newsdata.sql file and 'psql -d news -f newsdata.sql'
2. Connect to the machine running postgres with the news database
3. Run main.py
4. Informtion is output to the screen
