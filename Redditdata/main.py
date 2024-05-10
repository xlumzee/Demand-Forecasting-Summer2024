import praw
import pandas as pd

# Initialize PRAW with your specific credentials
reddit = praw.Reddit(
    client_id="v1Um7-4PqLJ7OXx5J3gAtw",
    client_secret="LHZ2IsBXcPncIkHGAZJAcqcQprFwjA",
    user_agent="my-app"
)

# Access the 'datascience' subreddit
subreddit = reddit.subreddit("datascience")

# Time filters for top posts
time_filters = ['day', 'week', 'month', 'year', 'all']
posts_data = []

# Fetch and extract data from top posts across different time frames
for time_filter in time_filters:
    top_posts = subreddit.top(time_filter=time_filter, limit=1000)
    for post in top_posts:
        posts_data.append({
            "Title": post.title,
            "ID": post.id,
            "Text": post.selftext,
            "URL": post.url,
            "Author": str(post.author),
            "Created": post.created_utc,
            "Score": post.score,
            "Flair": post.link_flair_text,
            "Comment Count": post.num_comments,
            "Type": "Top - " + time_filter
        })

# Fetch and extract data from hot posts
hot_posts = subreddit.hot(limit=1000)
for post in hot_posts:
    posts_data.append({
        "Title": post.title,
        "ID": post.id,
        "Text": post.selftext,
        "URL": post.url,
        "Author": str(post.author),
        "Created": post.created_utc,
        "Score": post.score,
        "Flair": post.link_flair_text,
        "Comment Count": post.num_comments,
        "Type": "Hot"
    })

# Fetch and extract data from new posts
new_posts = subreddit.new(limit=1000)
for post in new_posts:
    posts_data.append({
        "Title": post.title,
        "ID": post.id,
        "Text": post.selftext,
        "URL": post.url,
        "Author": str(post.author),
        "Created": post.created_utc,
        "Score": post.score,
        "Flair": post.link_flair_text,
        "Comment Count": post.num_comments,
        "Type": "New"
    })

# Convert list of dictionaries to a pandas DataFrame
posts_df = pd.DataFrame(posts_data)

# Save DataFrame to CSV file
posts_df.to_csv("reddit_datascience_newTopHot_posts.csv", index=False)
