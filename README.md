# redditPredict
A Python Reddit script to use group intelligence to find subreddits a user may like. Works by selecting users that have commented on the front page, saving all subreddits that those users have commented in and then when given a user as input looks for users that have those subreddits in their lists. So it's based on the theory that users will like things users with similar interests like. As the project grows I'll make sure to add data reduction to make the whole subreddit search more specific and accurate. 

What it does so far:
- Log into Reddit through its API
- Look for the logged in User's Subreddits
- Save them to a Comma Separated File called data.csv
- Save all usernames of scanned Reddit accounts to a CSV file called users.csv
- Check if Reddit account has been checked already before doing anything with it

For the future:
- Compare Subreddit lists before adding new user to them
- Look for users on random subreddits
- Save Subreddit lists of users automatically
- Actually accept user input and look for subreddits the user may like

Still have lots of work to do on this, and sadly not a lot of time. But I enjoy doing it. And I really want to see how well it works in the end. 



**main.py** will be the file run to input a username and receive a list of subreddits the user may like. 
**redditPredict** will be the file run to collect more subreddit-data-samples from users of random subreddits
