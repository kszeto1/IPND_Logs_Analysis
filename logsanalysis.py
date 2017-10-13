import psycopg2

# Connect to database named 'news'

def fetch_results(query):
    db = psycopg2.connect("news")
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    print results
    c.close()

"""CREATE VIEW most_viewed_articles as
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
        """



def most_viewed():
    """What are the most popular three articles of all time?"""
    print "The three most popular articles of all time:"
    query1 = "SELECT * FROM most_viewed_articles limit 3;"
    import pdb
    pdb.set_trace()
    fetch_results(query1)

def most_popular_author():
    """Who are the most popular article authors of all time?"""

def most_error_day():
    """On which days did more than 1% of requests lead to errors?"""

most_viewed()