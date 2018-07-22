#!/usr/bin/env python
import psycopg2


def get_pop_article():
    "Return the article that is the most popular"

    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("""
                select title, count
                from pop_articles
                order by count desc
                limit 3;
            """)
    popular_article = c.fetchall()
    db.close()
    return popular_article


def get_pop_author():
    "Return the author who is the most popular"

    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("""
                select name, count
                from pop_authors
                order by count desc
            """)

    popular_author = c.fetchall()
    db.close()
    return popular_author


def get_group_of_rate():
    "Return the day that did more than 1% of requets lead to errors"
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("""
                select a.time_t, a.count as OK, b.count as NOK
                from OK_status as a, NOK_status as b
                where a.time_t = b.time_t
                group by a.time_t, OK, NOK
                order by a.time_t;
            """)
    group_of_rate = c.fetchall()
    db.close()
    return group_of_rate

popular_article_tmp = get_pop_article()
popular_author_tmp = get_pop_author()
group_of_rate_tmp = get_group_of_rate()

print "\nThe most popular three articles\n"

for ar in popular_article_tmp:
    print ar[0] + " --- " + str(ar[1]) + " views"

print "\n\nThe most popular three authors\n"

for au in popular_author_tmp:
    print au[0] + " --- " + str(au[1]) + " views"


print "\n\nThe day did more than 1% of requests lead to errors\n"

for rate_by_day in group_of_rate_tmp:
    the_rate = float(rate_by_day[2]) / float(rate_by_day[1]+rate_by_day[2])*100
    the_rate = round(the_rate, 1)
    if the_rate >= 1.0:
        print str(rate_by_day[0])+" --- "+(str(the_rate)[:3])+"% errors\n"
