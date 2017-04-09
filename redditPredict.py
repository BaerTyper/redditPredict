import praw
import csv

usr = ""
pwd = ""
id = ""
secret = ""
agent = ""

def checkRedditor(username):
	try:
		userlist = pickle.load(open("users.p", "rb"))
		print(userlist)
		if (username in userlist):
			print("Don't do it.")
		else:
			print("Adding...")
			userlist.append(username)
			pickle.dump(userlist, open("users.p", "wb"))
			#saveReddits(username)
	except:
		userlist = []
		userlist.append(username)
		pickle.dump(userlist, open("users.p", "wb"))

def saveReddits(username):
	subreddits = []
	user = reddit.redditor(username)
	for comment in user.comments.new(limit=None):
		subreddits.append(str(comment.subreddit))

	subreddits = list(set(subreddits))
	subreddits.insert(0, username)

	with open("data.csv", "w") as stream:
		writer = csv.writer(stream)
		writer.writerow(subreddits)

	print("Done.")	


username = usr

print("Logging in...")
reddit = praw.Reddit(client_id=id, client_secret=secret, password=pwd, user_agent=agent, username=usr)
print("Logged in as " + str(reddit.user.me()))

checkRedditor(username)
