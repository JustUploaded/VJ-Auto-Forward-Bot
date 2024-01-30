from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "ad78167d4319a47d0c08d6dd2d8421ef")
      API_ID = int(getenv("API_ID", "11868520"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "6473401780:AAF20gWIy-yGh02Q5o18LtG7rF1B7neo65E")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002030459064:-1001960502411").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
