from tagger.config import FILE, USERNAME, PASSWORD
from tagger.tag_functions import get_post_id_from_url, get_or_create_category_id, update_post_categories
import pandas as pd
import re
import requests
import ast
import time
import random


# session setup for authentication 
session = requests.Session()
session.auth = (USERNAME, PASSWORD)


# load the data
df = pd.read_csv(FILE)
print(f'There is a total of {df.shape[0]} posts to be updated')

for idx, row in df.iterrows():
    # add random sleep time
    sec = random.random() * 2  # add a random delay 

    post_url = row['link']
    title = row['title']
    
    try:
        # convert the cat labels to actual list
        category_list = ast.literal_eval(row['tags'])
    except(ValueError, SyntaxError):
        print(f'Skipping {title} due to invalid format in tags column')
        continue

    print(f'Processing the post: {title}...')

    post_id = get_post_id_from_url(session, post_url)
    if not post_id:
        print(f'Could not find post ID for post {title}')
        continue
    cat_ids = []
    for cat_name in category_list:
        cat_id = get_or_create_category_id(session, cat_name)
        if cat_id:
            cat_ids.append(cat_id)
    
    if cat_ids:
        success = update_post_categories(session, post_id, cat_ids)
        if success:
            print(f'Categories updated successfully!')
        else:
            print(f'Failed to update categories for {title}, no new categories to applied')
    else:
        print(f'No valid category IDs could be resolved for {title}')
    time.sleep(sec)
    print(f'Paused for {sec}...')