from tagger.config import WP_URL
import pandas as pd
import re
import requests
import ast

def get_post_id_from_url(session, url):
    # extract slug from URL and fetch the wordpress post id
    slug = url.strip().rstrip('/').split('/')[-1]

    response = session.get(f'{WP_URL}/posts', params={"slug": slug})
    if response.status_code == 200 and response.json():
        return response.json()[0]['id']
    else:
        print(f"Could not find slug '{slug}' via API. Status: {response.status_code}")
    return None

def get_or_create_category_id(session, cat_name):
    # find category id by name or create the category if not exist
    response = session.get(f'{WP_URL}/categories', params={'search':cat_name})
    if response.status_code == 200 and response.json():
        for cat in response.json():
            if cat['name'].lower() == cat_name.lower():
                return cat['id']
    
    # if not exist, create the category
    create_res = session.post(f'{WP_URL}/categories', json={'name': cat_name})
    if create_res.status_code == 201:
        return create_res.json()['id']
    if create_res.status_code == 400:
        res_data = create_res.json()
        if res_data.get('code') == 'term_exists':
            return res_data.get('data', {}).get('term_id')
    print(f'Catetory erro for "{cat_name}": {create_res.text}')
    return None

def update_post_categories(session, post_id, category_ids):
    # append new categories to the post
    post_res = session.get(f'{WP_URL}/posts/{post_id}')
    existing_cats = post_res.json().get('categories', []) if post_res.status_code == 200 else []

    # merge existing and new unique categories
    all_cats = list(set(existing_cats + category_ids))

    # update the post 
    update_res = session.post(f'{WP_URL}/posts/{post_id}', json={'categories':all_cats})
    return update_res.status_code == 200
