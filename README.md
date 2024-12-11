Simple scripts to scrape submissions in a subreddit by top posts or keyword search. Outputs data in csv format.

### How to run
Modify `constants.py` to use your [Reddit API credentials](https://www.reddit.com/prefs/apps).

To get most controversial/gilded/hot/new/rising posts instead of top submissions, or to limit number of posts, modify Line 12 in `get_top_posts.py`. The default parameters are `limit=None` (retrieves as many as possible) and `time_filter=year`.

To search by keyword, enter your list of words in `constants.py`. 

### Example usage
```bash
python get_top_posts.py "subreddit-name" "data/results.csv"
```
```bash
python search_by_keyword.py "subreddit-name" "data/results.csv"
```