import os
import time
import datetime
import praw  # reddit api
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the Reddit client
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent="dad_joke_generator_app"
)

subreddit = reddit.subreddit("dadjokes")
post_data = []
after = None 

# Determine the path to the 'data' folder which is one level above the current script directory.
data_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

csv_path = os.path.join(data_folder, "dadjokes_partial_data.csv")

try:
    while True:
        try:
            # Fetch the next batch of posts using the 'after' parameter for pagination.
            top_posts = list(subreddit.top(time_filter="all", limit=250, params={"after": after}))
        except Exception as e:
            print(f"Error fetching posts: {e}")
            break  # Exit the loop if there's an error fetching posts

        if not top_posts:
            print("No more posts available.")
            break

        for post in top_posts:
            post_date = datetime.datetime.fromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S')
            post_data.append({
                "id": post.id,
                "upvotes": post.ups,
                "title": post.title,
                "selftext": post.selftext,
                "date": post_date
            })

        # Update 'after' with the fullname of the last post to paginate.
        after = top_posts[-1].fullname

        # Save the current batch to CSV in the data folder.
        df_batch = pd.DataFrame(post_data)
        df_batch.to_csv(csv_path, index=False)
        print(f"Saved partial data to {csv_path}. Waiting 5 minutes before next batch...")

        time.sleep(300)  # Wait 5 minutes before fetching the next batch

except KeyboardInterrupt:
    print("Process interrupted by user (KeyboardInterrupt).")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Save whatever data has been collected so far.
    df = pd.DataFrame(post_data)
    df.to_csv(csv_path, index=False)
    print(f"Data saved to {csv_path}")
