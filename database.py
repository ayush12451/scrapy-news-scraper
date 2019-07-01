import sqlite3

conn = sqlite3.connect('news.db')
curr = conn.cursor()


curr.execute('''create table news(
                 headline text,
                 news text,
                 image text,
                 tag text)''')

conn.commit()
conn.close()