from tweepy.streaming import StreamListener
>>> from tweepy import OAuthHandler
>>> from tweepy import Stream
>>> access_token = "1298548228107862016-TO9Q1nmDCF0yKkCWmpRTuV0o4Q8scK"
>>> access_token_secret = "iW1wiXcHsftcpC9G2ToT8xTirKgMcpxCVUBefwyXKL7Am"
>>> consumer_key = "GtNcEs46VI7R6o9QwS0EfgPSU"
>>> consumer_secret = "eZ8rjIyCErM7loty5JgWagU9JM5HjS8ysKRFHGGHdunMpLQYsr"
>>> class StdOutListener(StreamListener):
	def on_data(self, data):
           print data
           return True

  def on_error(self, status):
            print status
if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(GtNcEs46VI7R6o9QwS0EfgPSU,eZ8rjIyCErM7loty5JgWagU9JM5HjS8ysKRFHGGHdunMpLQYsr)
    auth.set_access_token(1298548228107862016-TO9Q1nmDCF0yKkCWmpRTuV0o4Q8scK,iW1wiXcHsftcpC9G2ToT8xTirKgMcpxCVUBefwyXKL7Am)
    stream = Stream(auth, l)
    stream.filter(track=['corona'])
