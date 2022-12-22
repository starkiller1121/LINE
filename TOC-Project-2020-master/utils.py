import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage


channel_access_token = os.getenv("opQ3Df9xS6mw6FJr9IXSZuWHK8oJMAIE2HwKTVlHlQadf1NGLtT4Mt2wRAadY8zPo3iYiqQ8emgmun1PxJI3NPWDG5erxoXsgHZ4eDhxX4Zb8HLM3Q9C5bit4b3M9QyMIRsB1JoQPUYn2mg9dCB10flFUts=", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
