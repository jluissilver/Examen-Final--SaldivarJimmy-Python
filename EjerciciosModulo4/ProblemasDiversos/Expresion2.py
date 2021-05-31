import re

texto = """Unfortunately one of those moments wasn't a giant squid monster. User_mentions:2, likes: 9, number of retweets: 7"""
patron="User_mentions:+[0-9]"
likes="likes: +[0-9]"
retweets="number of retweets: +[0-9]"
 
coincidencias = re.findall(patron, texto)
coincidencias2= re.findall(likes, texto)
coincidencias3= re.findall(retweets, texto)

for coincidencia in coincidencias:
    print(coincidencia)

for coincidencia in coincidencias2:
    print(coincidencia)

for coincidencia in coincidencias3:
    print(coincidencia)