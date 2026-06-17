# the script for crawling the blog posts
import requests
from bs4 import BeautifulSoup


def fetch_blog_title(page_number): # get the blog title and link to the post from the page number
    url = f"https://internationalstudents.blog.liu.se/blog/page/{page_number}"
    # store the results 
    blog_posts ={}
    print(f"Loading page {page_number}...")
    try: 
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # fetch all the blog titles
            titles = soup.find_all('h2', class_='card-title')
            links = soup.find_all('a', class_='card')

            for title, link in zip(titles, links):
                blog_posts[title.get_text()] = link['href']
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    return blog_posts

def fetch_blog_content(blog_url): # get the content of the blog post from the link
    try:
        response = requests.get(blog_url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            content = soup.find('div', class_='post-content')
            return content.get_text()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None