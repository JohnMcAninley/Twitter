from twython import TwythonStreamer
import Queue

class TwitterStreamer(TwythonStreamer):
    def on_success(self, data):
        print 'stream: received data'
      # put all matching tweet id's in the queue
        if 'text' in data:
            if 'retweeted_status' in data:
                tweet = data['retweeted_status']
            else: 
                tweet = data
           
            if tweet['retweeted'] == False:
                print tweet['id_str']
                self.queue.put(data['id_str']) 
                print 'stream: queue size: ' + str(self.queue.qsize())
                
            else:
                print 'Already Retweeted'

    def on_error(self, status_cose, data):
        print status_code 

    def share_queue(self, queue):
        self.queue = queue
