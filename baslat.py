from time import sleep
from InstagramAPI import InstagramAPI
import time
users = []
for line in open('liste-2.txt','r').readlines():
    users.append(line.strip())
time.sleep(8)
api = InstagramAPI("2021.2021.2021.2021.2021.2021", "sifre123")
api.login()
for user in users:
    api.searchUsername(user)
    result = api.LastJson
    username_id = result['user']['pk']
    api.follow(username_id)