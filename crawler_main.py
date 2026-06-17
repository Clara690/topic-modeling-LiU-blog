from crawler.crawler import fetch_blog_title, fetch_blog_content
from time import sleep
import random 
import pandas as pd

# this script is for fetching blog data including the blog title, link and content,
# and save the data to a csv file


# fetch the blog titles and links from all the 24 pages
for page in range(1, 24): # fetch the blog titles and links from all the 24 pages
    results = fetch_blog_title(page)
    sec = random.random() * 2  # add a random delay 
    sleep(sec) 
    # empty list to store the blog content
    blog_contents = []
    # convert the results to a dataframe 
    df = pd.DataFrame(list(results.items()), columns=['title', 'link'])

    # fetch blog content
    for link in results.values():
        content = fetch_blog_content(link)
        sec = random.random()   # add a random delay 
        sleep(sec)
        blog_contents.append(content)
    # add the blog content to the dataframe
    df['content'] = blog_contents

    # immediately save the results to a csv file after fetching each page, to avoid losing data due to unexpected errors
    if page == 1: # if it's the first page, write the header
        df.to_csv('blog_posts.csv', mode='w', index=False, header=True)
    else: # if it's not the first page, append to the file without writing the header
        df.to_csv('blog_posts.csv', mode='a', index=False, header=False)







