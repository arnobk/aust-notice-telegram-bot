import configparser

# Parse Configuration
config = configparser.ConfigParser()
config.read('.config')
bot_token = config['myconfig']['telegram_bot_token']
api_url = config['myconfig']['aust_notice_api_url']