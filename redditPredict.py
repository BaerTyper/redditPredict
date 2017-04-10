import praw
import csv
import pickle

usr = ""
pwd = ""
id = ""
secret = ""
agent = ""

def checkRedditor(username): # Saves username in "users.p" file, then calls saveReddits
	try:
		userlist = pickle.load(open("users.p", "rb"))
		print(userlist)
		if (username in userlist):
			print("Don't do it.")
		else:
			print("Adding...")
			userlist.append(username)
			pickle.dump(userlist, open("users.p", "wb"))
			saveReddits(username)
	except:
		userlist = []
		userlist.append(username)
		pickle.dump(userlist, open("users.p", "wb"))
		saveReddits(username)

def saveReddits(username): # Checks usernames subreddits and saves them to "data.p"
	try:
		mainList = pickle.load(open("data.p", "rb"))
		subreddits = []
		user = reddit.redditor(username)
		for comment in user.comments.new(limit=None):
			subreddits.append(str(comment.subreddit))

		subreddits = list(set(subreddits))
		subreddits.insert(0, username)

		mainList.append(subreddits)
		pickle.dump(mainList, open("data.p", "wb"))
	except:
		mainList = []
		subreddits = []
		user = reddit.redditor(username)
		for comment in user.comments.new(limit=None):
			subreddits.append(str(comment.subreddit))

		subreddits = list(set(subreddits))
		subreddits.insert(0, username)

		mainList.append(subreddits)
		pickle.dump(mainList, open("data.p", "wb"))	
	print("Done.")	

username = usr

print("Logging in...")
reddit = praw.Reddit(client_id=id, client_secret=secret, password=pwd, user_agent=agent, username=usr)
print("Logged in as " + str(reddit.user.me()))

checkRedditor(username)
