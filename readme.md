# AUST Notice Telegram Bot

This bot fetches notice from [AUST Website](http://aust.edu/news_events.htm ) using a unofficial PHP API made by me. Then responds according to your command.

### Try this Bot
Send message to [AUST Notice Bot](https://t.me/aust_notice_bot).

### Available Commands
- `/help` - Sends you help message.
- `/latest` - Sends you the most recent notice.
- `/recent [n]` - Sends you most recent 'n' notices.
- `/notice [n]` - Sends you the nth notice.
- `/today` - Sends you all the notices published today.

### Installation
- Create a `.config` file on the root directory with following info:

    ```
    [myconfig]
    telegram_bot_token = 
    aust_notice_api_url =
    ``` 
- Install requirements from `requirements.txt`.
- Run `python bot.py` to start the bot.

### TODO
[ ] Automatic notice update subscription.