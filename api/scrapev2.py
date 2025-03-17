import praw
import pandas as pd
import time

# Reddit API Credentials
reddit = praw.Reddit(
    client_id="hnhK9SdMb-YwQlU8tZz6mA",
    client_secret="9FF9RSH5WcVpcJUu5h94Ex8OHkygEg",
    user_agent="webscrapy",
    username="Careful_Hornet_7230",
    password="Testaccount1.",
)

# Choose subreddit
subreddit_name = "stocks"  # Change this if needed
subreddit = reddit.subreddit(subreddit_name)

# Store scraped data
posts = []

# Scrape newest posts continuously
count = 0

try:
    for post in subreddit.new(limit=None):  # `None` means get as many as allowed
        posts.append([
            post.id,
            post.title,
            post.selftext,
            post.url,
            post.created_utc
        ])
        count += 1

        if count % 100 == 0:
            print(f"Scraped {count} posts so far...")

        # Avoid getting blocked
        time.sleep(1)

except KeyboardInterrupt:
    print("\nKeyboard Interrupt detected! Saving data before exit...")

finally:
    # Convert to DataFrame
    df = pd.DataFrame(posts, columns=["id", "title", "text", "url", "created_utc"])

    # Save as CSV
    filename = f"{subreddit_name}_reddit_posts.csv"
    df.to_csv(filename, index=False, encoding="utf-8")

    print(f"Data saved! {len(df)} posts written to {filename}")
