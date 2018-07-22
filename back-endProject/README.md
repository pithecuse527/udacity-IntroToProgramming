This is a udacity's project that indicates some reporting.

The python code (article.py) should be run in virtual box(In my case, Ubuntu).

1. Run any terminal that can use virtual box.
2. When you are in terminal, go to my project folder('vagrant').
3. Start up the virtual box (vagrant up)
4. Log into it with vagrant ssh.
5. When you successfully logged into the virtual machine, go to my project folder.
6. Install the data using 'newsdata.sql' file.(psql -d news -f newsdata.sql)
7. Run my python project that is named "article.py"



Notice!
  - The example output will be in 'example.txt' file.
  - Before run my python project, you should create view that I write down below.

  create view ok_status as
  select to_char(time, 'FMMonth DD,YYYY') as time_t, count(*)
  from log
  where status like '%OK%'
  group by time_t;

  create view nok_status as
  select to_char(time, 'FMMonth DD,YYYY') as time_t, count(*)
  from log
  where status not like '%OK%'
  group by time_t;

  create view pop_articles as
  select articles.title, articles.slug, count(log.path)
  from articles, log
  where articles.slug = substr(log.path,10)
  group by articles.slug,articles.title;

  create view pop_authors as
  select articles.author, authors.name, count(log.path)
  from articles,authors,log
  where articles.author = authors.id and substr(log.path,10) = articles.slug
  group by articles.author, authors.name;
