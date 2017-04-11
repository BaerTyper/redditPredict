import praw
import pickle

usr = ""
pwd = ""
id = ""
secret = ""
agent = ""	

username = usr
print("Logging in...")
reddit = praw.Reddit(client_id=id, client_secret=secret, password=pwd, user_agent=agent, username=usr)
print("Logged in as " + str(reddit.user.me()))

check = input("What is your username?\n")
lists = pickle.load(open("data.p", "rb"))
