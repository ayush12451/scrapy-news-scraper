import json
import sqlite3
def payload_create(tag):

    conn = sqlite3.connect('news.db')
    curr = conn.cursor()
    curr.execute('''select * from news where tag = ?''',(tag,))
    rows = curr.fetchall()
    return rows
def create_index():
    conn = sqlite3.connect('news.db')
    curr = conn.cursor()
    curr.execute('''select * from news''')
    rows = curr.fetchall()
    return rows