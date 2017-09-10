#!/usr/bin/python3

import query


def find_top_articles():
    print("Finding the top 3 most popular articles:\n")
    # getting the three most popular articles from the log
    popular_list = query.get_popular_articles()
    # cycle through all results
    for article, views in popular_list:
        # print the result
        print(str(article) + " - " + str(views) + " views")


def find_top_authors():
    print("\nFinding the total views, grouped by author:\n")
    # getting views by author, ordered by most viewed to least viewed
    results = query.get_all_article_count()
    # cycle through all results
    for author, views in results:
        # print the result
        print(str(author) + " - " + str(views) + " views")


def find_error_percentage():
    print("\nFinding the percent of errors, by day, where the error count is above 1%\n")
    # getting the error percent for any day where the error was above 1%
    results = query.get_error_requests()
    # cycle through all results
    for date, percent in results:
        # print the result
        print(str(date) + " - " + str(percent) + "% errors")


if __name__ == '__main__':
    # Running the methods
    find_top_articles()
    find_top_authors()
    find_error_percentage()
