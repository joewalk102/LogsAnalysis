# "Database code" for the DB news.
import psycopg2

DBNAME = "news"


def _query_news(query):
    """
    Generic query method that will take any query passed to it and get the result
    :param query: query to use on database.
    :return: query result
    """
    # TODO: query checking to ensure no SQL injection attack
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result


def get_popular_articles():
    """Return top 3 articles from the database"""
    query = """
    SELECT articles.title, viewcount.views
    FROM articles
    JOIN (
      SELECT path, COUNT(path) AS views
      FROM log
      WHERE path LIKE '%article%'
      GROUP BY path
      ORDER BY views DESC
      LIMIT 3) AS viewcount
    ON articles.slug = SUBSTRING(viewcount.path, articles.slug)
    ORDER BY viewcount.views DESC;
    """
    return _query_news(query)


def get_all_article_count():
    """Return all articles from the database with title and view count"""
    query = """
    SELECT SUM(viewcount.views) AS authorViews, authors.name
    FROM articles
    JOIN (
      SELECT path, COUNT(path) AS views
      FROM log
      WHERE path LIKE '%article%'
      GROUP BY path) AS viewcount
    ON articles.slug = SUBSTRING(viewcount.path, articles.slug)
    JOIN authors ON articles.author = authors.id
    GROUP BY authors.name
    ORDER BY authorViews DESC;"""
    return _query_news(query)


def get_error_requests():
    """getting the error percent for any day where the error was above 1%"""
    query = """
    SELECT to_char(allTraffic.date, 'DD Mon YYYY'), to_char(allTraffic.percent, '99D99')
    FROM(
        SELECT logErrors.eDate AS date, ((CAST(logErrors.eCount AS REAL) / CAST(logTotal.tCount AS REAL)) * 100.0) AS percent
        FROM(
          SELECT DATE("log".time) AS eDate, COUNT("log".time) AS eCount
          FROM "log"
          WHERE status NOT LIKE '200%'
          GROUP BY DATE("log".time)) AS logErrors
        JOIN(
          SELECT DATE("log".time) AS tDate, COUNT("log".time) AS tCount
          FROM "log"
          GROUP BY DATE("log".time)) AS logTotal
        ON logErrors.eDate = logTotal.tDate) AS allTraffic
    WHERE allTraffic.percent > 1
    """
    return _query_news(query)

#_____________________________________________
# Unused method. Used for testing.
#_____________________________________________
def get_article(slug):
    query = """
    SELECT title
    FROM articles
    WHERE slug LIKE ('%{0}');""".format(slug)
    return _query_news(query)
