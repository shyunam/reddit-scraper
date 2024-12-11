import praw
import argparse
import csv
import constants


def get_top_subreddit_posts(subreddit_name):
    reddit = praw.Reddit(client_id=constants.client_id,
                         client_secret=constants.client_secret,
                         user_agent=constants.user_agent)
    
    top_posts = reddit.subreddit(subreddit_name).top(time_filter="year", limit=None)
    #top_posts = reddit.subreddit(subreddit_name).controversial(time_filter="year", limit=None)
    #top_posts = reddit.subreddit(subreddit_name).gilded(time_filter="year", limit=None)
    #top_posts = reddit.subreddit(subreddit_name).hot(time_filter="year", limit=None)
    #top_posts = reddit.subreddit(subreddit_name).new(time_filter="year", limit=None)
    #top_posts = reddit.subreddit(subreddit_name).rising(time_filter="year", limit=None)

    posts_data = []

    for post in top_posts:
        posts_data.append({
            'title': post.title,
            'author': post.author,
            'body': post.selftext,
            'url': post.url,
            'created_utc': post.created_utc,
            'score': post.score,
            'num_comments': post.num_comments
        })

    return posts_data

def save_to_csv(data, output_file_name):
    with open(output_file_name, 'w', newline='', encoding='utf-8') as data_file:
        csv_writer = csv.writer(data_file)

        header = data[0].keys()
        csv_writer.writerow(header)

        for entry in data:
            csv_writer.writerow(entry.values())


def main():
    parser = argparse.ArgumentParser(description="Scrape Reddit data for a given subreddit.")
    parser.add_argument("subreddit", help="Name of the subreddit to scrape")
    parser.add_argument("output_file_name", help="Name of the output csv file")
    args = parser.parse_args()

    subreddit_data = get_top_subreddit_posts(args.subreddit)
    save_to_csv(subreddit_data, args.output_file_name)

    print(f"Data saved to {args.output_file_name}")

if __name__ == "__main__":
    main()
