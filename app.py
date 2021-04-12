from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)
import random
app = Flask(__name__)

line_bot_api = LineBotApi(
    'd4RG9WGjc104ouvQ1TTczvV9Xa962ub5SabRCqIDnnXkJOd4OOqI0IR2Pl1C5egytXWyhBS9fV5+sK+th9+iWaCODN5JgrZe3bBEgGP48sYcXeoLWOjziZWaoBgtI25Lr+x+2dnX+8aSkO6VHXgdB04t891Ow1cDnyilFU=')
handler = WebhookHandler('59e11fc48798f3384e056e1086b9e18a')


@app.route(callback, methods=['POST'])
def callback()
   # get X-Line-Signature header value
   signature = request.headers['X-Line-Signature']

       # get request body as text
       body = request.get_data(as_text=True)
           app.logger.info(Request body + body)

               # handle webhook body
               try
                   handler.handle(body, signature)
                except InvalidSignatureError
                   print(Invalid signature. Please check your channel access tokenchannel secret.)
                       abort(400)

                return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event)
   msg = event.message.text
       if msg != '我要卡片'
        r = '請輸入我要生日卡片~'
        if '我要生日快卡片' in msg
        r = '我欲千里尋覓你\n喜愛如常也如是\n歡愉苦短夜色白\n你知我心為誰癡'
        if msg = '我要真的生日卡片'
        r = '喜歡你總是樂觀正向\n喜歡你每次見面開心的樣子\n喜歡你被我逗笑的樣子\n謝謝你喜歡我的孩子氣\n謝謝你喜歡我這個直男\n謝謝你讓我喜歡你\n我們有不少地方都不謀而合\n希望我們能在一起久久的\n麻煩你繼續包容我這個白目的男友啦~\n期待跟你一起旅行'
        """if '摸頭' in msg
    img = ImageSendMessage(
      original_content_url=httpsi.imgur.comlNj8vBV.jpg,
      preview_image_url=httpsi.imgur.comlNj8vBV.jpg
      )
      line_bot_api.reply_message(
        event.reply_token, img)
        return"""
           line_bot_api.reply_message(
                event.reply_token,
              TextSendMessage(text=r))


if __name__ == __main__
   app.run()
