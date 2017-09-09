import query


def find_top_articles():
    # getting the three most popular articles from the log
    popular_list = query.get_popular_articles()
    # cycle through all results
    for article in popular_list:
        # print the result
        print(article[0] + " - " + str(article[1]) + " views")


def find_top_authors():
    # getting views by author, ordered by most viewed to least viewed
    results = query.get_all_article_count()
    # cycle through all results
    for result in results:
        # print the result
        print(str(result[1]) + " - " + str(result[0]) + " views")


def find_error_percentage():
    # getting the error percent for any day where the error was above 1%
    results = query.get_error_requests()
    # cycle through all results
    for result in results:
        # print the result
        print(str(result[0]) + " - " + str(result[1]) + "% errors")


if __name__ == '__main__':
    # Running the methods
    print("Finding the top 3 most popular articles:\n")
    find_top_articles()
    print("\nFinding the total views, grouped by author:\n")
    find_top_authors()
    print("\nFinding the percent of errors, by day, where the error count is above 1%\n")
    find_error_percentage()
