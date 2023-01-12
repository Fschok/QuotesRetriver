import os

from quotes_retriver.twitta import TwittaStream, get_rules


def main():
    user_at = os.environ.get("USER")
    token = os.environ.get("TWITTER_TOKEN")
    while True:
        stream = TwittaStream(token, wait_on_rate_limit=True)
        rules = get_rules(user_at)
        stream.add_rules(rules)
        stream.filter(threaded=True)


if __name__ == '__main__':
    main()
