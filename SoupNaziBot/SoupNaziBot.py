from twython import TwythonStreamer, Twython, TwythonError
import ConfigParser
from TwitterStreamer import TwitterStreamer
import Queue
from threading import Thread
import time

def follow_and_retweet(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET, queue):

    bot = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
    time_queue = Queue.Queue() 

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
                bot.retweet(id = tweet_id)
                text = "@" + tweet["user"]["screen_name"] + " " + "NO SOUP FOR YOU!" 
                bot.update_status(status=text, in_reply_to_status_id=tweet_id)

            except TwythonError as e:
                print e

            time_queue.put(time.time())

def main():

  # Read twitter auth info from init file 
    config = ConfigParser.ConfigParser()
    config.readfp(open('twitter-auth.ini'))

    CONSUMER_KEY = config.get('AUTH', 'CONSUMER_KEY')
    CONSUMER_SECRET = config.get('AUTH', 'CONSUMER_SECRET')
    ACCESS_KEY = config.get('AUTH', 'ACCESS_KEY')
    ACCESS_SECRET = config.get('AUTH', 'ACCESS_SECRET')

  # Create streamer
    stream = TwitterStreamer(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

    queue = Queue.Queue()
    stream.share_queue(queue)

    thread = Thread(target = follow_and_retweet, args = (CONSUMER_KEY, CONSUMER_SECRET,
                    ACCESS_KEY, ACCESS_SECRET, queue)) 

    thread.start()

    stream.statuses.filter(track='RT giveaway, RT win, retweet giveaway, retweet win')

if __name__ == "__main__":
    main()
