# -*- coding: utf-8 -*-
# !/usr/bin/env python3
from flask import Flask, request
import telepot.namedtuple
from telepot.loop import OrderedWebhook
import requests
#ne eklemek isterseniz eðer kurulu deðil ise requirements.txt satýr olarak ekleyin youtube-dl,mechanize,bs4,....
TOKEN='TELEGRAM-TOKEN'


def handle(msg):
    global chat_id
    content_type, chat_type, chat_id, msg_date, msg_id = telepot.glance(msg, long=True)
    m = telepot.namedtuple.Message(**msg)
    #print (msg) 
    if (m.chat[4]==None) and (m.chat[5]==None):
        user = (m.chat[3])
    elif m.chat[5]==None: 
        user = m.chat[4]
    else:
        user = (m.chat[4]+" "+m.chat[5])
    
    if (("text" in msg) !=  True):
        bot.sendMessage(chat_id, f'*Hahaha gondegin emoji cok komik {user}*\n',parse_mode='Markdown',reply_to_message_id=msg_id)
        
    else:        #gelen metin mesajý: msg['text']  onu geri gönderelim
        bot.sendMessage(chat_id, msg['text'],parse_mode='Markdown',disable_web_page_preview=True)

     
print ('Bot Aktif ...')
PORT = int(os.environ.get('PORT', 8443))                       
app = Flask(__name__, static_url_path = "", static_folder = "./") #static folder, resim,dosya vs flask ile açmak için                         
bot = telepot.Bot(TOKEN)
webhook=OrderedWebhook(bot, {'chat': handle})

@app.route('/', methods=['GET'])
def index():
    return "<p>Merhaba, bu bir telegram botu</p><p><a href='https://t.me/......'>Botu baslat</a></p>" 

@app.route('/videolar', methods=['GET', 'POST'])
def index3():
    return "video sayfasi"
   
@app.route("/webhook", methods=['GET', 'POST'])
def pass_update():
    webhook.feed(request.data)
    return 'OK'
if __name__ == '__main__':
    try:
        bot.setWebhook("https://<APP-NAME>.herokuapp.com/webhook") #APPNAME yazan yere heroku da kurduðunuz makinanýn ismini verin, telegramla iletiþim için
    # Sometimes it would raise this error, but webhook still set successfully.
    except telepot.exception.TooManyRequestsError:
        pass
    webhook.run_as_thread()
    app.run(host='0.0.0.0',port=PORT, debug=True)