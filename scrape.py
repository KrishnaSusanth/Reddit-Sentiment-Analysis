import pandas as pd
import praw
user_agent = "Scraper"
reddit = praw.Reddit (
client_id="QtV-j1uZg31xJTQLecKacg",
client_secret="6gqR9uGA6ilTwiSVeI8VTSYw9o1O5g",
user_agent=user_agent
)
threads = {"id": [], "title" : [], "body":[]}
for  submission in reddit.subreddit('tollywood').hot(limit=None):
    thread = []
    threads["id"].append(submission.id)
    threads["title"].append(submission.title)
    thread.append(submission.selftext)
    submission.comments.replace_more(limit=0)  
    # Extract and print all comments
    for comment in submission.comments.list():
        thread.append(comment.body)
        for reply in comment.replies:
            thread.append(reply.body)
    threads["body"].append("::".join(thread))

threadsDf = pd.DataFrame(threads)

threadsDf.to_csv(r"C:\Users\Kailash.Rokkam\documents\leet\Threads.csv", index=False, encoding="utf-8")