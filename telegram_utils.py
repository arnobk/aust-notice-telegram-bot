from telegram.ext import Updater, CommandHandler
import telegram
from helper.bot_commands import BotCommands
import json
import api_utils
from datetime import date
from Notice import Notice

def typing_indicator(chat_id,context):
    context.bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)

def start(update,context):
    typing_indicator(update.message['chat']['id'],context)
    context.bot.send_message(chat_id=update.message['chat']['id'],reply_to_message_id=update.message['message_id'],text='Hi ' + update.message['chat']['first_name'] + '! Welcome to AUST Notice Bot. Send /help to know how to use.')

def help(update, context):
    typing_indicator(update.message['chat']['id'],context)
    reply = 'Welcome <strong>' + update.message['chat']['first_name'] + '</strong> to AUST Notice Bot. Use these following commands to interact with the bot.\n\n'
    for command in BotCommands:
        reply+= "/"+command['command']+': ' + command['desc']+'\n\n'
    reply+="Developed by Arnob Karmokar (@arnobdotme)."
    context.bot.send_message(chat_id=update.message['chat']['id'],reply_to_message_id=update.message['message_id'],text=reply,parse_mode='html')

def latest(update,context):
    typing_indicator(update.message['chat']['id'],context)
    notice = api_utils.get_notice()
    try:
        latest = Notice(notice[0]['text'],notice[0]['url'],notice[0]['date'])
        reply = '&#x2139  <strong>LATEST NOTICE\n\n<em>' + latest.title + '</em></strong>' + '\n\nURL: <a href="' + latest.url + '">' + latest.url + '</a>' + '\n\nPublished: ' + latest.date
        context.bot.send_message(chat_id=update.message['chat']['id'],reply_to_message_id=update.message['message_id'],text=reply,parse_mode='html')
    except:
        context.bot.send_message(chat_id=update.message['chat']['id'],reply_to_message_id=update.message['message_id'],text=reply)

def notice(update,context):
    typing_indicator(update.message['chat']['id'],context)
    notice = api_utils.get_notice()
    try:
        number = int(context.args[0])
        latest = Notice(notice[number-1]['text'],notice[number-1]['url'],notice[number-1]['date'])
        reply = '&#x2139  <strong>NOTICE NO: ' + str(number) + '\n\n<em>' + latest.title + '</em></strong>' + '\n\nURL: <a href="' + latest.url + '">' + latest.url + '</a>' + '\n\nPublished: ' + latest.date
        context.bot.send_message(chat_id=update.message['chat']['id'],reply_to_message_id=update.message['message_id'],text=reply,parse_mode='html')
    except:
        reply = 'Please specify which notice you want to get. Example: /notice 5 - This will fetch the 5th notice from latest one.'
        context.bot.send_message(chat_id=update.message['chat']['id'],reply_to_message_id=update.message['message_id'],text=reply,parse_mode='html')

def recent(update,context):
    typing_indicator(update.message['chat']['id'],context)
    notice = api_utils.get_notice()
    try:
        notice_list = []
        number = int(context.args[0])
        for index in range(min(number,20)):
            notice_list.append(Notice(notice[index]['text'],notice[index]['url'],notice[index]['date']))
                
        reply = '&#x2139  <strong>LAST ' + str(min(number,20)) + ' NOTICE</strong>\n\n'
        for notice in notice_list:
            reply += '<strong><em>' + notice.title +'</em></strong>\nURL: <a href="'+ notice.url + '">' + notice.url + '</a>' + '\nPublished: ' + notice.date +'\n\n'
        
        context.bot.send_message(chat_id=update.message['chat']['id'],reply_to_message_id=update.message['message_id'],text=reply,parse_mode='html')        
    except:
        reply = 'Please specify how many notice you want to get (max: 20). Example: /recent 10'
        context.bot.send_message(chat_id=update.message['chat']['id'],reply_to_message_id=update.message['message_id'],text=reply,parse_mode='html')

def get_prefered_format_date(today):
    if len(str(today.day)) != 1:
        day = str(today.day)
    else:
        day = '0' + str(today.day)
    
    if len(str(today.month)) != 1:
        month = str(today.month)
    else:
        month = '0' + str(today.month)

    year = str(today.year)[2:]
    today_required_format = day + '/' + month + '/' + year
    return today_required_format

def today(update,context):
    today = get_prefered_format_date(date.today())
    typing_indicator(update.message['chat']['id'],context)
    notice = api_utils.get_notice()
    notice_list = []
    for index in range(len(notice)):
        if notice[index]['date'] == today:
            notice_list.append(Notice(notice[index]['text'],notice[index]['url'],notice[index]['date']))
    if len(notice_list) > 0:
        reply = '&#x2139  <strong>Today\'s Notice (' + today + ')</strong>\n\n'
        for notice in notice_list:
            reply += '<strong><em>' + notice.title +'</em></strong>\nURL: <a href="'+ notice.url + '">' + notice.url + '</a>\n\n'
    else:
        reply = '&#x2139  <strong>No new notice published today (' + today +').</strong>'
    context.bot.send_message(chat_id=update.message['chat']['id'],reply_to_message_id=update.message['message_id'],text=reply,parse_mode='html')

def response_to_message(update,context):
    reply = "Please send /help command to learn how to use this bot."
    context.bot.send_message(chat_id=update.message['chat']['id'],reply_to_message_id=update.message['message_id'],text=reply,parse_mode='html')

def subscribe(update,context):
    with open('subscriber_list.txt','a+') as subscribers:
        subscribers.write(str(update.message['chat']['id']) + '\n')
    reply = "Hello " + update.message['chat']['first_name'] + ', You have successfully subscribed to instant notice updates. Send /unsubscribe if you want to opt out.'
    context.bot.send_message(chat_id=update.message['chat']['id'],reply_to_message_id=update.message['message_id'],text=reply,parse_mode='html')


        


