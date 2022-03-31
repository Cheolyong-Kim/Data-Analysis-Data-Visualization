from html.parser import HTMLParser
class 추출(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.is_strong =False
    def handle_starttag(self, tag, attrs):
        if tag =='strong':
            self.is_strong = True
    def handle_endtag(self, tag):
        if tag =='strong':
            self.is_strong = False
    def handle_data(self, data):
        if self.is_strong:
            print(data)
with open("data.html") as f:
    parser=추출()
    parser.feed(f.read())