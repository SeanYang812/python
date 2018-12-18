import json
import requests
from wxpy import *
bot = Bot(cache_path=True)
my_friends = []
my_friends = bot.friends


# print(bot.search('Quincy.Coder'))
# friend=bot.search('Quincy.Coder')[0]
# print(friend)

# 调用图灵机器人API，发送消息并获得机器人的回复
def auto_reply(text):
    url = "http://www.tuling123.com/openapi/api"
    api_key = "a2064e6849a64c16aaf29452842f40f7"
    payload = {
        "key": api_key,
        "info": text,
    }
    r = requests.post(url, data=json.dumps(payload))
    result = json.loads(r.content)
    return "[Sean微信测试，请忽略] " + result["text"]


@bot.register()
def forward_message(msg):
    for friend in my_friends:
        if friend.name == '刘孟':
        # if msg.sender == friend:
            return auto_reply(msg.text)

embed()