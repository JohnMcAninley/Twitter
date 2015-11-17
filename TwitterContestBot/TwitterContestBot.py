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
                if tweet['retweeted'] == False:
                    bot.create_friendship(id = tweet['user']['id_str']) 
                    bot.retweet(id = tweet_id)
                    time_queue.put(time.time())
            except TwythonError as e:
                print e

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

    while True:
        try:
            stream.statuses.filter(track='RT giveaway, RT win, retweet giveaway, retweet win')
        except Exception as e:
            print e

"""
    for result in results["statuses"]:
	
        if result["retweeted"] == False:
		 
            text = "@" + result["user"]["screen_name"] + " " + "NO SOUP FOR YOU!"

            try :

                bot.update_status(status=text, in_reply_to_status_id=result["id_str"])
                time.sleep(30)

                try:

                    file = open('SoupNaziBot/lastID', 'w')
                    file.write(result["id_str"])
                    file.close()
				
                except IOError as e:
                    print e

            except TwythonError as e:
                print e

    try:
        file = open('lastID', 'w')
        newID = str(results["search_metadata"]["max_id"])
        file.write(newID)
        file.close()

    except IOError as e:
        print e
"""

if __name__ == "__main__":
    main()
