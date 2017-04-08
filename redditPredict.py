import praw
import csv

usr = ""
pwd = ""
id = ""
secret = ""
agent = ""

def checkRedditor(username):
	userlist = []
	with open("users.txt", "r") as stream:
		reader = csv.reader(stream)
		for entry in reader:
			userlist.append(entry)
	if (username in userlist):
		print("Redditor already added to database.")
	else:
		with open("users.txt", "w") as saver:
			writer = csv.writer(saver)
			writer.writerow(userlist)
		saveReddits(username)	


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

	print("Done")	


username = usr

print("Logging in...")
reddit = praw.Reddit(client_id=id, client_secret=secret, password=pwd, user_agent=agent, username=usr)
print("Logged in as " + str(reddit.user.me()))

checkRedditor(username)
