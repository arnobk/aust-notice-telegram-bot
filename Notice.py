class Notice:
    def __init__(self,title,url,date):
        self.title = title
        if 'aust.edu' in url:
            self.url = url
        else:
            self.url = "http://aust.edu/" + url
        self.date = date
