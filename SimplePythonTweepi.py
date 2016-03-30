
import tweepy, sys, argparse


parser = argparse.ArgumentParser(description="Send a Tweet")
parser.add_argument('-k', metavar='K', type=str, help= 'Enter file with keys')
parser.add_argument('-t', metavar='T', type = str, help='Enter tweet')
parser.parse_args()

argkeys=''
tweet=""

if __name__ == "__main__":
   main(sys.argv[1:],argkeys, tweet)
   print (sys.argv[0])
   print (sys.argv[1])
   print (sys.argv[2])
   print (sys.argv[3])

filekeys=open(argkeys,'r')
keys = [x.strip('\n') for x in filekeys.readlines()]
filekeys.close()


#enter the corresponding information from your Twitter application:
CONSUMER_KEY = keys[0]#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = keys[1]#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = keys[2] #keep the quotes, replace this with your access token
ACCESS_SECRET = keys [3]#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#api.update_status(tweet)
print (tweet)