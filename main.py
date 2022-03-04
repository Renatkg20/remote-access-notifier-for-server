#!/bin/python3
import os 
import requests
# Telegram Bot notify if some successful access was registrated in auth.log 
def telegram_bot_sendtext(bot_message):

   bot_token = 'BOT_TOKEN'
   bot_chatID = 'ChatID'
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

   response = requests.get(send_text)

   return response.json()
# read logs of auth.log
with open("/var/log/auth.log", "r") as file:
    t = file.read()
# we look for the successul access by using grep and then it save as auth.txt
os.system("cat /var/log/auth.log | grep Accepted > /home/user/Desktop/auth.txt")

l = []
# I created the auth_2.txt in order to compare two files auth_2.txt and auth.txt. Thereby, I identief the successful access to the server. 
with open("/home/user/Desktop/auth_2.txt", "r") as file:
    t = file.read()
# save file for comparing 
with open("/home/user/Desktop/auth.txt", "r") as file:
    p = file.read()
res = p.split("\n")
# This part of code is looking for changes on the log files. In order to monitor changes script will impliment every one minute via crontab. 
for i, a in zip(t.split(" "), p.split(" ")):
    if i != a:
      l.append("1")
      os.system("cat /home/user/Desktop/auth.txt > /home/user/Desktop/auth_2.txt")
      break

if len(l) > 0:
    telegram_bot_sendtext(f"Accepted \n {res[-2]}")


# Please if you have some questions and misunderstandings of the current script. Please let me know I will be glad to respond as best I can. Thank you! 