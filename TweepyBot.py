
import tweepy, time, sys
import random

import shutil
from os import listdir
from os.path import isfile, join, getsize

argkeys= str(sys.argv[1])
argfile = str(sys.argv[2])
argmentions = str(sys.argv[3])
arghashtags = str(sys.argv[4])
arglinks = str(sys.argv[5])


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

filename=open(argfile,'r')
#f=filename.readlines()
content = [x.strip('\n') for x in filename.readlines()]
filename.close()


filementions=open(argmentions,'r')
mentions = [x.strip('\n') for x in filementions.readlines()]
filementions.close()

filehashtags= open(arghashtags, 'r')
hashtags = [x.strip('\n') for x in filehashtags.readlines()]
filehashtags.close()

filelinks=open (arglinks,'r')
linklist = [x.strip('\n') for x in filelinks.readlines()]
filelinks.close()

#
#for line in f:
#    api.update_status(line)
#    time.sleep(30)#Tweet every 15 minutes

photo_path='/home/pi/Desktop/TwitterBot/Pic/'
onlyfiles = [f for f in listdir(photo_path) if isfile(join(photo_path, f))]

y=len(onlyfiles)
for x in range (0,y):
    statusrandom=random.randrange(0, len(content)-1,1)
    hashtagsrandom=random.randrange(0, len(hashtags)-2,1)
    mentionsrandom=random.randrange(0, len(mentions),1)
    linkrandom=random.randrange(0, len(linklist),1)
    file=photo_path+onlyfiles[x]
    destination='/home/pi/Desktop/TwitterBot/Completed/'+onlyfiles[x]
    stat=hashtags[hashtagsrandom]
    stat+=" "+content[statusrandom]
    hashtagsrandom+=1
    x=0
#    while ((x<4)&(len(stat)<=100)):
#	if ((mentionsrandom)>=(len(mentions))):
#		mentionsrandom=0
#	stat+=" "+mentions[mentionsrandom]
#	mentionsrandom+=1
#	x+=1
#    x=0
    while ((x<4)&(len(stat)<=100)):
   	 if (hashtagsrandom>=len(hashtags)):
		hashtagsrandom=0
   	 stat+=" "+hashtags[hashtagsrandom]
   	 hashtagsrandom+=1
   	 x+=1
    stat+=" "+linklist[linkrandom]
    if (getsize(file)<(3072*1024)):
        api.update_with_media(file,status=stat)
    shutil.move(file, destination)
    a=1
    b=2
    time.sleep(random.randrange(a*60,b*60,5))#Tweet between a min and b min
