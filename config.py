import os

class Config(object):
   # The Telegram API things
   API_ID= int(os.environ.get("API_ID","6534707"))
   API_HASH = os.environ.get("API_HASH","4bcc61d959a9f403b2f20149cbbe627a")
   # get a token from @BotFather
   BOT_TOKEN = os.environ.get("BOT_TOKEN", "5502855202:AAGW3MYUov5Gb2wWgpcaNTgxDjZ98IFh4P8")
   # channel id = -100 (for logs)
   LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001858175451"))   
   # Array to store users who are authorized to use the bot 
   AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1430593323").split())    
   # force sub user to the channel (without @)
   CHNAME = os.environ.get("CHNAME", "animecolony")
