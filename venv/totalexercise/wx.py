import itchat
from helloworld import getResponse
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return getResponse(msg["Text"])["text"]
itchat.auto_login(hotReload=True)
itchat.run()
input()