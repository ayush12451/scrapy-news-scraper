import requests
import sqlite3
import json

conn = sqlite3.connect('news.db')
curr = conn.cursor()

curr.execute('''select headline,news from news''')
rows = curr.fetchall()
i=1
for row in rows:
    txt = row[1].encode('utf-8')
    text = str(txt)
    #text = temp.decode('utf-8')
    url = "https://api.meaningcloud.com/summarization-1.0"
    payload = "key=d518a279d420c6300446f6179e9a07d8&txt=" + text + "&sentences=5"
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.request("POST", url, data=payload, headers=headers)
    x = json.loads(response.text)
    curr.execute('''update news
                    set news= ?
                    where headline=?''',(x["summary"],row[0]))
    print("processed %d rows" %(i))
    i+=1
conn.commit()
conn.close()