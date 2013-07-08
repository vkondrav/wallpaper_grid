import praw
r = praw.Reddit('Scarlet Sickle test')
listing = list(r.get_subreddit('all').get_new_by_date())
print (listing)