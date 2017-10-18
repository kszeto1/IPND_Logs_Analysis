# Udacity's IPND Log Analysis Project
This Log Analysis Project was assigned from Udacity's Intro to Programming Nanodegree (IPND), specifically the Back-End 
Development path. 

>Your task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. 
This reporting tool is a Python program using the psycopg2 module to connect to the database.

The reporting tool should answer the 3 following questions:
> 1. What are the most popular three articles of all time?
> 2. Who are the most popular article authors of all time?
> 3. On which days did more than 1% of requests lead to errors?

## Installation
1. Start by [installing VirtualBox]("https://www.virtualbox.org/wiki/Downloads"). Virtualbox is the software used 
specifically for running the virtual machine. Vagrant, in the following step 2, will run launch Virtualfox after
installing. 

2. [Install vagrant]("https://www.vagrantup.com/downloads.html"), the software that configures the virtual machine(VM)
and enables you to share files between your host computer and VM's filesystem.

3. [Download the VM configuration]("https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip").
This directory contains the VM files. After downloading it, change to this directory using your terminal with the 
**```cd```** command. Then change to the vagrant directory inside FSND-Virtual-Machine.

4. Start the virtual machine by running **```vagrant up```**. Vagrant downloads and installs the Linux operating system.
Give it a few minutes for this to complete. After **```vagrant up```** is finished, you can run **```vagrant ssh```** to
log in to the newly installed Linux VM.
   
5. Once inside the VM, change the directory to **```vagrant```** and use **```ls```** to look around.

6. Load the data from newsdata.sql by using **```psql -d news -f newsdata.sql```**. **THIS COMMAND ONLY NEEDS TO BE RUN ONCE!**
This is what each component of the command does:
* psql — the PostgreSQL command line program
* -d news — connect to the database named news which has been set up for you
* -f newsdata.sql — run the SQL statements in the file newsdata.sql ```

7. Type **```psql -d news```** to explore the database.

## Create the Following Views
Create the following views before running logsanalysis.py:

```
CREATE VIEW most_viewed_articles as
SELECT articles.title, count(log.path) as views
    FROM articles, log
    WHERE log.path LIKE '%' || articles.slug
    GROUP BY articles.title
    ORDER BY views desc;
        
CREATE VIEW most_popular_author as
SELECT authors.name, count(log.path) as author_views
    FROM authors, articles, log
    WHERE status != '404 NOT FOUND'
    AND articles.author = authors.id
    AND log.path LIKE '%' || articles.slug || '%'
    GROUP BY authors.name
    ORDER BY author_views desc;
        
CREATE VIEW errors_per_day as
SELECT to_char(log.time, 'FMMonth DD, YYYY') "day", count(log.status) as errors
    FROM log
    WHERE status = '404 NOT FOUND'
    GROUP BY 1
ORDER BY 1;
        
CREATE VIEW requests_per_day as
SELECT to_char(log.time, 'FMMonth DD, YYYY') "day", count(log.status) as requests
    FROM log
    GROUP BY 1
    ORDER BY 1;
        
CREATE VIEW day_with_most_errors as
SELECT errors_per_day.day, concat(ROUND((100.0 * errors_per_day.errors / requests_per_day.requests), 2), '%')as percent_errors
    FROM errors_per_day, requests_per_day
    WHERE errors_per_day.day = requests_per_day.day
    AND (((100.0 * errors_per_day.errors / requests_per_day.requests)) > 1)
    ORDER BY percent_errors desc;
```


8. After creating the above views in psql, you may exit PSQL by typing **```\q```**. This returns you to the vagrant directory
 inside the VM.
 
9. Typing **```python logsanalysis.py```** executes the logsanalysis.py file.
Logsanalysis.py executes SQL queries using the database file (newsdata.sql) and the views created to output answers to the 3 questions.


## References

* [https://discussions.udacity.com/t/log-analysis-nothing-is-working/249753/7?u=kszeto]("https://discussions.udacity.com/t/log-analysis-nothing-is-working/249753/7?u=kszeto")
* [https://www.postgresql.org/docs/8.1/static/functions-math.html]("https://www.postgresql.org/docs/8.1/static/functions-math.html")
* [https://www.postgresql.org/docs/9.1/static/functions-formatting.html]("https://www.postgresql.org/docs/9.1/static/functions-formatting.html")
* [https://www.postgresql.org/docs/9.5/static/functions-formatting.html]("https://www.postgresql.org/docs/9.5/static/functions-formatting.html")
* [https://www.postgresql.org/docs/9.6/static/functions-formatting.html]("https://www.postgresql.org/docs/9.6/static/functions-formatting.html")
* [https://pyformat.info/#simple]("https://pyformat.info/#simple")








