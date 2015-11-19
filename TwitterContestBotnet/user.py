from twython     import Twython
from threading   import Thread, Lock
from collections import dequeue
from user_stream  import UserStream

class User:

    def __init__(self, user_id, screen_name):
        self.user_id = user_id
        seld.screen_name = screen_name
        self.post_history = dequeue()
        self.bot_lock = Lock()

    def authenticate(self, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET):
        try:
            self.post_bot = Twython(CONSUMER_KEY, CONSUMER_SECRET, 
                                    ACCESS_KEY,   ACCESS_SECRET) 
            return True
        except TwythonError as e:
            return False

    def start_user(self): 
        self.interactions_thread = Thread(target=relay_interactions)
        self.act_human_thread = Thread(target=act_human)
        self.interactions_thread.start()
        self.act_human_thread.start()

""" This function takes a tweet object, follows the user who created it, 
    and retweets the tweet. It is assumed the tweet has not been retweeted
    by any other botnet member. """
    def post(self, tweet):

        if time_queue.qsize() > 14:
           if (time() - self.post_history[-1]) < (60 * 15):
               return False
           else:
               self.post_history.pop()

        # TODO Better error handling     
        try:
            with self.bot_lock:
                self.post_bot.create_friendship(id=tweet['user']['id_str']) 
                self.post_bot.retweet(id=tweet_id)
                self.post_history.put(time())
                return True;

        except TwythonError as e:
            print e
            return False

    def relay_interactions(self):

        # TODO

    def act_human(self):
        # TODO
