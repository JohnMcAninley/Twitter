def main():

    CONFIG_FILENAME = 'twitter-auth.ini'
    TRACK_TERMS = 'RT giveaway, RT win, retweet giveaway, retweet win'

    botnet = TwitterBotnet()
    print 'Created ' + str(botnet.create_users(CONFIG_FILENAME)) + 'users'
    botnet.create_stream(CONFIG_FILENAME)

    botnet.enqueue_tweets()
    botnet.follow_retweet()

if __name__ == "__main__":
    main()
