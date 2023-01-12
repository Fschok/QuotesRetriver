import os

import tweepy


def get_rules(user_at):
    rules = tweepy.StreamRule("to:{}".format(user_at),
                              "is:reply", )
    return rules


class Twitta:

    def __init__(self, token):
        self.client = self._get_client(token)

    @staticmethod
    def _get_client(token):
        client = tweepy.Client(token)
        return client

    def send_tweet(self, from_tweet):
        tweet_str = "Bonjour"
        reply_to = from_tweet.id
        self.client.create_tweet()
        return


class TwittaStream(tweepy.StreamingClient):

    def __int__(self, token):
        super().__init__(token)
        self.twita_client = Twitta(token)

    def on_connect(self):
        rules = tweepy.StreamRule("to:{}".format(self.twita_client.user_at),
                                  "is:reply",)
        self.add_rules(rules)

    def on_tweet(self, tweet):
        self.twita_client.send_tweet(tweet)
