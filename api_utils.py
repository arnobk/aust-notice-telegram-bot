import config
import urllib.request, json 
import time


notice = ''
last_fetch = 0

def get_timestamp_millis():
    return int(time.time()*1000.0)

def get_notice():
    # Fetch notice data from API only after 5 minutes of last update.
    global notice,last_fetch
    if (get_timestamp_millis() - last_fetch >= 1000*60*5) or notice == '' or notice == 'error':
        print('Time: ' + str(get_timestamp_millis()) + ' | fetching notice...')
        notice = fetch_notice()
        print('Time: ' + str(get_timestamp_millis()) + ' | fetching complete...')
        last_fetch = get_timestamp_millis()
    return notice

def fetch_notice():
    try:
        with urllib.request.urlopen(config.api_url) as api_response:
            data = json.loads(api_response.read().decode())
            return data
    except:
        return 'error'
