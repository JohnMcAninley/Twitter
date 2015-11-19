from twython         import TwythonStreamer, Twython, TwythonError
from ConfigParser    import ConfigParser
from TwitterStreamer import TwitterStreamer
from Queue           import Queue
from threading       import Thread
from time            import time
from user            import User

class TwitterBotnet:

    def __init__(self):
        self.user_list = []
        self.tweet_queue = Queue()

    def create_users(self, config_filename):
        try:
            cp = ConfigParser()
            cp.readfp(open(CONFIG_FILENAME))

            for user_cfg in p.sections():
                if not user_cfg = 'stream':
                    user = User(cp.get(user_cfg, 'USER_ID'), 
                                cp.get(user_cfg, 'SCREEN_NAME'))
 
                    if user.authenticate(cp.get(user, 'CONSUMER_KEY'), 
                                         cp.get(user, 'CONSUMER_SECRET'),
                                         cp.get(user, 'ACCESS_KEY'),
                                         cp.get(user, 'ACCESS_SECRET')):
                        user_list.append(user)

        except ConfigParser.Error as e:
            print e

        return len(user_list)

    def create_stream(self, config_filename):
        try:
            cp = ConfigParser()
            cp.readfp(open(CONFIG_FILENAME))
            self.stream = TwitterStreamer(cp.get('DEFAULT', 'CONSUMER_KEY'), 
                                          cp.get('DEFAULT', 'CONSUMER_SECRET'),
                                          cp.get('DEFAULT', 'ACCESS_KEY'),
                                          cp.get('DEFAULT', 'ACCESS_SECRET'))
        except Exception as e:
            print e
 
    def follow_and_retweet(user_list, queue):

    while True:
        if not queue.empty():
            tweet_id = queue.get()
            
            print 'thread: removed tweet ' + tweet_id + ' from queue'
            print 'thread: time queue size: ' + str(time_queue.qsize()) 
            if not time_queue.empty():
                time_of_post = time_queue.get()
                if time_queue.qsize() > 13:
                    while time.time() - time_of_post < 60*15:
                        pass
                else: 
                    for i in range(time_queue.qsize()):
                        time_queue.put(time_of_post)
                        time_of_post = time_queue.get()
                    time_queue.put(time_of_post)

            try:
                tweet = bot.show_status(id = tweet_id)
                if tweet['retweeted'] == False:
                    bot.create_friendship(id = tweet['user']['id_str']) 
                    bot.retweet(id = tweet_id)
                    time_queue.put(time())
            except TwythonError as e:
                print e



    def enqueue_tweets(self, track_terms):

        Thread(target=follow_and_retweet, args=(stream.get_queue(), user_list)).start() 

    while True:
        try:
            stream.statuses.filter(track=TRACK_TERMS)
        except Exception as e:
            print e
