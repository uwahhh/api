import praw
import pandas as pd
import time

# Replace with your actual credentials
reddit = praw.Reddit(
    client_id="Hx7mblBGjCkE-cfyX0BALQ",
    client_secret="s8vMsRa6Z9PWQVqW-pilshY2I8Ztzw",
    user_agent="webscrape",
    username="xawz",
    password="Ninokano<3",
)

# Fetch posts from whichever reddit
subreddit = reddit.subreddit("stocks")

# List to store data
posts = []

# Keep track of the last post
last_post = None

# Scrape continuously until no more posts
while True:
    if last_post:
        submissions = subreddit.new(limit=100, params={"after": last_post})
    else:
        submissions = subreddit.new(limit=100)  # Get the first batch

    count = 0
    for post in submissions:
        posts.append([post.id, post.title, post.selftext, post.url, post.created_utc])
        last_post = post.name  # Store the last post ID
        count += 1

    print(f"✅ Scraped {count} new posts...")

    # Stop when there are no more posts
    if count == 0:
        break

    # Respect Reddit API rate limits (add delay)
    time.sleep(2)  # Wait 2 seconds before next request

# Convert to DataFrame
df = pd.DataFrame(posts, columns=["id", "title", "text", "url", "created_utc"])

# Save as CSV
df.to_csv(subreddit.display_name+".csv", index=False, encoding="utf-8")

print(f"✅ Scraped {len(df)} total posts! Data saved to "+subreddit.display_name+".csv")