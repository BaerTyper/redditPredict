import praw
import csv

usr = ""
pwd = ""
id = ""
secret = ""
agent = ""
subreddits = []

username = ""

print("Logging in...")
reddit = praw.Reddit(client_id=id,
                     client_secret=secret,
                     password=pwd,
                     user_agent=agent,
                     username=usr)
print("Logged in as " + str(reddit.user.me()))

user = reddit.redditor(username)
  
for comment in user.comments.new(limit=None):
    subreddits.append(str(comment.subreddit))
    
subreddits = list(set(subreddits))
subreddits.insert(0, username)

with open("data.csv", "w") as file:
	writer = csv.writer(file)
	writer.writerow(subreddits)

print("The deed has been done.")
