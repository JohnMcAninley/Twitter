# Twitter

This repository contains projects revolving around twitter.

TwitterContestBot

  This bot follows users and retweets tweets in order to enter contests.
  
  Create a config file with the structure:
  
    [AUTH]
    CONSUMER_KEY = <consumer_key>
    CONSUMER_SECRET = <consumer_secret>
    ACCESS_KEY = <access_key>
    ACCESS_SECRET = <access_secret>
  
  replacing the respective fields with your twitter authentication information.
  
  In TwitterContestBot.py change CFG_FILENAME to the file you created.
  
SoupNaziBot

  This bot finds tweets expressing a desire for soup and responds with "No soup for you!"
  
  Usage: See TwitterContestBot useag.
