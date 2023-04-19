import ParserVK_for_sql
import time
import json
from datetime import datetime
import understander
import sqlite3

with open('club.json') as f:
    groups = json.load(f)



'''
We get data broke on category
Now implemented from generator
'''
x =0
while x < 30:
    test = ParserVK_for_sql.Parse_VK(groups)
    for onepost in test.alanalises():
        id_group = onepost[0]
        id_post = onepost[1]
        date = datetime.fromtimestamp(onepost[2])
        text = onepost[3]
        theme = understander.mlp.predict(understander.vectroraizer.transform([text]))
        print(f"{id_group} - {id_post} \n {theme[0]} \n {date} \n {text}")

        try:
            conn = sqlite3.connect("Base_news.db")
            c = conn.cursor()
            c.execute('SELECT number_post FROM Vkontakte WHERE number_post = ?', (id_post,))
            result = c.fetchone()
            print(result)
            if not result:
                c.execute("""INSERT INTO Vkontakte
                                  (number_group, number_post, date, theme, data, url)
                                  VALUES
                                  ( ?, ?, ?, ?, ?, ?)
                                  """, \
                (id_group, id_post, date, theme[0], text, f"https://vk.com/feed?w=wall-{id_group}_{id_post}"))
            conn.commit()
        except sqlite3.Error as error:
            print("Error base")
        finally:
            if conn:
                conn.close()
        time.sleep(5)
    time.sleep(900)
    x += 1

