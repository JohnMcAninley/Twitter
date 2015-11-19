from twython import TwythonStreamer
from Queue   import Queue
from tweet   import Tweet

class TwitterStreamer(TwythonStreamer):

    def __init__(self, CONSUMER_KEY, CONSUMER_SECRET, 
                 ACCESS_KEY, ACCESS_SECRET, queue):

        self.queue = queue
        super(TwythonStreamer, self).__init__(CONSUMER_KEY, CONSUMER_SECRET, 
                                              ACCESS_KEY,   ACCESS_SECRET)

    def on_success(self, data):

        if 'text' in data:
            if 'retweeted_status' in data:
                data = data['retweeted_status']
            self.queue.put(Tweet(data['id_str'], data'[user']['id_str'], data['text']) 
                
    def on_error(self, status_cose, data):
        print status_code 
